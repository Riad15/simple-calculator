print("------simple calculator------")
def calculator(result):
    print(f"Your result: {result}")

print(" if u want to addition then enter : 1\n if u want to subtraction then enter : 2 \n if you want to multiply then enter : 3 \n if you want to division then enter : 4 ")
a=int(input("enter a number: "))
if a==1:
    num1=int(input("first numr: "))
    num2=int(input("2nd number: "))
    sum=num1+num2
    calculator(sum)

elif a==2:
    num1 = int(input("maximum number: "))
    num2 = int(input("minimum number: "))
    sub = num1-num2
    calculator(sub)
elif a == 3:
    num1=int(input("enter first number: "))
    num2 = int(input("enter 2nd number: "))
    mul = num1 * num2
    calculator(mul)
elif a == 4:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter 2nd number:  "))
    div = num1 / num2
    calculator(div)

else:
    print("please read the carefully")

