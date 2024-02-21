'''
系统中出现多个产品族（品牌），但每次只使用其中一个产品族
缺点是引入了很多的类，分析会更复杂
'''

from abc import ABC,abstractmethod

class TV(ABC):      # 抽象产品 1
    @abstractmethod
    def play(self):
        pass

class AirConditioner(ABC):  # 抽象产品 2
    @abstractmethod
    def changetemperature(self):
        pass

class HaierTV(TV):  # 具体产品
    def play(self):
        print("海尔电视播放中...")

class HuaweiTV(TV): # 具体产品
    def play(self):
        print("华为电视播放中...")

class HaierAirCon(AirConditioner):  # 具体产品
    def changetemperature(self):
        print("海尔空调温度改变中!!!")

class HuaweiAirCon(AirConditioner): # 具体产品
    def changetemperature(self):
        print("华为空调温度改变中!!!")

class EFactory(ABC):    # 抽象工厂
    @abstractmethod
    def produceTV(self):
        pass
    
    @abstractmethod
    def produceAirCon(self):
        pass

class HaierFactory(EFactory):   # 具体产品族工厂1
    def produceTV(self):
        return HaierTV()
    
    def produceAirCon(self):
        return HaierAirCon()

class HuaweiFactory(EFactory):  # 具体产品族工厂2
    def produceTV(self):
        return HuaweiTV()
    
    def produceAirCon(self):
        return HuaweiAirCon()

class Client:                   # 客户端
    def __init__(self, FactoryName):    # 传入工厂名称参数
        self.factname = FactoryName

    def run(self):
        try:
            factory = eval(self.factname)()
            tv = factory.produceTV()
            tv.play()

            ac = factory.produceAirCon()
            ac.changetemperature()
        except NameError:
            print(f"Error! Factory '{self.factname}' doesn't exits...")

if __name__ == '__main__':
    f1 = Client('HuaweiFactory')
    f1.run()

    f2 = Client('HaierFactory')
    f2.run()