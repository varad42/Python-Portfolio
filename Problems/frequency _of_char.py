def freq(word):
    storage = {}
    for i in word:
        if i in storage:
            storage[i] = storage[i] + 1
        else:
            storage[i] = 1
    return storage

print(freq("banana"))  # {'b': 1, 'a': 3, 'n': 2}
print(freq("aaaa"))  # {'a': 4}
print(freq(""))  # {}