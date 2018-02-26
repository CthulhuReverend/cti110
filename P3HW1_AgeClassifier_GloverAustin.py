#CIS110
#P3HW1 - Age Classifier
#Austin Glover
#02-26-17

#values

age = int(input("What is the age of the individual? "))


#classifications

if age <= 1:
    print("He or She is an infant.")
else:
    if age <= 12:
        print("He or She is a child.")
    else:
        if age <= 19:
            print("He or She is a teenager")
        else:
            print("He or She is an adult")
