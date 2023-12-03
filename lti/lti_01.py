"""
create a class
few methods
Add of a and b
override methodA
override to multiply
"""

class cal():
    def method_1(self, a, b):
        add = a + b
        print(add)

    def method_2(self):
        print("Method 2")


class calc(cal):
    def method_1(self, a, b):
        mul = a * b
        print(mul)

obj1 = calc()
obj1.method_1(10, 20)
obj = cal()
obj.method_1(10, 20)