

class A :
    pass

class B(A) :
    pass

class C(A) :
    pass

class D(C) :
    pass

class E(D,B,C) :
    pass

print(E.mro())
