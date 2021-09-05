# Built-In Imports
import time, random, sys, os

from typing import Callable, Dict
from collections import Counter
from replit import db


black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"


st = 0
def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(st)
  print()



yes = ['YES', 'yes', 'Yes', 'y', 'Y']
no = ['NO', 'no', 'No', 'n', 'N'] 
all_choices = ['NO', 'no', 'No', 'n', 'N', 'YES', 'yes', 'Yes', 'y', 'Y']

# <-- Jobs -->
all_jobs = ['cosplayer', 'youtuber', 'manager', 'fastfoodcook', 'housewife', 'internettroll', 'teacher']
current_job = []



class Game:

    def __init__(self) -> None:
        self.deposit_allowed = 500
        self.deposited = 0
        self.working = False
        self.inventory = []
        self.money = 300000
        

    def play(self) -> None:
        commands = self.get_commands()

        while True:
            command = input(f"{bright_green}Command (type [help] to see list of all commands):\n>> ")

            if command not in commands:
                print(f'\n{red}Wrong input!\n')
                continue

            if command == 'work' and self.working == False:
                print(red + "You don't  have any job.  How will you work? Such a idiot")

            commands[command]()

    def get_commands(self) -> Dict[str, Callable[[], None]]:
        return {
            'help': self.rules,
            'job':self.job_funtion,
            'joblist': self.joblist_function,
            'jobresign': self.job_resign,
            'deposit': self._deposit_money,
            'dep': self.dep_money,
            'balance': self.display_balance,
            'bal': self.display_balance,
            'withdraw': self.withdraw_money,
            'with': self.withdraw_money,
            'work': self.work,
            'shop': self.shop,
            'beg': self.beg,
            'buy': self.buy,
            'inv': self.inventory_display,
            'inventory': self.inventory_display,
            'sell': self.sell,
            'hunt': self.hunt
            
        }

    def login(self): # making the login system
     # the  thing
        print("Do you want to log-in, sign-up or play as guest (Money won't be saved if you play as a Guest):")
        account_choice = input("[1] Login\n[2] Sign Up\n[3] Guest\n>>> ")

        if account_choice == "1":
            
            print("Login\n")
            user = input("Username: ")
            passcode = input("Password: ")
            try:
                Password = db[user]

                if Password == passcode:
                    
                    print(green+"Logged in!"+white)
                    time.sleep(2) # waiting 2 seconds
                    

                else:
                    
                    print(red+"Incorrect!"+white)
                    time.sleep(2)
                    self.login()

            except:
                
                print(red+"That username is not included!"+white)
                time.sleep(2)
                self.login()

        elif account_choice == "2":
            
            print("Sign up\n")
            newuser = input("Username: ")
            newpasscode = input("Password: ")

            try:
                db[newuser] = newpasscode
                
                print(green+"Account made!"+white)
                time.sleep(2)
                
                self.login()
            
            except:
                
                print(red+"Account already made!"+white)
                time.sleep(2)
                
                self.login()

        elif account_choice == "3":
            
            print(red+"Playing as a Guest"+white)
            time.sleep(2)
            

        else:
            
            print(red+"Invalid Command!"+white)
            time.sleep(2)
            
            self.login()

    def rules(self):
        print(f"""
        {blue}\nHere are the commands you can use:
        To see the list of commands, type [help]
        {bright_green}Work/Job:
        \t{bright_blue}See all Jobs, {yellow}Command: [joblist],
        \t{bright_blue}Get a job, {yellow}Command: [job],
        \t{bright_blue}Resign from job, {yellow}Command: [jobresign]
        \t{bright_blue}Work on the job, {yellow}Command: [work],
        {bright_green}Money:
        \t{bright_blue}Check your balance, {yellow}Command: ['bal' or 'balance'],
        \t{bright_blue}Deposit money in the bank, {yellow}Command: [dep or deposit],
        \t{bright_blue}Withdraw money from the bank, {yellow}Command: [with or withdraw],
        \t{bright_blue}Beg, {yellow}Command: [beg],
        \t{bright_blue}Inventory, {yellow}Command: [inv or inventory],
        {bright_green}Shopping/Buying:
        \t{bright_blue}See the shop, {yellow}Command: [shop],
        \t{bright_blue}Buy Item,  {yellow}Command: [buy],
        \t{bright_blue}Sell Item,  {yellow}Command: [sell],
        {bright_green}Shopping/Buying:
        \t{bright_blue}Hunt, {yellow}Command: [hunt], (Unlocks with buying a rifle)
        \t{bright_blue}Fish, {yellow}Command: [fish], (Unlocks with buying a rod)
        \t{bright_blue}Multiplies your money, {yellow}Command: [multiply], (Unlocks with buying a multiplier)
        """)

    def joblist_function(self):
        time.sleep(0.5)
        os.system('clear')
        print(f"""
        {bright_red}Here are the list of jobs:
        ■ Cosplayer,        ■ YouTuber,
        ■ Manager,          ■ Fast Food Cook,
        ■ House Wife,       ■ Internet Troll,
                    ■ Teacher
        
        """)
    
    def job_funtion(self):
        time.sleep(0.5)
        os.system('clear')
        global working
        global current_job
        

        while self.working == False:
            job_select = input(f"\n{magenta}What job do you want to work as? [Enter the job name in lowercase and without spaces]\n> ")
            while job_select in all_jobs:
                if job_select in all_jobs and self.working == False:
                    print(f"\n{green}You are working as a {job_select.title()}\n")
                    current_job.append(f"{job_select.title()}")
                    self.working = True
                    break
                    
            else:
                print(f"{red}\nOIII, there is no job like that...\n")

    def job_resign(self):
        time.sleep(0.5)
        os.system('clear')
        global current_job

        if len(current_job) == 0:
            print(f"{red}\nLOL, you don't even have a job. What are you resigning from?\n")

        if len(current_job) == 1:
            print("\nYou have resigned from your job. Congrats on being jobless... \n")
            current_job.pop()
            self.working = False

    def _deposit_money(self) -> None:
        if self.deposit_allowed == self.deposited:
            print("You have a full bank kiddo...")
            return

        self.dep_money()

    def dep_money(self):


        try:
            money_to_dep = int(input(f"{bright_blue}\nHow much money do you want to deposit?(enter amount ONLY):\n>> "))
            while money_to_dep <= self.deposit_allowed - self.deposited:
                self.money -= money_to_dep
                self.deposited += money_to_dep

                break
            if money_to_dep > self.deposit_allowed:
                print(f"{red}\n Number too high.\n")
        except:
            print(f"{red}\nOIIIIII, Wrong INPUT. Try again.\n")   

    def display_balance(self):
        while True:
            print(f"{bright_blue}\nWallet: ⏣ {self.money}\nBank: {self.deposited}/{self.deposit_allowed}\n") 
            break 

    def withdraw_money(self):

        if self.deposited == 0:
            print(f"{red}\nYou don't have any money in your bank. You withdrawing air?\n")

        if self.deposited != 0: 
            try:
                money_to_with = int(input(f"{bright_blue}\nHow much money do you want to withdraw?(enter amount ONLY):\n>> "))
                while money_to_with <= self.deposited:
                    self.money += money_to_with
                    self.deposited -= money_to_with
                    break

                if money_to_with > self.deposited:
                    print(f"{red}\nNumber too high.Your too poor\n")


            except:
                print(f"{red}\nOIIIIII, Wrong INPUT. Try again.\n")                                                                             

    def work(self):
        
        time.sleep(0.5)
        os.system('clear')
        words = ['ritzy', 'cool', 'unique', 'calendar', 'sweater', 'ancient', 'open', 'wave', 'blush', 'gold', 'nod', 'racial']

        while self.working:
            random_choice = random.choice([1, 2, 3, 4, 5, 6, 7])

            while True:
                random_word = random.choice(words)
                break

            if random_choice == 1:
                print(f"{bright_yellow}Write down the word that will appear on the screen for a second(it will be hard to see):")
                time.sleep(4)
                print(f"\n{black}{random_word}\n")
                time.sleep(1)
                os.system('clear')
                work1 = input(f"{green}\nWhat was the word?\n> ")


                if work1 == random_word:
                    print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
                    self.money += 15000
                    break
                if work1 != random_word:
                    print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 69 for this hour of work.\n")
                    self.money += 69
                    break

            if random_choice == 2:
                highlow_number = random.choice(range(2, 101))
                number_guess = random.choice(range(2, 101))
                
                highlow_user = input(f"I have guessed a number. Is {number_guess} high or low from that number(high/low).\n>> ")
                if highlow_user == 'high' or highlow_number == 'HIGH' or highlow_number == 'High':
                    if number_guess > highlow_number:
                        print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
                        self.money += 15000
                        print(highlow_number)
                        break
                    if number_guess < highlow_number:
                        print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 0 for this hour of work.\n")
                        self.money += 0
                        print(highlow_number)
                        break

                if highlow_user == 'low' or highlow_number == 'LOW' or highlow_number == 'Low':
                    if number_guess < highlow_number:
                        print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
                        self.money += 15000
                        print(highlow_number)
                        break
                    if number_guess > highlow_number:
                        print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 0 for this hour of work.\n")
                        self.money += 0
                        print(highlow_number)
                        break
                    
            if random_choice == 3:
                with open('sentences.txt', 'r') as sentences:
                    sentence = [line.strip() for line in sentences.readlines()]


                random_sentence = random.choice(sentence)

                user_type = input(f"{bright_cyan}Write down the following sentence:\n\n{random_sentence}\n\n>> ")

                if user_type == random_sentence:
                    print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
                    self.money += 15000
                    break
                
                if user_type != random_sentence:
                    print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 0 for this hour of work.\n")
                    self.money += 0
                    break

            if random_choice == 4 or random_choice == 5 or random_choice == 6 or random_choice == 7:
                print(f"{red}\nYou can't work right now.\n")
                break

    def shop(self):
        print(f"""
        {blue}\nHere are the commands you can use:
        To see the list of commands, type [help]
        {bright_blue}{red}︻デ═一{bright_blue}Hunting Rifle, {yellow}ID: [rifle], {magenta}Command unlocked: [hunt], {cyan}Price: ⏣ 15,000
            \t\t{white}Use rifle to hunt and sell what you find.
        \t{bright_blue}🎣  Fishing Rod, {yellow}ID: [rod], {magenta}Command unlocked: [fish], {cyan}Price: ⏣ 15,000
            \t\t{white}Use rod to hunt and sell what you find.
        \t{bright_blue}   Multiplier, {yellow}ID: [multiplier], {magenta}Command unlocked: [multiply], {cyan}Price: ⏣ 35,000
            \t{white}Mulitplies the amount of money you have by 5%
        \t{bright_blue}❤️  Life Saver, {yellow}ID: [life], {cyan}Price: ⏣ 25,000
            \t{white}Saves your life if you die trying to rob someone.
        """)

    def beg(self):
        random_number2 = random.choice([0, 1, 2])
        random_money = random.choice(range(1, 100))

        if random_number2 == 1 or random_number2 == 0:
            print(f"{red}\nEwwww beggar. No stonks for u\n")
        
        if random_number2 == 2:
            print(f"{green}\nMr.beggar, you can have ⏣ {random_money}.\n")
            self.money += random_money
    
    def buy(self):  
        bought_stuff = {
            'rifle': self.inventory.append,
            'rod': self.inventory.append,
            'multiplier': self.inventory.append,
            'life': self.inventory.append
        }

        pricing = {
            'rifle': 15000,
            'rod': 15000,
            'multiplier': 35000,
            'life': 25000
        }

        buying_choice = input(f"{yellow}\nWhat do you want to buy?(Enter the ID)(to see ID's type 'shop' in commands):\n>> ")

        if buying_choice not in bought_stuff:
            print(f'\n{red}That item is not in the shop. Enter something you can buy!!!\n')

        if buying_choice in bought_stuff:
            object_price = pricing[buying_choice]
            if self.money >= object_price:
                self.money -= object_price 
                bought_stuff[buying_choice](buying_choice)
                
                print(f"{green}\nYou have succesfully bought the item.\n")

            else:
                print(f"\n{red}You don't have enough money in your wallet. Sorry\n")

    def inventory_display(self):
        if len(self.inventory) == 0:
            print(f"\n{red}You don't have anything in your inventory.\n") 

        if len(self.inventory) > 0:
            count_dict = Counter(self.inventory)

            print(f"{bright_blue}\nHere is your inventory: ")
            for key, value in count_dict.items():
                print(f"\t{bright_yellow}{value} {key}  (s)\n")

    def sell(self):
        sell_price = {
            'rifle': 9000,
            'rod': 9000,
            'multiplier': 20000,
            'life': 10000,
            'deer': 650,
            'boar': 900,
        }
        selling_choice = input(f"{magenta}\nWhat would you like to sell?(Enter ID)\n> ")

        while selling_choice in self.inventory:
            print(f"{green}You have sold 1 {selling_choice.title()} for {sell_price[selling_choice]}. ")
            self.inventory.remove(selling_choice)
            self.money += sell_price[selling_choice]
            break 

    def hunt(self):
        random_number = random.choice([0, 1, 2, 3])
        things = ["deer 🦌", "boar 🐗", "skunk 🦨", "banknote 💵"]
        sel_thing = random.choice(things)

        if random_number in range(2):
            print(f"\n{blue}You can't hunt right now, the woods are empty.")
        print(f"{bright_green} You went into the woods and brought a {sel_thing}. The id of the item is just its name, i.e deer.")
        self.inventory.append(sel_thing)

    