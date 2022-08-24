def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


# "olleh"
# "h" + "olle"
# "he" + "oll"
# ...
# "hello" + ""
# Base case: When len of str is 0
def reverse_string(str):
    if not str:  # Empty string eval to false, python can be unintuitive sometimes...
        return ""
    return str[-1] + reverse_string(str[:-1])


def all_strings_given_set(set, k, str=""):
    if k == 0:
        return print(str)
    for e in set:
        all_strings_given_set(set, k-1, str + e)


print(factorial(5))
print(fibonacci(8))
print(reverse_string("Reverse this string recursively"))
all_strings_given_set(['a', 'b', 'c'], 3)
