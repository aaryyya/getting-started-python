# side=float(input("Enter Side here: "))
# areaofsq=side*side
# print(areaofsq)

# num1=float(input("Enter Number_1 for calculating average here: "))
# num2=float(input("Enter Number_2 for calculating average here: "))
# average=(num1+num2)/2
# print(average)


num1=int(input("Enter number1 here: "))
num2=int(input("Enter number2 here: "))
num3=int(input("Enter number3 here: "))
# var1="True"if num1>=num2 else "False"
# print(var1)
# print("Check Odd or Even")
# if(num1%2==0):
#     print("even")
# else:
#     print("odd")

print("Check which is greater n1,n2 or n3")
if(num1>=num2 and num1>=num3):
    print("num1 is greater than equal to num2 n num3")
elif(num2>=num3):
    print("num2 is greater than equal to num3")
else:
    print("num3 is greater ")
