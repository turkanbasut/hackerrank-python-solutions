# Task
# Read a given string, change the character at a given index and then print the modified string.
#
# Input Format
# The first line contains a string, S.
#
# The next line contains an integer i, denoting the index location and a character c separated by a space.
#
# === codingbroz.com_728x90 (#88864) === === codingbroz.com_728x90 (#88864) ===
# Output Format
# Using any of the methods explained above, replace the character at index i with character c.
#
# Sample Input
#
# abracadabra
# 5 k
# Sample Output
#
# abrackdabra


def mutate_string(string, position, character):
    n = list(string)
    n[position] = character
    string = "".join(n)
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)