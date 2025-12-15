import pandas as pd

roster_guild = [
    {"Name": "Arengar", "Level": 20, "Class": "Mage"},
    {"Name": "Lyria", "Level": 12, "Class": "Rogue"},
    {"Name": "Thoran", "Level": 33, "Class": "Warrior"}
]

df = pd.DataFrame(roster_guild)
print(df)