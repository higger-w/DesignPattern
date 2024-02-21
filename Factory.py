from abc import ABC,abstractmethod

class TV(ABC):      # 抽象产品
    @abstractmethod
    def play(self):
        pass

class HaierTV(TV):  # 具体产品1
    def play(self):
        print(f"海尔电视播放中...") 

class HuaweiTV(TV): # 具体产品2
    def play(self):
        print(f"华为电视播放中...") 

class TVFactory(ABC):   # 抽象工厂
    @abstractmethod
    def productTV(self):
        pass

class HaierTVFactory(TVFactory):
    def productTV(self):
        print("海尔TV工厂生产海尔电视机！")
        return HaierTV()

class HuaweiTVFactory(TVFactory):
    def productTV(self):
        print("华为TV工厂生产华为电视机！")
        return HuaweiTV()

class Client:
    def __init__(self, pname):
        self.product = pname    # 可以从配置文件读取，也可以用户在main函数中创建对象时输入
    
    def run(self):
        try:
            factory = eval(self.product)()  # 字符串名称  转  具体产品工厂对象
            tv = factory.productTV()
            tv.play()
        except NameError:
            print(f"Error! Product '{self.product}' doesn't exits...")

if __name__ == '__main__':
    t1 = Client('HaierTVFactory')
    t1.run()

    t2 = Client('HuaweiTVFactory')
    t2.run()