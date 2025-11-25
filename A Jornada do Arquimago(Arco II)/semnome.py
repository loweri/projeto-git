guild_members = [
    {"name": "Kael", "class": "Mage", "level": 12},
    {"name": "Lyra", "class": "ElfArcher", "level": 10},
    {"name": "Roric", "class": "Warrior", "level": 11}
]
classes = ["mage","warrior","werebeast","werefox","elfarcher","elfpriest"]
def show_main_menu():
    print("Hello, adventurer! Welcome to the register system of the Deep Purple Staff guild!")
    selection = input(f"\nPlease, select wich option you would like to select: \n1) Register \n2) Verify \n3) Progress report \n4) Exit \nPlease enter the matching number: ").strip().lower().capitalize()
    return selection
while True:
    selection = show_main_menu()
    if selection == "4":
        print("Exiting the application, thank you and see you next!")
        break
    elif selection == "1":
        name = input(f"\nPlease, enter your name for the records: ").strip().lower().capitalize()
        print(f"\nWelcome to the guild, we are pleased to meet you {name}! \n{("-") * 30}")
        class_selected = input(f"Now, please choose your class: \n1) Mage \n2) Warrior \n3) Werebeast \n4) Werefox \n5) ElfArcher \n6) ElfPriest\nEnter the class name: ").strip().lower()
        if class_selected not in classes:
            print("Class provided not available, try again:\n")
            continue
        print(f"\nThe class is {class_selected}, and now recorded on the database!\n{("-") * 30}")
        level_selected = int(input(f"Please provide your current level for the guild records: "))
        new_member = {"name": name,"class": class_selected,"level":level_selected}
        guild_members.append(new_member)
        print(f"\nThat will be all, thank you for the informations! You are {name} currently at level {level_selected} and the class is {class_selected}! \nPlease adress to the master of the guild for new quests!\n{("-") * 40}")
    elif selection == "2":
        search = input("Please, type the name of the member you want to search:\n").strip().lower().capitalize()
        search_notfound = False
        for member in guild_members:
            if member["name"] == search:
                print(f"\nMember's name found: {member["name"]}. \nThe member's class is: {member["class"]}. \nThe current level is: {member["level"]}.\nEnd of the search! Thank you.\n{("-") * 40}")
                search_notfound = True
                break    
        if search_notfound == False:
            print(f"{("-") * 40}\nThe name provided was not found.\n{("-") * 40}")
    elif selection == "3":
        levels_list =[]
        for member in guild_members:
            current_member = member["level"]
            levels_list.append(current_member)
        level_avg = (sum(levels_list)) / (len(levels_list))
        print(f"{("-") * 40}\nTotal members: {len(levels_list)}\nStrongest member: {max(levels_list)}\nWeakest member: {min(levels_list)}\nAverage guild's level: {level_avg}\n{("-") * 40}")
    else:
        print(f"Invalid choice! Try again.\n")