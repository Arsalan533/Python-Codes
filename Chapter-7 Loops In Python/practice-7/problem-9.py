'''
***
* * for n = 3
*** 
'''

# n =  int(input("Enter the number: "))
# for i in range(1, n+1):
#     if(i==1 or  i==n):
#         print("*"* n, end="")
#     else:
#          print("*", end="")  
#     print(" "* (n-2), end="")   
#     print("*", end="")
# print("")                             
n = int(input("Enter the number: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)  # First and last row filled with stars
    else:
        print("*" + " " * (n-2) + "*")  # Middle rows with spaces between stars
