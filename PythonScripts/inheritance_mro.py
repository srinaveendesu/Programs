class A():
    def a(self):
        print('this is a')


class B(A):
    def a(self):
        #super().a()
        print('this is b')

class C(B):
    def a(self):
        print('this is c')

c = C()
print (super.__base__)
c.a()
super(C,c).a()
super(B, c).a()
print (C.__mro__)

# <class 'object'>
# this is c
# this is b
# this is a
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


class Example():
    @classmethod
    def example_class_method(cls):
        print("This is Example")


class Example2(Example):
    @classmethod
    def example_class_method(cls):
        print("This is Example2")


example = Example2()
super(Example2, example).example_class_method()

# This is Example


class AA():
    pass

class BB():
    pass

class CC():
    pass

class X(AA, BB):
    pass

class Y(BB, CC):
    pass

class Z(X,Y):
    pass


print (Z.__mro__)
print (X.__mro__)
# (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.AA'>, <class '__main__.Y'>, <class '__main__.BB'>,<class '__main__.CC'>, <class 'object'>)
"""
(AA,O)
(BB,O)
(CC,O)
(X,AA,BB)
(Y, BB, CC)
(Z, X, Y) -> (Z (X ,AA,BB) (Y, BB, CC) ) -> (Z , X (AA,BB) (Y BB CC) ) -> (Z,X,AA, (BB) (Y BB CC)) -> (Z,X,AA,Y (BB) (BB CC) ) -> (Z,X,AA,Y,BB,CC)

L[A] = A + merge(BDEO,CDFO,BC)
     = A + B + merge(DEO,CDFO,C)
     = A + B + C + merge(DEO,DFO)
     = A + B + C + D + merge(EO,FO)
     = A + B + C + D + E + merge(O,FO)
     = A + B + C + D + E + F + merge(O,O)
     = A B C D E F O
"""