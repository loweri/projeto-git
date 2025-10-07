print("Arcane Academia Results")
# Part one: Collecting and validating informations
while True:
    first_note_str = input("Type your first note or 'exit' to quit: ").strip().lower()
    if first_note_str =='exit':
        break
    second_note_str = input("Type your second note or 'exit' to quit: ").strip().lower()
    if second_note_str =='exit':
        break
    # Part two: Convert and calculate
    first_note = float(first_note_str)
    second_note = float(second_note_str)
    media = (first_note + second_note) / 2
    print(f"The average is {media:.2f}")
    # Part three:
    if media >= 7:
        print(f"{media:.2f} - status *Approved*, congratulations")
    elif media >= 5:
        print(f"{media: .2f} - status *Not approved*, but you can still try again!")
    else:
        print (f"*Not Approved*, no more chances this year.")
    print("-" * 30)
# -- End of the loop here.
# - This code should run after 'break' triggered.
print("Thank you")
print("Goodbye")