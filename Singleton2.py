def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)   # 仅初始化1次生成一个唯一的对象
        return instances[cls]
    return getinstance
 
@singleton
class Country:
    def __init__(self, name, area):
        self.name = name 
        self.area = area
        print(f"Country name: {self.name}, land area: {self.area} km^2.")

 
a = Country('China', 965)
b = Country('Japan', 75)

print(a == b)   # True，因为 a 和 b 引用的是同一个实例

print(a.name, a.area)
print(b.name, b.area)