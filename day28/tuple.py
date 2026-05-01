#mulitple inheritance
class A:
    def cls1(self):
        print("section 1")
class B:
    def cls2(self):
        print("section 2")
class C(A,B):
    def cls3(self):
        print("section 3")
C=C()
C.cls1()

#mulilevel inheritance
class gp:
    def grandp(self):
        print("grand parents")
class par(gp):
    def parent(self):
        print("parent")
class child(par):
    def child(self):
        print("child")
a=gp()
a.grandp()
obj=par()
obj.parent()
c=child()
c.child()



