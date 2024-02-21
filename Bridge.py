'''  桥接模式 Bridge Pattern
动机：将抽象部分与实现部分分离，是他们都可以独立地变化。用抽象关联取代传统的多层继承。将类之间的静态继承关系转换为动态的对象组合关系。
优点：
- 分离抽象接口及实现部分
- 可以取代多层继承方案，极大地减少子类的个数
- 提高系统的可扩展性，在两个变化维度中任意扩展一个维度，不需要修改原有系统，符合开闭原则

缺点：
- 关联关系建立在抽象，会增加系统的理解与设计难度
- 正确识别两个独立的变化维度有难度
'''
from abc import ABC,abstractmethod
import typing

class Color(ABC):   # 抽象类
    @abstractmethod # 笔类型、图形类型
    def bepaint(self, penType : str, name : str):
        pass

class Black(Color):
    def bepaint(self, penType: str, name: str):
        print(f"{penType} 黑色的 {name}.")

class Blue(Color):
    def bepaint(self, penType: str, name: str):
        print(f"{penType} 蓝色的 {name}.")

class Green(Color):
    def bepaint(self, penType: str, name: str):
        print(f"{penType} 绿色的 {name}.")

class Red(Color):
    def bepaint(self, penType: str, name: str):
        print(f"{penType} 红色的 {name}.")

class Yellow(Color):
    def bepaint(self, penType: str, name: str):
        print(f"{penType} 黄色的 {name}.")


class Pen(ABC):
    def __init__(self):
        self._color = None
    
    def setColor(self, color):
        self._color = color
    
    @abstractmethod
    def draw(self, name):
        pass

class BigPen(Pen):
    def draw(self, name):
        penType = "大号毛笔绘制"
        self._color.bepaint(penType, name)

class MiddlePen(Pen):
    def draw(self, name):
        penType = "中号毛笔绘制"
        self._color.bepaint(penType, name)

class SmallPen(Pen):
    def draw(self, name):
        penType = "小号毛笔绘制"
        self._color.bepaint(penType, name)
    
class Client:
    def __init__(self, col: str, pen:  str):
        self.Color  = eval(col)()
        self.PenType = eval(pen)()
        try:
            self.Color  = eval(col)()
        except NameError:
            print("Error! 所指定颜色不存在！")
        
        try:
            self.PenType = eval(pen)()
        except NameError:
            print("Error! 所指定毛笔类型不存在！")

    def run(self, shape:str):
        self.PenType.setColor(self.Color)
        self.PenType.draw(shape)

if __name__ == '__main__':
    c1 = Client(col = 'Red', pen = 'SmallPen')
    c1.run('乌龟')

    c2 = Client(col = 'Blue', pen = 'MiddlePen')
    c2.run('飞机')