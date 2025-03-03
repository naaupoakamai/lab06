from time import sleep
from math import sqrt 

def root_after(num1,num2):
    sleep(num2/1000)
    sqrt_value=sqrt(num1)
    print(f'Square root of {num1} after {num2} miliseconds is {sqrt_value}')

num1=int(input(''))
num2=int(input(''))
root_after(num1,num2)