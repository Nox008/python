""" print("hello world")
age = 12
marks = 90.5
name = "sam"
isPassed = True
print(name, age, marks, isPassed) """     #python variable declarations

""" for i in range(5):
    print(i)

age=17
if(age>=18):
    print("adult")
else:
    print("go back to school") """     #python for loops and if statements

""" def greet(name):
    print("hello", name)

greet("Anox") """                     #simple python function

#simple python calculator
num1 = int(input("Enter a Number:"))
num2 = int(input("Enter another number:"))
print("1.Add")
print("2.Substract")
print("3.Mulitply")
print("4.Divide")
choice = int(input("Enter Your Choice:"))
match choice: #match(choice) also works somehow
    case 1: 
        print("Two numbers added is:", num1+num2)
    case 2:
        print("Two numbers subtracted is:", num1-num2)
    case 3:
        print("Two numbers multiplied is:", num1*num2)
    case 4:
        print("Two numbers divided is:", num1/num2)
    case _:
        print("Choice invalid!!!")