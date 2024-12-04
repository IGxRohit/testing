print("कौन बनेगा हजारपति Season 1")
user=str(input("ENTER PLAYER NAME:"))
money=0
Q1=str(input("Q.1 How many days are there in a week? \noptions are \n A.  4 days \n B.  6 days\n C.  7 days\n D.  9 days \n Your Answer:-"))
if Q1.upper()=="C":
    money=money+100
    print("Your option is Right 7 days                                          ",money,"Rupees")
elif Q1=="A" or Q1=="B" or Q1=="D":
    print("You loose  :__ ",money,"rupees")
else:
    print("you pressed wrong key so you loose tis game",money,"rupees")
    


# question 2nd



Q2=str(input("Q.2 Rainbow consist of how many colours? \noptions are \n A.  4 color \n B.  6 color\n C.  7 color\n D.  9 color \n Your Answer:-"))
if Q2.upper()=="C":
    money=money+200
    print("Your option is Right 7 color                                         ",money,"rupees")
elif Q2=="A" or Q2=="B" or Q2=="D":
    print("You loose  :__ ",money,"rupees")
else:
    print("you pressed wrong key so you loose tis game",money,"rupees")


    #QUESTION #3RD
Q3=str(input("Q.3  How many hours are there in a day?\noptions are \n A.  43 HOURS \n B.  6 HOURS\n C.  7 HOURS\n D.  24 HOURS \n Your Answer:-"))
if Q3.upper()=="D":
    money=money+300
    print("Your option is Right 24 HOURS                                        ",money,"rupees")
elif Q3=="A" or Q3=="B" or Q3=="C":
    print("You loose  :__ ",money,"rupees")
else:
    print("you pressed wrong key so you loose tis game",money,"rupees")



    # 4TH QUESTION
Q4=str(input("Q.4 How many minutes are there in an hour? \noptions are \n A.  60 MINUTES \n B.  63 MINUTES\n C.  69 MINUTES\n D.  9 MINUTES \n Your Answer:-"))
if Q4.upper()=="A"or"a":
    money=money+400
    print("Your option is Right 60 MINUTES                                         ",money,"rupees")
elif Q4=="C" or Q4=="B" or Q4=="D":
    print("You loose  :__ ",money,"rupees")
else:
    print("you pressed wrong key so you loose tis game",money,"rupees")

print("बधाई हो,",user,"आप इतनी  RS ",money,"राशि जीत चुके हैं")





# print("कौन बनेगा हजारपति Season 1")  # Prints the game title

# user = str(input("ENTER PLAYER NAME: "))  # Gets the player's name and stores it in the 'user' variable

# money = 0  # Sets the initial money to 0

# questions = [  # Creates a list of questions and their details
#     {
#         "question": "Q.1 How many days are there in a week?",
#         "options": ["A.  4 days", "B.  6 days", "C.  7 days", "D.  9 days"],
#         "answer": "C"
#     },
#     {
#         "question": "Q.2 Rainbow consist of how many colours?",
#         "options": ["A.  4 color", "B.  6 color", "C.  7 color", "D.  9 color"],
#         "answer": "C"
#     },
#     # Add more questions here
# ]

# for i, question in enumerate(questions):  # Loops through each question in the 'questions' list
#     print(question["question"])  # Prints the question
#     for option in question["options"]:  # Loops through the options for the current question
#         print(option)  # Prints each option
#     while True:  # Starts a loop that continues until a valid answer is given
#         answer = input("Your Answer: ").upper()  # Gets the user's answer and converts it to uppercase
#         if answer in ["A", "B", "C", "D"]:  # Checks if the answer is one of the valid options (A, B, C, D)
#             break  # If the answer is valid, exits the loop
#         else:
#             print("Invalid answer. Please choose A, B, C, or D.")  # Prompts the user to enter a valid option
#     if answer == question["answer"]:  # Checks if the user's answer matches the correct answer
#         money += 100 * (i + 1)  # Adds the corresponding amount of money to the player's total
#         print("Your option is Right! You have earned", money, "Rupees.")  # Prints a message indicating a correct answer
#     else:
#         print("You loose  :__ ", money, "rupees")  # Prints a message indicating an incorrect answer
#         break  # Exits the loop if the player answers incorrectly

# print("बधाई हो,", user, "आप इतनी  RS ", money, "राशि जीत चुके हैं")  # Prints a final message with the player's winnings