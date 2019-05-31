class A:
    def __init__(self):
        self.x = 'a'
        print("A", self.x)

class B(A):
    def __init__(self):
        super().__init__()
        self.x = "b"
        print("B", self.x)

class C(A):
    def __init__(self):
        super().__init__()
        self.x = 'c'
        print("C", self.x)

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D", self.x)

D()   
