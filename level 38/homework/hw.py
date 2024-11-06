print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")
option = int(input("Choose an option"))
if (option  in [1,2,3,4]):
    num1 =int(input("choose first number"))
    num2 =int(input("choose first number"))
else:
    print("ERROR")
if option == 1:
    result = num1 + num2
elif option == 2:
     result = num1 - num2
elif option == 3:
    result = num1 * num2
elif option == 4:
    result = num1 // num2

print(result)

