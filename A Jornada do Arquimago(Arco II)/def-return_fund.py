#Lets create a flex EXP calculator: calculate the new EXP (even if doesnt count the actual or the gain)
def calculate_texp(cexp,gexp):
    final_exp = cexp + gexp
    return final_exp
print("Let's check how much exp you'll have with the exp acquired")
tot_exp = calculate_texp(1000,50)
print(f"This is the final result of your exp: {tot_exp}")