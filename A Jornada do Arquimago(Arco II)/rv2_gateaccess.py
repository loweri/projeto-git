#Access Gate
print("Hello, welcome to the palace. Please, your name, or type 'exit' to quit:")
name_guest = input().strip()
if name_guest == 'exit':
    print("Thanks for coming, see you next time!")
else:
    print(f"Welcome {name_guest} to the palace, before enter I need your age:")
    age = input()
    age1 = int(age)
    if age1 < 18:
        print("Infurtunately, you're not allowed yet, come back later!")
    else:
        print("Welcome to the palace, you can enter now!")
print("Good to see you")