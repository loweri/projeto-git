#The Items Forge
def forge_item(item_name,current_level,upgrade_cost):
     new_level = current_level + 1
     new_gold = current_gold - upgrade_cost
     return new_level, item_name, new_gold
#defining the variables
# we could consider that everything depends on the item, I'll set two
### we start with the dict of the item and it's cost to upgrade:
items = {
     "Beginner Sword": 5,
    "Apprentice Sword": 15,
}
current_gold = 100
### let's try and check the results
weap, levelup, gold_left = forge_item("Beginner Sword", 1, items["Beginner Sword"])
print(
     f"The new level it is {levelup}.\n"
     f"Your weapon {weap} was suscesfully upgraded!\n"
     f"Your current gold is: {gold_left}.\n"
)
current_gold = gold_left
weap2, levelup2, gold_left2 = forge_item("Apprentice Sword", 3, items["Apprentice Sword"])
print(
     f"The new level it is {levelup2}.\n"
     f"Your weapon {weap2} was suscesfully upgraded!\n"
     f"Your current gold is: {gold_left2}.\n"
)