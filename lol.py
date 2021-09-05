import time
import random
import sys
import os


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

allowed_commands = ['help', 'joblist', 'job', 'jobresign', 'work', 'bal', 'balance', 'dep', 'deposit', 'with', 'withdraw', 'fish', 'hunt', 'shop', 'buy', 'sell', 'hunt', 'fish', 'multiply']


all_jobs = ['cosplayer', 'youtuber', 'manager', 'fastfoodcook', 'housewife', 'internettroll', 'teacher']
current_job = []
working = False

money = 500
deposit_allowed = 100
deposited = 0

def rules():
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
        {red} Note: More commands will unlock once you start buying things.
        """)
    
def gamePlay():
    while True:
        command = input(f"{bright_green}Command (type [help] to see list of all commands):\n>> ")
        while command in allowed_commands:
            if command == 'help':
                rules()
                break

            elif command == 'joblist':
                joblist_function()
                break

            elif command == 'job' and working == False:
                job_funtion()
                break

            elif command == 'job' and working == True:
                print(f"\n{red}You are already doing a job. You can't work on two jobs,that is dumb...\n")
                break

            elif command == 'jobresign':
                job_resign()
                break

            elif command == 'work' and working == True:
                work()
                break
            
            elif command == "work" and working == False:
                print(f"{red}\nLOL, you don't have a job, how you gonna work?\n")
                break

            elif command == 'dep' or command == 'deposit' and deposit_allowed != deposited:
                dep_money()
                break

            elif command == 'dep' or command == 'deposit' and deposit_allowed == deposited:
                print("You have a full bank kiddo...")
                break

            elif command == 'bal' or command == 'balance':
                display_balance()
                break

            elif command == 'with' or command == 'withdraw' and deposited != 0:
                withdraw_money()
                break
            
            elif command == 'with' or command == 'withdraw' and deposited == 0:
                print(f"{red}\nNo money deposited. What are you even trying to wothdraw LOL?\n")
                break

            elif command == 'shop':
                shop()
                break

            elif command == 'beg':
                beg()
                break


def dep_money():
    global money
    global deposit_allowed
    global deposited

    try:
        money_to_dep = int(input(f"{bright_blue}\nHow much money do you want to deposit?(enter amount ONLY):\n>> "))
        while money_to_dep <= deposit_allowed - deposited:
            money -= money_to_dep
            deposited += money_to_dep
            break
        if money_to_dep > deposit_allowed:
            print(f"{red}\n Number too high.\n")
    except:
        print(f"{red}\nOIIIIII, Wrong INPUT. Try again.\n")       


def display_balance():
    while True:
        global money
        global deposit_allowed
        global deposited
        print(f"{bright_magenta}\nWallet: ⏣ {money}\nBank: {deposited}/{deposit_allowed}\n") 
        break 


def withdraw_money():
    global money
    global deposit_allowed
    global deposited

    try:
        money_to_with = int(input(f"{bright_blue}\nHow much money do you want to withdraw?(enter amount ONLY):\n>> "))
        while money_to_with <= deposited:
            money += money_to_with
            deposited -= money_to_with
            break

        if money_to_with > deposited:
            print(f"{red}\nNumber too high.\n")

    except:
        print(f"{red}\nOIIIIII, Wrong INPUT. Try again.\n")  


def joblist_function():
    time.sleep(0.5)
    os.system('clear')
    print(f"""
    {bright_red}Here are the list of jobs:
    ■ Cosplayer,        ■ YouTuber,
    ■ Manager,          ■ Fast Food Cook,
    ■ House Wife,       ■ Internet Troll,
                ■ Teacher
    
    """)


def job_funtion():
    time.sleep(0.5)
    os.system('clear')
    global working
    global current_job
    

    while working == False:
        job_select = input(f"\n{magenta}What job do you want to work as? [Enter the job name in lowercase and without spaces]\n> ")
        while job_select in all_jobs:
            if job_select in all_jobs and working == False:
                print(f"\n{green}You are working as a {job_select.title()}\n")
                current_job.append(f"{job_select.title()}")
                working = True
                break
                   
        else:
            print(f"{red}\nOIII, there is no job like that...\n")

            
def job_resign():
    time.sleep(0.5)
    os.system('clear')
    global current_job

    if len(current_job) == 0:
        print(f"{red}\nLOL, you don't even have a job. What are you resigning from?\n")

    if len(current_job) == 1:
        print("\nYou have resigned from your job. Congrats on being jobless... \n")
        current_job.pop()


def work():
    global money
    time.sleep(0.5)
    os.system('clear')
    words = ['ritzy', 'cool', 'unique', 'calendar', 'sweater', 'ancient', 'open', 'wave', 'blush', 'gold', 'nod', 'racial']

    random_choice = random.choice([1, 2, 3, 4, 5, 6, 7])
    if random_choice == 1:
        random_word = random.choice(words)
        print(f"{bright_yellow}Write down the word that will appear on the screen for half a second(it will be hard to see):")
        time.sleep(4)
        print(f"\n{black}{random_word}\n")
        time.sleep(0.5)
        os.system('clear')
        work1 = input(f"{green}\nWhat was the word?\n> ")


        if work1 == random_word:
            print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
            money += 15000
        if work1 != random_word:
            print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 3,000 for this hour of work.\n")
            money += 3000
        

    if random_choice == 2:
        highlow_number = random.choice(range(2, 101))
        number_guess = random.choice(range(2, 101))
        
        highlow_user = input(f"I have guessed a number. Is {number_guess} high or low from that number(high/low).\n>> ")
        if highlow_user == 'high' or highlow_number == 'HIGH' or highlow_number == 'High':
            if number_guess > highlow_number:
                print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
                money += 15000
            if number_guess < highlow_number:
                print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 3,000 for this hour of work.\n")
                money += 3000

        if highlow_user == 'low' or highlow_number == 'LOW' or highlow_number == 'Low':
            if number_guess < highlow_number:
                print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
                money += 15000
            if number_guess > highlow_number:
                print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 3,000 for this hour of work.\n")
                money += 3000
            
    if random_choice == 3:
        sentences_list = [
            "The memory we used to share is no longer coherent.",
            "Bill ran from the giraffe toward the dolphin.",
            "She was the type of girl who wanted to live in a pink house.",
            "The door slammed on the watermelon.",
            "It's a skateboarding penguin with a sunhat!",
            "He excelled at firing people nicely.",
            "He always wore his sunglasses at night.",
            "Mothers spend months of their lives waiting on their children.",
            "He decided to live his life by the big beats manifesto.",
            "People keep telling me 'orange' but I still prefer 'pink'."
        ]

        random_sentence = random.choice(sentences_list)

        user_type = input(f"{bright_cyan}Write down the following sentence:\n\n{random_sentence}\n\n>> ")

        if user_type == random_sentence:
            print(f"{green}\nBOSS: Great work. I am going to give you ⏣ 15,000 for this hour of work.\n")
            money += 15000
        
        if user_type != random_sentence:
            print(f"{red}BOSS: Terrible effort. I am going to give you ⏣ 3,000 for this hour of work.\n")
            money += 3000

    if random_choice == 4 or random_choice == 5 or random_choice == 6 or random_choice == 7:
        print(f"{red}\nYou can't work right now.\n")

    
def shop():
    print(f"""
    {blue}\nHere are the commands you can use:
    To see the list of commands, type [help]
    {bright_green}Work/Job:
    \t{bright_blue}︻デ═一 Hunting Rifle, {yellow}Code to buy: [huntingrifle], {magenta}Command to use: [hunt], {cyan}Price: ⏣ 15,000
        \t{white}Use rifle to hunt and sell what you find.
    \t{bright_blue}Fishing Rod, {yellow}Code to buy: [fishingrod], {magenta}Command to use: [fish], {cyan}Price: ⏣ 15,000
        \t{white}Use rod to hunt and sell what you find.
    \t{bright_blue}Multiplier, {yellow}Code to buy: [multiplier], {magenta}Command to use: [multiply], {cyan}Price: ⏣ 35,000
        \t{white}Mulitplies the amount of money you have by 5%
    \t{bright_blue}Life Saver, {yellow}Code to buy: [lifesaver], {cyan}Price: ⏣ 25,000
        \t{white}Saves your life if you die trying to rob someone.
    """)


def beg():
    global money
    random_number2 = random.choice([0, 1, 2])
    random_money = random.choice(range(100, 500))

    if random_number2 == 1:
        print("Ewwww beggar. No stonks for u")
    
    if random_number2 == 2:
        print(f"Mr.beggar, you can have ⏣ {random_money}.")
        money += random_money