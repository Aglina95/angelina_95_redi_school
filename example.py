name = input("What's your name? ")

course = input("Which course are you enrolled in? ")

if course.casefold() != "Intro to programming".casefold():
    print("Hi," , name.title(), "You are in the wrong classroom!!! This is ", course.title())

else:
    print("Hi, " , name.title(), "you're in the right classroom! Welcome to ", course.title())


                


#age = input("How old are you? ")
#print("My name is ", name)
#print("I am", age , "years old")
#print("You're in the right classroom")


