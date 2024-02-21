'''  适配器模式 
动机：      
有两个不存在直接继承或关联关系的类A、B， A希望能利用到B类中某个已存在的、功能完善的方法，而不再去具体实现A的接口源码；适配器模式使接口不兼容的那些类可以一起工作。

主要角色：
1. 目标类   Target   抽象接口类
2. 适配者   Adaptee     
3. 适配器   Adapter  具体实现接口
4. 客户端   Client
客户端针对目标类编程，希望调用目标类的某个方法；而适配者中已经提供了关于Target中该方法的完整实现。

具体分为两种类型，类适配器、对象适配器（使用频率更高、更灵活）：
类适配器：  Target与Adapter是继承关系，Adapter与Adaptee也是继承关系
public class Adapter extends Adaptee implements Target{
    public void request(){
        super.specificRequest();
    }
}

对象适配器： Target与Adapter是继承关系，然而Adapter与Adaptee之间是委派关系（在Adapter中定义一个Adaptee的对象）

由于语法的限制，有些语言中一个类只能单继承一个父类，所以类适配器可能不太适合使用；并且即使能多继承、假设适配多个父类这样也不太好扩展。
public class Adapter extends Target{
    private Adaptee adaptee;    // 委派一个对象

    public Adapter(Adaptee x){
        this.adaptee = x;
    }
    
    public void request(){
        adaptee.specificRequest(); 
    }
}
如果有新的Adaptee，不用修改源代码，只需要增加一个新的Adapter（继承Target）即可

需要设计一个可以模拟各种动物行为的机器人，在机器人中定义一系列方法，如叫喊cry、移动move；如果已存在一个狗的类，其中已经定义了功能类似的wang和run方法；

'''
from abc import ABC,abstractmethod

class Robot(ABC):
    @abstractmethod
    def cry(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog:
    def wang(self):
        print("狗儿_wang wang wang!")
    
    def run(self):
        print("狗儿_run run run!")

class Bird:
    def tweedle(self):
        print("鸟儿_ji ji ji!")
    
    def fly(self):
        print("鸟儿_fly fly fly!")

# 对象适配1
class DogAdapter(Robot):    # 让机器人适配狗特性的适配器类
    def __init__(self):
        self.__adaptee = Dog()
    
    def cry(self):
        print("机器人模仿狗的叫喊：")
        self.__adaptee.wang()
    
    def move(self):
        print("机器人模仿狗的移动：")
        self.__adaptee.run()

# 对象适配2
class BirdAdapter(Robot):    # 让机器人适配狗特性的适配器类
    def __init__(self):
        self.__adaptee = Bird()
    
    def cry(self):
        print("机器人模仿鸟的叫喊：")
        self.__adaptee.tweedle()
    
    def move(self):
        print("机器人模仿鸟的移动：")
        self.__adaptee.fly()

class Client:
    def __init__(self, AdapterName):
        self.Adapter = AdapterName
    
    def run(self):
        try:
            robot = eval(self.Adapter)()
            robot.cry()
            robot.move()

        except NameError:
            print(f"Error! Robot adapter '{self.Adapter}' doesn't exits...")

if __name__ == '__main__':
    rb1 = Client('DogAdapter')
    rb1.run()
    print()
    rb2 = Client('BirdAdapter') 
    rb2.run()
