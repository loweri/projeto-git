#Inventory
inventory = []
print("Welcome to your personal inventory for cooking ingredient")
while True:
    print("Please, type the ingredient to add, or 'end' to exit:")
    user_entry = input().strip().lower()
    if user_entry == "end":
        break
    else:
        inventory.append(user_entry)
print(f"Inventory finished with: {inventory}")
print("Thank you for using the app, see you next!")