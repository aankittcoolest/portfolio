### Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

```
Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)

Output:
{'a': 1, 'b': 5, 'c': 7, 'd': 5}
```

## Approach
- Loop through second dictionary and add new elements or sum existing elements with first dictionary.


```py
def merge_dicts(dict1, dict2):
    for key in dict2:
        if dict1.get(key):
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]

    return dict1


print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}))
```