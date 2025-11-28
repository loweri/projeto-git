#Create a spell to verify if an adventurer has the minimum level to use an item
def verify_item(item_name,min_level,adventurer_level):
    if adventurer_level >= min_level:
        print(f"You have all the requirements for {item_name}!")
    else:
        print(f"You don't have the necessary level for {item_name}")
#Fake Items and required levels
items = {
    "Sword Of Faith": 15,
      "The Dusk Axe": 21,
        "Blade Of Chaos": 30
}
#Fake Adventurers
adventurers = [20, 20, 33]
index = 0
#output
# print("First verification, for the Sword of Faith?")
# print("Your current level is 20.")
# newitem = verify_item("Sword Of Faith",15,20)
# print(f"{"="*40}\nSecond verification, for The Dusk Axe.")
# print("Your current level is 21.")
# newitem = verify_item("The Dusk Axe",21,20)
# print(f"{"="*40}\nThird verification, for Blade Of Chaos:")
# print("Your current level is 33.")
# newitem = verify_item("Blade of Chaos",30,33)
# NOTA: Aqui notei que eu poderia ter utilizado o loop for depois de ter feito
# -- mas preferi manter o original para lembrar o que podedria vs o que deveria
# --- segue abaixo o loop for para referência:
for item_name, min_level in items.items():
    print("="*40)
    adventurer_level = adventurers[index]
    verify_item(item_name, min_level, adventurer_level)
    index += 1