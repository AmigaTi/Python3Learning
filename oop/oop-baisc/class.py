#!/usr/bin/python
# -*- coding: utf-8 -*-


# __init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，
# 因为self就指向创建的实例本身。

# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量，
# 只有内部可以访问，外部不能访问

# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量
# 但是不同版本的Python解释器可能会把__name改成不同的变量名。

# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Wrong score')

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

    def __private_method(self):     # 外部不能调用此私有方法
        print('call private method')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
bart.print_score()        # Bart Simpson : 59
grade = bart.get_grade()
print(grade)              # C
names = bart.get_name()
print(names)              # Bart Simpson

# bart.__private_method()     # AttributeError: 'Student' object has no attribute '__private_method'
# bart._Student__private_method()     # call private method
