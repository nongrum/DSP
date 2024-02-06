#python program for factorial
def factorial(n):
    res =1
    for i in range(2, n+1):
        res *= i
    return res 
num =4
print("the factorial of 4 is ", factorial(num))