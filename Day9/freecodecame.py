#unbox a collection
students=["Swathi","Uday","Manisha","Zynab"]
a,b,c,d=students
print(a)
print(b)
print(c)
print(d)

#String concatenation
name='shriya'       #declaring a variable
rollno=37           #2nd variable
Name=name           #start with name
Name+=str(rollno)   #concatenation(+=)
print(Name)

#f-string
name1='Shriya'
Rollno=37
name1_Rollno=f'My name is {name1} and my roll number is{Rollno}'
print(name1_Rollno)

num1=5
num2=10
print(f'The sum of {num1} and {num2} is {num1+num2}')
