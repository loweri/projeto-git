#Efficient Alchemist
def calculate_request(potion_amount,unitary_weight):
    total_volume = potion_amount * 10
    final_weight = potion_amount * float(unitary_weight)
    return total_volume, final_weight
###
volume, weight = calculate_request(33,1.5)
print(
    f"Total volume: {volume} ml.\n"
    f"Total weight: {weight} g."
)