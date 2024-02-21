'''
一、简单工厂模式   或   静态工厂模式
包含角色：
    1. 工厂角色      Factory    静态方法      
    2. 抽象产品角色   Product    声明公用的抽象方法和属性
    3. 具体产品角色   ConcreteProduct   覆盖抽象产品中声明的方法，多种产品多种覆盖

可以降低系统耦合度，使用工厂方法时无需知道对象创建细节，传入工厂类的参数可以是字符串、也可以是提前规定好的整型参数
但是所有产品都由一个工厂来生产，工厂类的职责相对较重，添加新产品需要修改工厂类的判断逻辑，违背开闭原则

适合生产较少的产品，工厂类中的控制逻辑比较简单
'''
from abc import ABC,abstractmethod

class TV(ABC):      # 抽象产品
    @abstractmethod
    def play(self):     # , price
        pass

class HaierTV(TV):  # 具体产品1
    def play(self):
        print(f"海尔电视播放中...") # 售价{price}元

class HuaweiTV(TV): # 具体产品2
    def play(self):
        print(f"华为电视播放中...") # 售价{price}元

class TVFactory:
    @staticmethod
    def productTV(brand):
        if brand == 'Haier':
            print("TV工厂生产海尔电视机！")
            return HaierTV()
        elif brand == 'Huawei':
            print("TV工厂生产华为电视机！")
            return HuaweiTV()
        else:
            raise TypeError("There aren't this brand product.")
    
class Client:
    def __init__(self, brandName):
        self.brand = brandName

    def run(self):  # , price
        # tv = TV()   # tv产品  定义为  抽象TV类
        # tf = TVFactory()
        tv = TVFactory.productTV(self.brand)    # tf.productTV(self.brand)
        tv.play()   # price

if __name__=='__main__':
    t1 = Client('Haier')
    t1.run()    # 100

    t2 = Client('Huawei')
    t2.run()    # 200