# Naive solution, O(n^2) (Memory is O(1) though)
def first_recurr_char1(arr):
    # The solution here is to go backwards from the first element, the first duplicate when going backwards
    # is the first reoccurring character
    for i in range(0, len(arr)):
        for j in range(i, -1, -1):
            if arr[j] == arr[i] and i != j:
                return arr[i]

# Using a hashmap, this can become O(n), memory complexity is O(n) as well.
# (You can use a list as well if you want)
def first_recurr_char2(arr):
    occs = {}
    for elem in arr:
        if elem in occs:
            return elem
        occs[elem] = "this can be anything, value is useless in this."


arr = [5, 2, 3, 2, 3, 4, 2, 5]
print(first_recurr_char1(arr))
print(first_recurr_char2(arr))