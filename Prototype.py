import copy
from abc import ABC,abstractmethod

class Prototype(ABC):    # 抽象类，声明对象的克隆接口
    @abstractmethod
    def clone(self):    # 返回一个类型为自己的对象
        pass

class Email_S(Prototype):   # shallow copy 
    def __init__(self, sd, rp, tt, date, msg, apd):
        self.sender = sd
        self.recipient = rp
        self.title = tt
        self.date = date
        self.message = msg
        self.appendix = apd     # list

    def clone(self):    # 浅克隆对象
        return copy.copy(self)
    
    def display(self):
        print('-'*50)
        print(f"  Time  : {self.date}    Title:{self.title}")
        print(f" Sender : {self.sender}" + ' '*18 + f"Recipient:{self.recipient}")
        print(f" Message: {self.message}")
        print(f"Appendix: {self.appendix}")
        print('-'*50)
    
    def getAppendix(self):
        return self.appendix

class Email_D(Prototype):   # deep copy
    def __init__(self, sd, rp, tt, date, msg, apd):
        self.sender = sd
        self.recipient = rp
        self.title = tt
        self.date = date
        self.message = msg
        self.appendix = apd     # list

    def clone(self):    # 深克隆对象
        return copy.deepcopy(self)
    
    def display(self):
        print('+'*50)
        print(f"  Time  : {self.date}    Title:{self.title}")
        print(f" Sender : {self.sender}" + ' '*18 + f"Recipient:{self.recipient}")
        print(f" Message: {self.message}")
        print(f"Appendix: {self.appendix}")
        print('-'*50)

if __name__ == '__main__':
    mail1 = Email_S('Alice', 'Bob', 'Marry Me', '2023-12-12 10:00:00', 'I like you very much, please be my wife!', [1,2,3])
    _mail1 = mail1.clone()  # 浅克隆一份

    # mail1.display()
    # _mail1.display()

    mail1.appendix.append(400)  # 修改源对象的引用类型附件对象

    mail1.display() 
    _mail1.display()        # 浅拷贝后可变对象的值也一样

    print("\n")

    mail2 = Email_D('Bob', 'Alice', 'Reply', '2023-12-12 11:00:00', 'Fxxk you, gun ni ma de :) ', [4,5,6])
    _mail2 = mail2.clone()  # 深克隆一份

    # mail2.display()
    # _mail2.display()

    mail2.appendix.append(700)  # 修改源对象的引用类型附件对象

    mail2.display()         # 深拷贝后可变对象的值不一样
    _mail2.display()