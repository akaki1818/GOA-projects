#2) შექმენით დროში მოგზაურობის პროგრამა, რომელიც მომხმარებელს შეეკითხება მის ამჟამინდელ ასაკს, ამჟამინდელ წელს, რამდენი წლით სურს დროში მოგზაურობა, შემდეგ კი პროგრამა დაბეჭდავს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი დროში მოგზაურობის შემდეგ
year = int(input("what year it is:"))
age = int(input("enter age:"))
print("do you want to time travel ?")
anserw = input ()
if anserw == ("yes") :
    years= int(input("for how many years"))
new_date = years + year
new_age = years + age
print (new_date)
print (new_age)