txt = input("Enter text: ")
def words(txt):
    for word in txt.split(' '):
        yield word
print(list(words(txt)))