# #1) დაწერე ფუნქცია, რომელიც იღებს ორი რიცხვის მნიშვნელობას input() საშუალებით და ბეჭდავს მათ ჯამს.
# def print_sum():
#     num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
#     num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
#     print("ჯამი არის:", num1 + num2)
    
# #2) დაწერე ფუნქცია, რომელიც იღებს რიცხვს input()-ით და ბეჭდავს მის კვადრატს.

# def print_square():
#     num = int(input("შეიყვანეთ რიცხვი: "))
#     print("რიცხვის კვადრატი არის:", num ** 2)

# #3) დაწერე ფუნქცია, რომელიც იღებს სახელს input()-ით და ბეჭდავს ამ სახელის სიმბოლოების რაოდენობას.

# def print_name_lenght():
#     name = input("enter ur name")
#     print("სახელის ისმბოლოების რაოდენობა არის: ", len(name))
#     # len - lenght

# #4) დაწერე ფუნქცია, რომელიც input()-ით იღებს ორ რიცხვს და ბეჭდავს, რომელია დიდი.
# def print_larger_number():
#     num1 = int(input("enter first number:"))
#     num2 = int(input("enter second number"))

#     if num > num2:
#         print("first num is bigger", num1)
#     elif num 2 > num1:
#         print("პირველი რიცხვი უფრო დიდია:", num1)
#     else:
#         print("both nums are equal")

# #5) დაწერეთ ფუნქცია რომელიც მომხმარებლისგან იღებს რიცხვს და თუ რიცხვი 1-დან 10-მდეა დაბეჭდავს თუარა დაუბეჭდავს "არასწორი რიცხვი"


    
# def check_number():
#     num = int(input("შეიყვანეთ რიცხვი: "))
#     if 1 <= num <= 10:
#         print("რიცხვი სწორია")
#     else:
#         print("არასწორი რიცხვი")

# #6) დაწერე ფუნქცია, რომელიც input()-ით იღებს ტემპერატურას ცელსიუსში და ბეჭდავს ფარენჰეიტში გადაყვანილ მნიშვნელობას.
# def celsiu_to_fahrenheit():
#     celsius = float(input("enter temprerature in celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print("temperature in fahrenheit is: ", fahrenheit)
# #7) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.

# def is_even():
#     num = int(input("enter num: "))
#     print num % 2 == 0

# #8) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ტექსტს და დააბრუნებს ტექსტის სიგრძეს.

# def text_length():
#     text = input("შეიყვანეთ ტექსტი: ")
#     return len(text)