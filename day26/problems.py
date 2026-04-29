# class std:
#     def __init__(self):
#         print("Student is good at math")
# cl=std()


#last digit of a number
def lastDigit(self, n: int) -> int:
        if n < 0:
            n = 24
        return n % 10

#logical operator
a = int(input("enter"))
b = int(input("enter"))

# Do a and b
p = a and b

# Do a or b
q = a or b

# Do not a
r = not a

# The code below prints the output. Don't change it!
print(p, q, r)
