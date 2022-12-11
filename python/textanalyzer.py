def count_character(text, character):
    counter = 0
    for count in text:
        if count == character:
            counter +=1
    return counter

filename = input("Enter filename: ")
with open(filename) as f:
    text = f.read()

print(count_character(text, "r"))