PLACEHOLDER = "[name]"


with open("python/python-in-100-days-udemy/day24/mailMerge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("python/python-in-100-days-udemy/day24/mailMerge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"python/python-in-100-days-udemy/day24/mailMerge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
