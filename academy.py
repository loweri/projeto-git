print("Arcane Academia Results")
cal_avg = [] #caculated average
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
    average = (first_note + second_note) / 2
    cal_avg.append(average) #section added further on studies
    print(f"The average is {average:.2f}")
    # Part three - the conditions to run the math
    if average >= 7:
        print(f"{average:.2f} - status *Approved*, congratulations")
    elif average >= 5:
        print(f"{average: .2f} - status *Not approved*, but you can still try again!")
    else:
        print (f"*Not Approved*, no more chances this year.")
    print("-" * 30)
# -- End of the loop here.
# - This code should run after 'break' triggered.
print(f"\n{"-" * 5} Final record {"-" * 5}")
print(f"Recorded averages: {cal_avg}")
print("Thank you")
print("Goodbye")