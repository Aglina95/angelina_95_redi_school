name = "Angelina"
age = 31
city = "Copenhagen"
language = ["Greek", "English"]
is_student = True
languagelist = " and ".join(language)

#print variables
print("Your name is", name)
print("Your name's length is" , len(name))
print("You are" , age, "years old")
print("You live in ", city)
print("You speak", languagelist)

if is_student == True:
    print("You are currently a student")

#check types with type()
print(type(name))
print(type(age))
print(type(city))
print(type(language))
print(type(is_student))