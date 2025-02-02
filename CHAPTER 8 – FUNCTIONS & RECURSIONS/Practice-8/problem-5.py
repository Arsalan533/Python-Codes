# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(2)
'''
Real-Life Example: Removing Books from a Stack
Imagine you have 3 books stacked on a table. Your task is to remove one book at a time, starting from the top.

At first, there are 3 books → You see ***
You remove one book → Now there are **
You remove another book → Now only * is left
You remove the last book → No books left, so the process stops
This is exactly how recursion works in the code! It prints a line of stars, reduces the count by 1, and repeats until no stars are left.'''
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(3)
