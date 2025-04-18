
name = input("Whats your name? ")
age = int(input("How old are you? "))
if age < 18:
    print("sorry, you must be 18 years old to take this survey.")
else:
    location = input("Where do you live in this World? ")
    funThings = input("Why do you like coding? ")


    hours = int(input("How many hours do you code per week? "))
    if hours == 0:
        print("Thats okay! you don't need to code for this survey.")
    else:
        projects = input("Would you like to learn web, AI, or cyber? ")

        print("Thanks " + name + "! You are " + str(age) + " years old. You live in " + location + ". You like to code because " + funThings + ". You spend " + str(hours) + " hours coding per week. You would like to learn " + projects + ".")