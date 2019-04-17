from django.test import TestCase


# Create your tests here.


class A(object):
    pass


a1 = A()
a2 = A()


#

# class A(object):
#     def __init__(self):
#         self.y=10
#         self.x=44
#     x=10
#     y=12
#
# class B(A):
#
#     x=8
#     y=20
#
# b=B()
# print(b.y)
# print(b.x)

########################-----单例模式----############################


# 基于__new__模式

class Settings(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Settings, cls).__new__(cls, *args, **kw)
        return cls._instance


s1 = Settings()
s2 = Settings()

print(s1 == s2)
print(id(s1))
print(id(s2))

# 基于模块的模式
