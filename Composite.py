'''
组合模式(Composite Pattern)：  组合多个对象形成树形结构，以表示“部分-整体”的结构层次。组合模型对单个对象（叶子对象）和组合对象（容器对象）的使用具有一致性。
是一种对象结构型设计模式。
将对象组织到树形结构中，可以用来描述整体与部分的关系。

## 主要包含的角色
- Component 抽象构件（父类）
- Leaf      叶子构件（子类1）
- Composite 容器构件（子类2），内含一个集合children，可以存储容器内的所有成员（都是Component类型）。

### 透明组合模式：
1. 抽象构件Component中声明了所有用于管理成员对象的方法
2. 在客户端眼里，Leaf和Composite提供的业务方法是一致的，客户端可以一致地对待所有的对象
3. 缺点是不够安全，因为叶子对象和容器对象本质上是有区别的

### 安全组合模式：
1. 抽象构件Component中不会声明任何用于管理成员对象的方法，而是在容器对象Composite中声明并实现这些方法
2. 对于叶子对象Leaf，客户端不可能调用到这些方法
3. 缺点是不够透明，客户端不能完全针对抽象编程，必须有区别的对待叶子构件和容器构件

## 案例：   树形文件系统、水果盘

## 总结
### 优点
- 可以清楚地定义分层次的复杂对象，表示对象的全部或部分层次，让客户端忽略了层次的差异，方便对整个层次结构进行控制
- 客户端可以一致地使用一个组合结构或其中单个对象，不必关心处理的是单个对象还是整个组合结构，简化了客户端代码
- 增加新的容器构件和叶子构件都很方便，符合开闭原则
- 为树形结构的面向对象实现提供了一种灵活的解决方案

### 缺点
- 在增加新构件时很难对容器中的构件类型进行限制
'''
import typing
from abc import ABC,abstractclassmethod

class MyElement(ABC):  
    @abstractclassmethod
    def eat(self):
        pass

class Apple(MyElement):
    def eat(self):
        print("吃苹果！")

class Peer(MyElement):
    def eat(self):
        print("吃梨子！")

class Banana(MyElement):
    def eat(self):
        print("吃香蕉！")

class Orange(MyElement):
    def eat(self):
        print("吃橘子！")

class Melon(MyElement):
    def eat(self):
        print("吃甜瓜！")

class Pineapple(MyElement):
    def eat(self):
        print("吃菠萝！")

class Strawberry(MyElement):
    def eat(self):
        print("吃草莓！")

class Grape(MyElement):
    def eat(self):
        print("吃葡萄！")

class Grapefruit(MyElement):
    def eat(self):
        print("吃西柚！")

class Pitaya(MyElement):
    def eat(self):
        print("吃火龙果！")

class Kiwifruit(MyElement):
    def eat(self):
        print("吃猕猴桃！")

class Cherry(MyElement):
    def eat(self):
        print("吃樱桃！")

class Litchi(MyElement):
    def eat(self):
        print("吃荔枝！")

# 盘子，容器构件，包含一个集合
class Plate(MyElement):
    def __init__(self):
        self.__list = []
    def add(self, c : MyElement):
        self.__list.append(c)
    
    def remove(self, c : MyElement):
        self.__list.remove(c)
    
    def eat(self):
        for c in self.__list:
            c.eat()

class Client:
    def run(self):
        f1 = Apple()
        f2 = Peer()
        p1 = Plate()
        p1.add(f1)
        p1.add(f2)

        f3 = Orange()
        f4 = Banana()
        p2 = Plate()
        p2.add(f3)
        p2.add(f4)

        f5 = Litchi()
        p3 = Plate()
        p3.add(p1)
        p3.add(p2)
        p3.add(f5)

        p3.eat()


if __name__ == '__main__':
    x = Client()
    x.run()