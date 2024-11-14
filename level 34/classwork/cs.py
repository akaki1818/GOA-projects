def moutane_wyali():
    print("1. ადგე მაგიდიდან.")
    print("2. მიდი სამზარეულოში.")
    print("3. გახსენი წყლის ონკანი.")
    print("4. შეავსე ჭიქა წყლით.")
    print("5. დააბრუნე ჭიქა მაგიდასთან.")
moutane_wyali()

def check_even_odd():

    number = int(input("გთხოვთ, შეიყვანოთ რიცხვი: "))
    
    if number % 2 == 0:
        print(number, " არის ლუწი რიცხვი.")
    else:
        print(number, " არის კენტი რიცხვი.")

check_even_odd()

def greet_user():
    name = input("გთხოვთ, შეიყვანეთ თქვენი სახელი: ")
    
    print("Hello, " + name + "!")

greet_user()
