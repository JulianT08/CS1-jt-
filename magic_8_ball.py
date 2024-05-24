## This code uses the random and time libraries to create a Magic 8-Ball that supplies answers to the user's most desired questions. This is done through
## picking a random choice from the list, "answer". If the user is unsatisfied with the answer, they can enter "This is terrible".
## This will restart the program to a specified point. If the user's response is anything but terrible, then the program will stop. 


import random # imports the random library.
import time # imports the time library.

while True: #infinite loop (while condition True is true)
    print('''Welcome to the Magic 8-Ball!
             ----------------------------''') # prints the welcome sign.
    print('''Directions: I will first ask you to pose a question to the powerful Magic 8-Ball.
            Once that is complete you will toss the ball at least 50 feet into the air.
            Once you catch the ball a magical guiding answer will appear.
            There in lies the power of the Magic 8-Ball. (Example: Will I get an A in Computer Science?
            ''') # prints the directions
    
    question = str.lower(input("Ask me a question -->  ")) # prompts the user to ask a question and stores it, in lowercase, in the variable question.
    if question == "stop": #if the user enters stop
        break # then end the loop. 
    answer = ["Yes", "No", "That's a tough one", "Up to you, my friend", "Of courseeee", "Well yes of course", "U wish!"] # defines the list "answer" with the acceptable list of responses. 
    time.sleep(1) # delays the next command by 1 second. 
    print('''
    Now toss me into the air (50 - 100 ft for best results)

    <><><><><><><><><><><><><><><><><><><><><><><><><><><>
    ''') # prints the text.
    print('''Here it comes!!!!
And the answer is.....
''') # prints the text.
    time.sleep(2) # delays the next command by 2 second.
    response = random.choice(answer) # sets the variable "response" equal to a random choice from the list, "answer".
    print(response) # prints the variable. (ex. "That's a tough one")
    print('''
I hope you are satisfied with your answer. If not, please type "This is terrible"''') # prints the text.
    terrible = str.lower(input("What do you think? -->   ")) # sets "terrible" as an input and prints the highlighted part.
    time.sleep(1) # delays the next command by 1 second.

    if "terrible" in terrible: # if the term "terrible is contained in the input, "terrible" the following will be printed. 
        print(''' TOO BAD
Sorry I tried my best but we can go again, just give me a second''') # prints the text.
        time.sleep(3) # delays the next command by 3 second.
    else: # otherwise:
        try: # tries the following:
            terrible = int(terrible) # sets the varibale "terrible" as an integer. 
            print("Invalid syntax, but quitting the program") # prints the text.
            break # stop the code
        except ValueError: # if the user's response does not meet the criteria:
            break # stop the code
