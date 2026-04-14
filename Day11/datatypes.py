#global variable
x="awesome"
def myfun():
    x="easy"
    print("Python is "+ x+'to use')
myfun()
print('Python is '+x)
print("-------------------")

#global keyword
y="awesome"
def mycode():
    global y
    y='fantastic'
    print('Python is '+y)
mycode()
print(y)

print("---------------------")

def nums(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
nums(5,6)
   