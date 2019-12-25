"""
Find a string

In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2
"""


def count_substring(string, substring):
    # Initialize count and start to 0
    count = 0
    start = 0

    # Search through the string till
    # we reach the end of it
    while start < len(string):

        # Check if a substring is present from
        # 'start' position till the end
        flag = string.find(substring, start)

        if flag != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            start = flag + 1

            # Increment the count
            count += 1
        else:
            # If no further substring is present
            # return the value of count
            return count


if __name__ == '__main__':
    # string='ABCDCDC'
    # sub_string='CDC'
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
