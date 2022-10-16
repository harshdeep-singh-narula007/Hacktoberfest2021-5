def test(words):
    return  max(words, key=len) 
strs =  ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Longest string of the said list of strings:")
print(test(strs))
strs =  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print("\nOriginal strings:")
print(strs)
print("Longest string of the said list of strings:")
print(test(strs))
