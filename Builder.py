'''
建造者模式是一步一步构建一个复杂的对象，属于对象创建型模式。
将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示。
关注如何逐步创建一个复杂的对象，不同的创造者定义了不同的创建过程
可以精细地控制产品的创建过程（关注次序）。
适用场景：创建产品或套餐需要有共同点、组成成分相似（food+drink）；如果产品组成差异性大则不适合用本模式。

KFC套餐案例：
套餐是一个复杂对象，他一般包含主食（汉堡或鸡肉卷）和饮料（可乐或果汁）等组成部分，不同的套餐有不同的组成部分；
服务员可根据顾客的要求一步一步装配这些组成部分，构造一分完整的套餐，然后返回给顾客。
'''  
from abc import ABC, abstractmethod

class Meal: # 套餐类
    def __init__(self, food = None, drink = None):
        self.fd = food
        self.dk = drink 

    @property
    def food(self):
        return self.fd
    
    @food.setter
    def food(self, fdname):
        self.fd = fdname

    @property
    def drink(self):
        return self.dk
    
    @drink.setter
    def drink(self, dkname):
        self.dk = dkname

class MealBuilder:  # 套餐创建者 
    def __init__(self):
        self._meal = Meal()  # 初始化套餐

    @abstractmethod
    def buildFood(self):    # 构造套餐组成1：food
        pass

    @abstractmethod
    def buildDrink(self):   # 构造套餐组成2：drink
        pass

    def getMeal(self):  # 返回完整的套餐对象
        return self._meal

class PlanA(MealBuilder):   # 具体套餐A
    def buildFood(self):
        self._meal.food = "一个鸡腿堡"
    
    def buildDrink(self):
        self._meal.drink = "一杯可乐"

class PlanB(MealBuilder):   # 具体套餐B
    def buildFood(self):
        self._meal.food = "一个鸡肉卷"
    
    def buildDrink(self):
        self._meal.drink = "一杯果汁"

class KFCWaiter:    # 指挥者  
    def __init__(self):
        self.mb = MealBuilder() # 包含一个抽象的套餐建造者
    
    def setMealBuilder(self, mb):   # 注入一个具体的套餐建造者对象
        self.mb = mb
    
    def construct(self):        # 注意构造顺序
        self.mb.buildFood()     # 构造子部件1
        self.mb.buildDrink()    # 构造子部件2
        return self.mb.getMeal() # 返回完整的套餐对象

class Client:
    def __init__(self, taocan : str):
        self.mealbuilder = taocan
        
    def run(self):
        try:
            mb = eval(self.mealbuilder)()
            waiter = KFCWaiter()
            waiter.setMealBuilder(mb)   # 本质上由mb决定选择的套餐
            meal = waiter.construct()
            print(" 套餐组成：")
            print(meal.food)
            print(meal.drink)
        except:
            print(f"套餐{self.mealbuilder}不存在！！")

if __name__ == '__main__':
    bob = Client('PlanA')
    bob.run()
    
    print("-"*20)

    David = Client('PlanB')
    David.run()