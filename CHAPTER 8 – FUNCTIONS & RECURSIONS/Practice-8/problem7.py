
def rem(l, word):
    n = []
    for item in l:
        if item != word:  # Exclude the specified word
            n.append(item)
    return n  # Return the list after checking all items

l = ["Harry", "arsalan", "billo", "gemini"]
print(rem(l, "arsalan"))

