class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Fetute 2 working")


class B(A):

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("feature 4 working")


class C:

    def __init__(self):
        print("in C init")

    def feature5(self):
        print("feature 5 working")


class D(A, C):
    def __init__(self):
        super().__init__()
        print("in D init")

    def feat(self):
        super().feature2()

a1 = D()
a1.feat()