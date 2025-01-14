

a = 10
print(a)
a="hello"
print(a)
a='A'
print(a)
print("sanket") 
print("hi")
print("hello")
print("hello" ,end= " ")
print("sanket this is python")
a = 10
print(a) 
b =10
print(b)
print(id(a))
print(id(b))
a, b = 10, 3
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Power:", 2 ** 3)           # 8

"""n = int(input("enter the number of your wish"))
print("Enter the value you want check odd or even " , n)
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
"""

n = int(input("Enter the number of your wish"))
print("Enter the value you want to check odd or even" , n)
if(n % 2 == 0):
    print("n is even")
else:
    print("n is odd")

"""if
elif ladder
"""

w = int(input("Enter any value of your wish"))
print("checking the if elif ladder", w)
if w > 10:
    print("greater than 10")
elif w > 5:
    print("greater than 5")
else:
    print("greater than 0")
"""
gretest of 3 number

"""
g =int(input("Enter the value of first number"))
h = int(input("Enter the value of second number"))
k = int(input("Enter the value of third number"))
print("the first number to test the greatest of 3 number is " , g)
print("the second number to test the greatest of 3 number is " , h)
print("the third number to test the greatest of 3 number is " , k)
if g > h and g > k :
    print("the greatest number is ",g)
elif h > k:
    print("the greatest number is",h)
else:
    print("the greatest number is ",k)

str = "abc"
for x in str:
    print(x)
l = int(input("enter the value"))
print("enter the value of variable of your wish",l)
for f in range(1,l):
    print(f)
    """while loop"""
    i =1
    while i <=10:
        i= i+1
        print(i)
"""
  prime Number
  

number = int(input("enter number"))
print("the number you have entered is ", number)
i = 2
checkPrime= False
while i < number:
    if number % i == 0:
        checkPrime = True
        i= i+1
        if checkPrime:
            print("not Prime")
        else:
            print("Prime")
            """
"""
Use of break, continue and pass in for loop
"""
for i in range(3):
    if i == 2:
        break
    print(i)
    #continue
for j in range(5):
    if j == 4:
        continue
    print(j)
    def sayHello():
        print("Hello")
    sayHello()
    def sayHello(name):
        print("hello",name)
    sayHello("sanket")
    def sayHello(name,surname):
        print("Hello " , name,surname)
    sayHello("sanket","sachdeva")
    """
    function to compute the factorial of number
    """

n = int(input("enter number"))
print("enter the number for which you want to calculate factorial", n)

cnt = 1
for fact in range(1,n+1):
    cnt = cnt * fact
    print(cnt)