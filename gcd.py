#this code will help us calculate the great common divisor of two numbers

#this code uses while loop
'''num1 = int(input('What is the first numer?: '))
num2 = int(input('What is the second number?: '))
i = 1

#the code here will loop through all numbers that are less than num1 and num2 to see the common divisor in both numbers
while i <=num1 and i <= num2:
    if num1%i ==0 and num2%i==0:
        gcd=i
    i = i+1

print('GCD IS:', gcd)'''

# the code above is also possible possible. However, this one down here below is also possible

div=[]
N1= int(input('Enter number1: '))
N2 = int(input('Enter number2: '))
for i in range(1, N1+1) and range(1,N2+1):
    if N1%i==0 and N2%i==0:
        div.append(i)

print(div[-1])