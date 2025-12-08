# The treasure and the duplicates
## Tupla/ Set
rare_artifact = ("Time Gem", 5000)
item_roll = ["Apple","Ice","Apple","Sword","Ice","Sword"]
processed_items = set(item_roll)
# the lesson is to build the lines above AND to try two things:
# first try to add a new item into rare_artifact (should give me an error)
# and second print that and the processed items
rare_artifactv2 = tuple(list(rare_artifact) + ["Time Stone", 250])
print(
    f"Extra point: {rare_artifact}\n"
    f"First point: {rare_artifactv2}\n"
    f"Second point: {processed_items}"
)