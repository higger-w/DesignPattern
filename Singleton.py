'''
单例设计模式是为了保证一个类，无论调用多少次产生的实例对象，都是指向同一个内存地址，仅仅只有一个实例（只有一个对象）
'''

# class Singleton(object):

#     def __init__(self, name):
#         self.name = name
#         print(f"__init__ name is {self.name}")

#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance

# from threading import RLock
# class Singleton(object):
#     single_lock = RLock()

#     def __init__(self, name):
#         self.name = name
#         print(f"__init__ name is {self.name}")

#     @classmethod
#     def instance(cls, *args, **kwargs):
#         with Singleton.single_lock:
#             if not hasattr(Singleton, "_instance"):
#                 Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance


single_1 = Singleton.instance('第1次创建')
single_2 = Singleton.instance('第2次创建')

print(single_1 is single_2)     # True

