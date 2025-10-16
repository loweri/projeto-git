print("Arcane Inventory") #the name of the project
# a simple interface to ask if wanna show the report:
start_str = input("Welcome to your inventory. View report? (yes/no): ").strip().lower()
if start_str != 'yes':
    print("Closing inventory...")
#now I should define my two lists - it is about the item: mandrake root
List_of_Mandrakes = [20, -5, -3, 15, -2, -10, 30, -5] #Defined list, we need just to count
total_collected = 0
total_used = 0
index = 0
# -- now from here we start to code from "what do I want to register?"
while index < len(List_of_Mandrakes):
    current_transaction = List_of_Mandrakes[index]
    if current_transaction >= 0:
        total_collected = total_collected + current_transaction
    else:
        used_amount = current_transaction * -1
        total_used = total_used + used_amount
    index = index + 1
balance = total_collected - total_used
print("\n---Arcane Inventory Report---")
print(f"Total Mandrake Roots Collected: {total_collected}")
print("-" * 45)
print(f"Total Mandrake Roots Used: {total_used}")
print("-" * 45)
print(f"Final balance in invetory: {balance}")
print("-" * 45)