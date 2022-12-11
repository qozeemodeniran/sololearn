def add_five(x):
    return x+5

nums = [11, 22, 33, 44, 55]
results = list(map(add_five, nums))

print(results)