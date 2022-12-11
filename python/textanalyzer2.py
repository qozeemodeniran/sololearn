def count_character(text, character):
    counter = 0
    for count in text:
        if count == character:
            counter +=1
    return counter

filename = input("Enter filename: ")
with open(filename) as f:
    text = f.read()

for character in "abcdefghijklmnopqrstuvwxyz":
    percentage = 100 * count_character(text, character) / len(text)
    print("{0} - {1}%".format(character, round(percentage, 2)))