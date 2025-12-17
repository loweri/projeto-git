import pandas as pd

roster_guild = [
    {"Name": "Arengar", "Level": 20, "Class": "Mage"},
    {"Name": "Lyria", "Level": 12, "Class": "Rogue"},
    {"Name": "Thoran", "Level": 33, "Class": "Warrior"},
    {"Name": "Mira", "Level": 18, "Class": "Mage"},
    {"Name": "Dorn", "Level": 25, "Class": "Warrior"}
]

df = pd.DataFrame(roster_guild)

print("📊 Guild Sheet")
print(df)

print("\n🧙 Class by Quantity")
print(df["Class"].value_counts())

print("\n⭐ Average guild level")
print(df["Level"].mean())

result_tst = (
    df[df["Level"] >= 20]              # filtro
      .sort_values(by="Level", ascending=False)  # ordenação
      [["Name", "Class"]]              # seleção de colunas
)

print(f"\n{result_tst}")

# Regra de Power diferente por classe
df["Power"] = df["Level"]

df.loc[df["Class"] == "Mage", "Power"] *= 12
df.loc[df["Class"] == "Warrior", "Power"] *= 10
df.loc[df["Class"] == "Rogue", "Power"] *= 8

# Filtrar os mais fortes
elite = df[df["Power"] >= 200]

# Ordenar do mais forte pro mais fraco
elite = elite.sort_values(by="Power", ascending=False)

print(f"\n{elite}")