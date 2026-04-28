class Solution:
    def operations(self, x, y):
        # Perform addition
        p = x + y
        
        # Perform subtraction
        q = x - y
        
        # Perform multiplication
        r = x * y
        
        # Perform division (integer division)
        s = x // y
        
        # Perform modulo
        t = x % y

        # Print result
        print(p, q, r, s, t)

#logical operator
a = int(input())
b = int(input())

# Do a and b
p = a and b

# Do a or b
q = a or b

# Do not a
r = not a

# The code below prints the output. Don't change it!
print(p, q, r)

#Bitwise operator
a=int(input())
b=int(input())
c=int(input())
#code here
#Do a^a below
d= a ^ a
#Do c^b below
e= c ^ b
#Do a&b below
f= a&b
#Do c|(a^a) below
g= c|(a^a)
#Do ~e below
e= ~e
print(d, e, f, g)

#last digit of a number
def lastDigit(self, n: int) -> int:
        if n < 0:
            n = 24
        return n % 10


#lists
mylist=list(map(int,input("enter num").split()))
if len(mylist)>=2:
     print("second ele",mylist[1])
print("even num of list")
for n in mylist:
     if n%2==0:
          print(n)
