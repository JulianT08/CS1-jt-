## Author: Julian Toub 11/30/2023
## Date: 11/30/2023
## Description: The Rock Paper Scissors game is a straightforward game that, when played against a computer, is entirely based on probability.
## Challenges: The code utilizes the random library to have the bot select a random choice (rock, paper, or scissors) from the list "rpsanswers".
## The choice is then paired against the user's choice which is stored in the variable "userrps". If the pairings result
## in the user winning, a positive message is posted and the score is updated. If the pairings result in the bot winning,
## a negative message is posted and the score is updated. If the user reaches 4 games played with less than 2 wins, they will be exited. 


import random # brings in the random library to allow for the random functions to be used
import time # brings in the time library to allow for the time functions to be used

rpsanswers = ["rock", "paper", "scissors"] # defines the list 'rpsanswers'
yourscore = 0 # sets the variable 'your score' equal to 0
user2score = 0 # sets the variable 'user2score' equal to 0 
turns = 0 # sets the variable 'turns' equal to 0

while True: # while the condition is true, keep running until a break
    if turns > 3 and yourscore <= 2: # if the user plays more than 3 games and attains a score of less than or equal to 2, the code will exit
        print('''
    -------
    WOW you're bad
    ---
    GOODBYE
    -------''') # prints this before exitting
        break # exits the code

    wantplay = str.lower(input('''
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
Want to play Rock, Paper, Scissors? You will be allowed
to play as long as your score remains above +2 after 3 turns. (btw try the special version after a
tries.)
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
''')) # prompts user for whether they want to play rps and stores their response, in lowercase, in a variable wantplay

    if 'y' in wantplay: # if the user's response to wanting to play contains a 'y', the game will start
        while True: # while the condition is true keep running until a break
            impossible = str.lower(input("Would you like to try the special version? " )) # sets the variable 'impossible' as an input and prints the text
            uservuser = str.lower(input("Would you like to play against a friend? "))# sets the variable 'uservuser' as an input and prints the text

            if 'y' in impossible and 'y' in uservuser: # if the user's responses to 'impossible' and 'uservuser' both contains a 'y' an error message is printed
                print('''
Please do not say yes to both the special version and playing against a friend
''') # prints the highlighted text
            else: # if the else and elif is voided
                break # exits the code

        
        while True: # while the condition is true keep running until a break
            userrps = str.lower(input('''
    Now pick Rock, Paper, or Scisssors '''))# sets the variable 'userrps' as an input and prints the text
            botrps = random.choice(rpsanswers) # sets the variable botrps equal to a random selection from the list 'rpsanswers'

            if userrps not in rpsanswers: # if the user's response is not contained within the list 'rpsanswers' an error message will be shown
                print("Invalid Answer") # prints the highlighted text
            elif 'y' in impossible: # if the user's response to wanting to play the impossible version contains a 'y' the loop will break
                break # exits the code
            elif 'y' in uservuser: # if the user's response to wanting to play against a friend contains a 'y' the loop will break
                user2 = str.lower(input('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    Now PLAYER 2, pick Rock, Paper, or Scisssors ''')) # sets the variable 'impossible' as an input and prints the text (\n adds a blank line)
                break # exits the code
            else: # if the if and elif is voided
                if userrps == botrps: # if the user's choice is the same as the bot's randomized choice, the game is a tie
                    print('tie') # prints the highlighted text
                else: # if the if and elif is voided
                    print('''
        I pick ''' + botrps) # prints the highlighted text
                    break # exits the code
        
        if 'y' in impossible: # if the user's response to wanting to play the impossible version contains a 'y' the code will try the following statements         
            if userrps == 'rock': # if the user selects 'rock' the bot is to play 'paper'
                botrps = 'paper' # bot plays 'paper'
            elif userrps == 'scissors': # if the user selects 'scissors' the bot is to play 'rock'
                botrps = 'rock' # bot plays 'rock'
            elif userrps == 'paper': # if the user selects 'paper' the bot is to play 'scissors'
                botrps = 'scissors' # bot plays 'scissors'

            print(f'''
You chose {userrps} and the bot chose {botrps}''') # prints the highlighted text ussing an f string. An f string utilizes variables within a print command
            print('''
        You Lose :(
        ''') # prints the highlighted text
            yourscore -=1 # decreases the variable 'your score' by 1 
            turns +=1 # increases the varibale 'turns' by 1 
            print(f'''
You chose {userrps} and the bot chose {botrps}''') # prints the highlighted text
        elif 'y' in uservuser:
            if userrps == 'rock' and user2 == 'paper': # if the user's choice is 'rock' and the second player's chioce is 'paper'...
                print('''
        You lose :( Player 2 wins''') # prints the highlighted text
                user2score +=1 # adds 1 to the variable 'user2score'
                turns +=1 # adds 1 to the variable 'turns'
            elif userrps == 'scissors' and user2 == 'rock': # if the user's choice is 'scissors' and the second player's chioce is 'rock'...
                print('''
        You lose :( Player 2 wins''') # prints the highlighted text
                user2score +=1 # adds 1 to the variable 'user2score'
                turns +=1 # adds 1 to the variable 'turns'
                
            elif userrps == 'paper' and user2 == 'scissors': # if the user's choice is 'paper' and the second player's chioce is 'scissors'...
                print('''
        You lose :( Player 2 wins''') # prints the highlighted text
                user2score +=1 # adds 1 to the variable 'user2score'
                turns +=1 # adds 1 to the variable 'turns'
            elif userrps == 'rock' and user2 == 'scissors': # if the user's choice is 'rock' and the second player's chioce is 'scissors'...
                print('''
        You Win :( Player 2 loses''') # prints the highlighted text
                yourscore +=1 # adds 1 to the variable 'yourscore'
                turns +=1 # adds 1 to the variable 'turns'
            elif userrps == 'scissors' and user2 == 'paper': # if the user's choice is 'scissors' and the second player's chioce is 'paper'...
                print('''
        You Win :( Player 2 loses''') # prints the highlighted text
                yourscore +=1 # adds 1 to the variable 'yourscore'
                turns +=1 # adds 1 to the variable 'turns'
            elif userrps == 'paper' and user2 == 'rock': # if the user's choice is 'paper' and the second player's chioce is 'rock'...
                print('''
        You Win :( Player 2 loses''') # prints the highlighted text
                yourscore +=1 # adds 1 to the variable 'yourscore'
                turns +=1 # adds 1 to the variable 'turns'
            print(f'''
You chose {userrps} and PLAYER 2 chose {user2}''') # prints the highlighted text
            
            print(f"The score is {yourscore} | {user2score}") # prints the highlighted text
        else: # if the if and elif is voided
            if userrps == 'rock' and botrps == 'paper': # if the user chooses 'rock' and the bot chooses 'paper'...
                print('''
        You Lose :(
        ''') # prints the highlighted text
                yourscore -=1 # decreases 'yourscore' by 1 indicating a loss
                turns +=1 # adds one to the varible 'turns'
            elif userrps == 'rock' and botrps == 'scissors': # if the user chooses 'rock' and the bot chooses 'scissors'...
                print('''
        You WIN :)
        ''') # prints the highlighted text
                yourscore +=1 # increases 'yourscore' by 1 indicating a win
                turns +=1 # adds one to the varible 'turns'
            elif userrps == 'scissors' and botrps == 'paper': # if the user chooses 'rock' and the bot chooses 'paper'...
                print('''
            You WIN :)
            ''') # prints the highlighted text
                yourscore +=1 # increases 'yourscore' by 1 indicating a win
                turns +=1 # adds one to the varible 'turns'
            elif userrps == 'scissors' and botrps == 'rock': # if the user chooses 'scissors' and the bot chooses 'rock'...
                print('''
            You Lose :(
            ''') # prints the highlighted text
                yourscore -=1 # decreases 'yourscore' by 1 indicating a loss
                turns +=1 # adds one to the varible 'turns'
            elif userrps == 'paper' and botrps == 'rock': # if the user chooses 'paper' and the bot chooses 'rock'...
                print('''
            You WIN :)
            ''') # prints the highlighted text
                yourscore +=1 # increases 'yourscore' by 1 indicating a win
                turns +=1 # adds one to the varible 'turns'
            elif userrps == 'paper' and botrps == 'scissors': # if the user chooses 'paper' and the bot chooses 'scissors'...
                print('''
        You Lose :(
        ''') # prints the highlighted text
                yourscore -=1 # decreases 'yourscore' by 1 indicating a loss
                turns +=1 # adds one to the varible 'turns'
            print(f'''Your score is {yourscore}
                  ''') # prints the highlighted text
    elif "no" in wantplay: # if the user's response to wanting to play again is 'no' the code will exit
        break # exits the code
    
    else: # if the if and elif is voided
        print("Invalid") # prints the highlighted text
    time.sleep(1) # uses the function time.sleep() to delay the next command
        
askprob = str.lower(input('''
Would you like to see the probability of winning, losing, or tying? ''')) # sets 'askprob' as an input and asks if the user would like to see the probability of each scenario
if 'y' in askprob: # if the user's response contains a 'y' print the following
    print('''
          -------------------------------------------
          There is a 33% probability for each outcome.
          For example, a tie between you and the computer
          is expected to happen 1/3 of the time.
          -------------------------------------------''') # prints the highlighted text





