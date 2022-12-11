text = input("Enter sentence: ")
text = text.split(' ')

print(max(text, key=len))