print("Welcome to my Quiz about Baseball!")

user_answer = input("Q1: Which country has won the 2023 WBC?")

A1 = "Japan"
if user_answer == A1:
    print("Correct!")
elif user_answer == "":
    print("You should write something!")
else:
    print("Incorrect!")

user_answer = input("Q2: If pitcher threw 3 strike, is it strike out then? (Yes/No)")

A2 = "Yes"
if user_answer == A2:
    print("Correct!")
elif user_answer == "":
    print("You should write something!")
else:
    print("Incorrect!")

user_answer = input("Q3: How many players on the field in baseball?")

A3 = "9" and "9 players"
if user_answer == A3:
    print("Correct!")
elif user_answer == "":
    print("You should write something!")
else:
    print("Incorrect!")