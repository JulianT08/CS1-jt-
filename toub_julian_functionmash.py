## This code is a large mashup that utilizes 13 functions to perform various operations. Some of the most complex functions are 'check_palindrome' and 'returns_initials'.
## The most challenging function was "replace_character'. This takes a string and a character that should be replaced with another character. I overcame
## many obstacles and pondered different ways to complete this. The code is 126 lines and full of interesting operations. 

import random #imports the random library
def chorus(): #defines the function 'chorus'
    print("Happy Birthday to you")
def verse(name): #defines the function 'verse' using the parameter of 'name'
    print(f"Happy Birthday to {name}")
def age_song(age): #defines the function 'age_song' using the parameter of 'age'
    print(f"I can't believe you are are {age}") 
def print_elements(my_list): #defines the function 'print_elements' using the parameter of 'my_list'
    for element in my_list: #prints every item in the list 'my_list'
        print(element)
def contain_element(my_list, element): #defines the function 'contain_element' using the parameters of 'my_list' and 'element'
    if element in my_list: #if the user inputs an element that is contained in the list 'my_list' the code will return True
        return True
    else: #if the user's input is not contained in the list, the code will return False
        return False
def difference(num1, num2): #defines the function 'difference' using the parameter of 'num1' and 'num2'
    print(num2-num1) #prints the difference between the entered numbers

def is_string_an_integer(string): #defines the function 'is_string_an_integer' using the parameter of 'string'
    if "-" in string: #if the character '-' is at the begining of the entered string, the number is not positive
        string = string[1:] #assigns the variable 'string' to the first character of the entered string
    if string.isnumeric(): #checks if the string is a number
        return True
    else:
        return False
def random_number_within_range(): #defines the function 'random_number_within_range'
    num1 = input("Enter number 1: ") #assigns the varible 'num1' to store the input
    num2 = input("Enter number 2 (must be greater than Number 1): ") #assigns the varible 'num2' to store the input

    if is_string_an_integer(num1) and is_string_an_integer(num2): #uses the function 'is_string_an_integer' with the inputs 'num1' and 'num2' to check if they are both integers
        print(random.randint(int(num1), int(num2))) #prints a random number between the 2
def replace_character(string, old_ch, new_ch): #defines the function 'replace_character' using the parameters of 'string', 'old_ch', and 'new_ch'
    new_string = '' #creates a blank string for the new word to become
    for ch in string: #goes through every characters in the string
        if ch == old_ch: #if the users character is found in the string, the old character will be replaced by the new one
            new_string += new_ch
        else: #if the users character is not found in any specific position, the string will add the character back to the new word
            new_string += ch
    new_string #prints the variable 'new_string'
def reverse_string(string): #defines the function 'age_song' using the parameter of 'age'
    reversed_string = string[::-1] #reverses the entered string and sets that as 'reversed_string'
    print(reversed_string)
        
def check_palindrome(string): #defines the function 'check_palindrome' using the parameter of 'string'
    reversed_string = string[::-1] #reverses the entered string and sets that as 'reversed_string'
    print(f"You entered '{string}', when reversed, the output is '{reversed_string}'") #prints the f-string
    if reversed_string == string: #if the reversed version of the string is the same as the original version the word is a palindrome
        print("Yes, this is a palindrome! \n")
    else:
        print('No, this is not a palindrome. \n')
def return_initials(string, string2): #defines the function 'return_initials' using the parameters of 'string' and 'string2'
    initial_1 = string[0] #sets the variable 'initial_1' equal to the first character in 'string'
    initial_2 = string2[0] #sets the variable 'initial_2' equal to the first character in 'string2'
    print(f" Initials = {initial_1}{initial_2}") #prints the two initials 
    
def main(): #defines the function 'main'
    
    name = input("Enter name: \n") #promts the user for a name
    age = input("Enter age: \n") #promts the user for a name
    want_song = str.lower(input("Would you like to hear a happy birthday song? \n")) #aks the user if they want to hear a song
    if 'y' in want_song: #if the user wants to hear a song the song will be played using the following functions
        chorus()
        verse(name)
        chorus()
        age_song(age)
        verse(name)
        chorus()
        age_song(age)
        print()
    age_addition = str.lower(input('Would you like to know your age in a certain number of years? ')) #asks if the user wants to see their age in a given number of years
    if 'y' in age_addition: #if the user does want to see it, their current age is added to the entered number of years
        years_input = input("In how many years would you like to know your age? ")
        print(f'In {years_input} years, you will be {int(age)+int(years_input)}!!')
    else: #if the user doesn't want to see their future age, then 'Guess not" is printed
        print('Guess not')
    books = ['','Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges'] #defines the list books 
    print()
    print_elements(books) #uses the function 'print_elements' with the parameter 'books'
    while True:
        print()
        element = str.capitalize(input("What do you want to check the list for? ")) #asks the user what they would like to check the list for
        print(contain_element(books, element)) #prints the function 'contain_element' with the parameters 'books' and 'element'
        if contain_element(books, element): #if the element is found in the list 'books' the code will break
            break
    print()
    while True:
        action = input("What would you like to do: 1. Find a difference or 2. Check if a string is an integer. ") #asks the user to pick between 2 actions
        if action == "1": #if the user picks action 1, the code will find the difference between 2 numbers
            n1 = int(input("Enter number 1: "))
            n2 = int(input("Enter number 2: "))
            difference(n1, n2)
            break
        elif action == "2": #if the user picks action 2, the code will check if an entered string is an integer
            string = input("Enter string: ")
            print (is_string_an_integer(string))
            break

    for i in range(5): #the code will print a random number within a given range 5 times, using the function 'random_number_within_range'
            print("Enter 2 numbers and I will print a random number between them (will repeat 5 times. ")
            random_number_within_range()
    print()
    print()
    string = input("Enter a string. ") #asks for a string
    old_ch = input('What character would you like to omit from the string? ') #asks what would should be omitted 
    new_ch = input("What character would you like to replace the omitted one with? ") #asks what should replace the omitted characters
    
    print(replace_character(string, old_ch, new_ch)) #prints the corrected new string
    string = input('Enter a string you would like to reverse: ') #prompts for a string
    reverse_string(string) #uses the function 'reverse_string' with the parameter 'string' to reverse what the user inputs
    print('')
    string = input("Enter a string that you would like check to see if it's a palindome: ") #prompts for a string
    check_palindrome(string) #uses the function 'check_palindrome' with the parameter 'string' to check if the input is a palindrome
    want_to_get_initials = str.lower(input("Would you like to see the initials of two words? ")) #asks if the user would like to see the initials of two words
    if 'y' in want_to_get_initials: #if the user responds with yes, the code will ask for two words and then print the initials using the functions 'return_initials'
        string = input("Enter the first word: ")
        string2 = input("Enter the second word: ")
        return_initials(string, string2) 
    else:
        print('OK')
        print()
main() #executes the main function
print("Hi there, it's Julian, I hope you enjoyed this program.")
