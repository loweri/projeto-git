while True:
    try:
        level_asked = int(input("Please, type your level:"))
        print("Level accepted\n")
        break
    except ValueError:
        print("Number not valid, try again")
print(f"Your current level is {level_asked}")