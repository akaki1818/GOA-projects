names = ["დავით", "მარიამი", "ნინო", "გიორგი", "თეა", "კატო", "ნიკოლოზი", "მალხაზ", "ელენე", "მაკო"]

filtered_names = []

for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

print(filtered_names)

numbers = []

for number in range(1, 101):
    numbers.append(number)

print(numbers)

foods = ["პიცა", "ბურგერი", "პასტა", "სუპი", "ხაჭაპური"]

cars = ["ტოიოტაო", "მერსედესი", "ბმვ", "ფორდი", "ხონდო"]

combined = foods + cars

print(combined)

ruits = ["ვაშლი", "ბანანი", "ნესვი", "ნარგილი", "გრეიპფრუტი"]


mixed = fruits + ["მარცვლეული", "რბილი", "ყავა", "ხორცი", "მაიონეზი"]

for item in mixed[:]:
    if item not in fruits:
        mixed.remove(item)

print(mixed)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("ლუწი რიცხვები:", even_numbers)
print("კენტი რიცხვები:", odd_numbers)
