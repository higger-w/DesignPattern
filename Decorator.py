'''
# 装饰设计模式 Decorator Pattern

## 模式动机
- 是一种对象结构型模式
- 可以在不改变一个对象本身功能的基础上给对象增加额外的新行为
- 是一种用于替代继承的技术，他通过一种无须定义子类的方式给对象动态增加职责，使用对象之间的关联关系取代类之间的继承关系
- 引入了装饰类，在装饰类中既可以调用待装饰的原有类的方法，还可以增加新的方法，以扩展原有类的功能

- 以对客户透明的方式动态给一个对象附加上更多的责任
- 可以再不需要创建更多子类的情况下，让对象得功能得以扩展

## 角色
- Component         抽象构件类：抽象接口，只声明通用方法
- ConcreteComponent 具体构件类：实现了一些基本方法
- Decorator         抽象装饰类：是所有装饰类的父类，同时是Component的子类，会关联（注入）一个Component类的子类对象
- ConcreteDecorator 具体装饰类：扩展抽象装饰类，提供更多功能


## 透明装饰模式
- 完全针对抽象编程，不该将对象声明为具体构件类型或具体装饰类型，应该全声明为抽象构件类型
- 可以透明地使用装饰之前的对象和装饰之后的对象，无须关心其区别
- 某个已装饰过的对象，可以继续注入另一个ConcreteDecorator，实现多层装饰
- 无法单独调用addedBehavior()方法
`
Component o,d1,d2; //全部使用抽象构件类型定义
o = new ConcreteComponent();
d1 = new ConcreteComponent(o);
d2 = new ConcreteComponent(d1);
d2.operation();  // 无法单独调用d2的addedBehaviour()方法
`

## 半透明装饰模式 Semi-transparent
- 可以给系统带来更多灵活性，设计简单，使用方便
- 使用具体装饰类型来定义装饰后的对象，因此可以单独调用addedBehavior()方法
- 缺点在于，不能实现对同一对象的多次装饰，而且需要有区别地对待装饰前、装饰后的对象
`
Component c1;   // 使用抽象构件类型定义
c1 = new ConcreteComponent();
c1.operation();

ConcreteDecorator c2;   // 使用具体装饰类型定义
c2 = new ConcreteDecorator(c1);
c2.operation();
c2.adderBehaviour();    // 单独调用新增业务方法
`
'''
from abc import ABC, abstractmethod

class Transform(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transform):
    def __init__(self):
        print("变形金刚是一辆车！")

    def move(self):
        print("在陆地上移动！")

class Changer(Transform):       # 抽象装饰类 （变形）
    def __init__(self, trans : Transform) -> None:
        self.__transform = trans
    
    def move(self):
        self.__transform.move()

class Airplane(Changer):
    def __init__(self, trans: Transform) -> None:
        super().__init__(trans)
        print("变形成飞机！")
    
    def fly(self):
        print("在天空飞翔！")

class Robot(Changer):
    def __init__(self, trans: Transform) -> None:
        super().__init__(trans)
        print("变形成机器人！")
    
    def fire(self):
        print("向霸天虎开火！")

if __name__ == '__main__':
    '''
    半透明装饰方法
    '''
    camero = Car()  # 具体构件类
    camero.move()

    print("--------------")

    bumblebee = Airplane(camero)
    bumblebee.move()
    bumblebee.fly() # 调用到了具体装饰类Airplane中新增加的方法

    print("+++++++++++++++")
    
    # X = Robot(camero)
    # X.move()
    # X.fire() 

    X = Robot(bumblebee)
    X.move()
    X.fire()
    # X.fly()   半透明装饰模式只具有最后一次具体装饰类的功能、属性，会丧失中间层装饰类的功能、属性