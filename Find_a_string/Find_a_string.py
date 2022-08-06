# Problem :
#
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
#
#
# Input Format :
# The first line of input contains the original string. The next line contains the substring.
#
# Constraints :
# 1 <= len(string)<= 200
# Each character in the string is an ascii character.
#
# Output Format :
# Output the integer number indicating the total number of occurrences of the substring in the original string.
#
#
# Sample Input :
# ABCDCDC
# CDC
#
# Sample Output :
# 2

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        l = i
        for j in range(0, len(sub_string)):
            if string[l] == sub_string[j]:
                l += 1
                if j == len(sub_string) - 1:
                    count = count + 1
                else:
                    continue
            else:
                break

    return count
