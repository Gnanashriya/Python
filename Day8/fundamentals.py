x, y, z = 1, 2.5, "Python"
print(x, y, z)

a=2
b=3
# Floor Division
print("Floor Division:", a // b)
# Division
print("Division:", a / b) 

# Modulus
print("Modulus:", a % b) #remainder of the division

# Exponentiation
print("Exponentiation:", a ** b)
a=int((input ("enter a number: ")))

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = []
        for i in range (1,n+1):
            if i%3==0 and i%5==0:
                s.append("FizzBuzz")
            elif  i%3==0:
                s.append("Fizz")
            elif i%5==0:
                s.append("Buzz")
            else :
                s.append(str(i))
        return s
