#form reader
member = {"name": "Lyra", "class": "Elfarcher", "level": 10}
for names,result in member.items(): #this one I don't recall, need to check on the previous lessons
    print(f"Key: {names}, Value: {result}")
lyra_class = member["class"]
print(f"Lyra's class is: {lyra_class}")