class A (object):
    val1 = 'hello'
    val2 = "world"

    def fun1(self):
        print(self.val1)
    def fun2 (self):
        self.val1 = "bye"
        print("change!")
    def fun3(self):
        print(self.val1 + " " + self.val2)

a1 = A()
a2 = A()
A.val2 = "beautiful world"
a1.fun3()
a2.fun3()

a1.fun2()
a1.fun3()

a2.fun3()

def fun4(self):
    print("bye bye")

A.fun1 = fun4
a1.fun1()
#a1.fun4()报错，可见改的是内容

def fun5(self):
    print("hello hello")
def fun6():
    print("hello hello")
#wrong
#a1.fun1 = fun5
#a1.fun1()
a1.fun1 = fun6
a1.fun1()
a2.fun1()


class User1(object):
    pass
class User2(User1):
    pass
class User3(User2):
    pass


user1 = User1()
user2 = User2()
user3 = User3()
# isinstance()就可以告诉我们，一个对象是否是某种类型
# print(isinstance(user3, User2))
# print(isinstance(user3, User1))
# print(isinstance(user3, User3))
# print(isinstance(user2, User2))
# print(isinstance(user2, User1))
# print(isinstance(user2, User3))
# print(isinstance(user1, User2))
# print(isinstance(user1, User1))
# print(isinstance(user1, User3))

print(type(user3))
print(type(User3))

