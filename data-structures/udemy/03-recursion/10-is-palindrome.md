
## isPalindrome
Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.

```
Examples

isPalindrome('awesome') # false
isPalindrome('foobar') # false
isPalindrome('tacocat') # true
isPalindrome('amanaplanacanalpanama') # true
isPalindrome('amanaplanacanalpandemonium') # false
```

## Approach

```py
def isPalindrome(strng):
    if len(strng) == 1:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])

print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("python"))
```