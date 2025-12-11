#The guild's management - Mage's Guild
roster_guild = []
def i_main_menu():
    addmember = print("1. Subscribe to the guild")
    checkmember = print("2. Member List")
    exit = print("3. Exit.")
def require_level():
    while True:
        try:
            add_level = int(input("Your current level: "))
            break
        except ValueError:
            print("Only numbers are accepted, try again")
    return add_level
print("Welcome, adventurer!\n" \
"You are at the HellFire Mage's Guild.\n" \
"Bellow you'll find all the options available!")
while True:
    i_main_menu()
    selection = int(input("Please, choose an option: "))
    if selection == 1:
        add_member = input("Please, enter your name to the guild: ")
        add_lvl = require_level()
        advclass = input("Your Class: ").strip().lower().capitalize()
        listofguildmember = {
        "Name": add_member,
        "Level": add_lvl,
        "Class": advclass
}
        roster_guild.append(listofguildmember)
        print(roster_guild)
        selection2 = int(input("What's next?\n1. Go back to menu\n" \
        "2. Exit\n Please choose an option: "))
        if selection2 == 1:
            continue
        elif selection2 == 2:
            print("The guild says goodbye, until the next one!")
            break
        else:
            print("Invalid number, try again")
## pausa aqui, preciso atualizar o menu 2 pra visualmente mostrar as informações melhor, e também pra percorrer a lista com um FOR
    elif selection == 2:
        print(roster_guild)
        selection3 = int(input("What's next?\n1. Go back to menu\n" \
        "2. Exit\n Please choose an option: "))
        if selection3 == 1:
            continue
        elif selection3 == 2:
            print("The guild says goodbye, until the next one!")
            break
        else:
            print("Invalid number, try again")
    elif selection == 3:
        print("The guild says goodbye, until the next one!")
        break
    else:
        print("Invalid number, try again")