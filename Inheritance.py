class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Fetute 2 working")


class B:
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("feature 4 working")


class C(A, B):
    def feature5(self):
        print("feature 5 working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

c1 = C()
c1.feature1()