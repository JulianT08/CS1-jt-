import sys
import random
import csv
from pathlib import Path
import time
def edit(websites, usernames, passwords):
    while True:
        website_selection = str.lower(input('Which website would you like to edit? (type "break" to stop)'))

        if website_selection in websites:
            index_edit = websites.index(website_selection)
            usernames[index_edit] = input(" Enter the username: ")
            passwords[index_edit] = input(" Enter the password: ")
            print(f' \n Website: "{websites[index_edit]}"      Username: "{usernames[index_edit]}"       Password: "{passwords[index_edit]}" \n')
            break
        elif website_selection == 'break':
            break
        else:
            print(f'The website entered is not found in the list, here are the available sites: {websites}')
def add(websites, usernames, passwords):
    while True:
        print()
        website = input("Add a website (type 'stop' to continue without adding): ") #asks the user for a website or to view the list of sites
        if website == 'list':
            for i in range(len(websites)):
                print(f' \n Website: "{websites[i]}"      Username: "{usernames[i]}"       Password: "{passwords[i]}" \n')
        elif website == 'stop':
            break
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        websites.append(website)
        usernames.append(username)
        passwords.append(password)
        break
def end():
    sys.exit()
def main():
    websites = [] #creates an empty list named 'websites'
    usernames = [] #creates an empty list named 'usernames'
    passwords = [] #creates an empty list named 'passwords'
    add(websites, usernames, passwords)
    print()
    while True:
        mode = input('''What would you like to do? 
        1. Add a site
        2. Edit a site
        3. Print a site
        4. Print the list
        5. Generate a secure password
        6. Export list to excel
        7. End the program
        
        ''')
        if mode == '1':
            add(websites, usernames, passwords)
            print()
            time.sleep(1)
        elif mode == '2':
            edit(websites, usernames, passwords)
            print()
            time.sleep(1)
        elif mode == '3':
            while True:
                user_search = str.lower(input("Which website would you like to search for? "))
                if user_search in websites:
                    index = websites.index(user_search)
                    print(f' \n Website: "{websites[index]}"      Username: "{usernames[index]}"       Password: "{passwords[index]}" \n')
                    break
                else:
                    print('Website is not in list. ')
                    ask_for_website = str.lower(input("What website would you like to find the info for? "))
            print()
            time.sleep(1)
        elif mode == '4':
            for i in range(len(websites)):
                print(f' \n Website: "{websites[i]}"      Username: "{usernames[i]}"       Password: "{passwords[i]}" \n')
                print()
            time.sleep(1)
        elif mode == '5':
            alphabet_lower = list('abcdefghijklmnopqrstuvwxyz')
            alphabet_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            special_characters = list('!@#$%&*()?><:{}|+')
            numbers = list('1234567890')

            pwd = random.choice(alphabet_lower) + random.choice(alphabet_upper) + random.choice(special_characters)+ random.choice(numbers) + random.choice(alphabet_upper) + random.choice(special_characters) + random.choice(numbers)

            print(f'Your specially generated, secure, password is...    {pwd}')
            time.sleep(1)

        elif mode == '6':
            columns = {}
            columns['websites'] = websites
            columns['usernames'] = usernames
            columns['passwords'] = passwords
            rows = zip(columns['websites'],columns['usernames'],columns['passwords'])

            with open('PasswordKeeper.csv','w',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Websites:', 'Usernames:', 'Passwords:' ])
                writer.writerows(rows)
            folder = (Path.cwd())

            print(f'''
            
            Data successfully stored in the same folder as the project.
            
            The folder is {folder}
            ''')
            time.sleep(1)
        elif mode == '7':
            end()
        else:
            print("Please enter a number 1, 2, 3, 4, 5, based on what command you would like to execute. ")
            print()

main()