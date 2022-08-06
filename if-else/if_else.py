# Task

# Given an integer,n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n  is even and greater than 20, print Not Weird
# Input Format
#
# A single line containing a positive integer,n.


# Print Weird if the number is weird. Otherwise, print Not Weird.
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# Weird.


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("weird")
    elif 1 < n < 6:
        print("not weird")
    elif 6 <= n < 21:
        print("weird")
    elif n > 20:
        print("not weird")
