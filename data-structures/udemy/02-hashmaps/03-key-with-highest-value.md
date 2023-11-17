## Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

```
Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict)

Output:
b
```


### Approach1
```py
def max_value_key(my_dict):
    max_val = -1
    max_key = ''
    for (key,val) in my_dict.items():
        if max_val < val:
            max_val = val
            max_key = key
    return max_key

print(max_value_key({'a': 5, 'b': 9, 'c': 2}))
```



### Approach2
```py
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

print(max_value_key({'a': 5, 'b': 9, 'c': 2}))
```
