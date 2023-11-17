
def reverse_dict(my_dict):
    return {value: key for (key, value) in my_dict.items()}


print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))
