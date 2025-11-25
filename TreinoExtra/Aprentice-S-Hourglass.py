# The main focus of this is to exercise basic lessons to improve the base.
# Objective: One hourglass that checks the Aprentice's Age's based on year and month.
# The hourglass is a bit temperamental and if the user types something too much absurd, it refuses to answer.
# The objective is: the hourglass will calculate only once and quit due its temper.
current_year = 2025
current_month = 10 #this is just for exercise
print(f"""{("-")*50}\nHello aprentice, welcome to the hourglass interface.\n
        {("-")*50}\n
        Your age spent inside the academy is stored here. 
        if you lost track of time because some of the time zones, time flux or time exercises,
        and if you still remember the year that you were born, please get ready!\n
        {("-")*50}\n"""
    )
while True:
    #first we define our year input, then convert to INT for number, also we break if the answer is exit;
    typed_year_str = input("Please, enter your birth year, or Exit to quit: ").strip().lower()
    if typed_year_str == "exit":
        print("If you do not record your year, please adress to the #Acceptance Records at the First Tower.")
        break
    if not typed_year_str.isdigit():
        print("That's not a valid year. Try again.")
        continue
    typed_year = int(typed_year_str)
    if typed_year > current_year:
        print(f"That time is not here yet. Wrong time zone!\nLet's try again ... \n{("-")*50}")
        continue
    elif typed_year < 1915:
        print(f"Oh, are you sure? You must be an experienced aprentice!\nLet's try again ... \n{("-")*50}")
        continue
    #now here we look for the month, to finish our request, and needs to be between the first month and the current;
    while True:
        typed_month_str = input("Now enter your month(1-10): ")
        typed_month = int(typed_month_str)
        if typed_month < 1:
            print(f"Hum... That's not a month present in this world, try something between 1 and 10...\n{("-")*50}")
            continue
        elif typed_month > 10:
            print(f"You'are smart than that or your sense of time is really messed up, try something between 1 and 10...\n{("-")*50}")
            continue
    #to finish we just do the math and finish the output;
        else:
            aprentice_year = current_year - typed_year
            aprentice_month = current_month - typed_month
            print(f"\nYour senses of the flow of the time should be right, aprentice.\nYou're {aprentice_year} years and {aprentice_month} months older.")
            print("Now leave me alone and try to write down your days and months here to keep your own records.\nGoodbye.")
        break
    break