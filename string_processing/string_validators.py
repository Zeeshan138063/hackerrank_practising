"""
Python has built-in string validation methods for basic data. It can check
if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

Task

You are given a string .
Your task is to find out if the string  contains:
alphanumeric characters,
alphabetical characters,
digits,
lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
"""


def string_format(string):
    # In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    print(any(c.isalnum() for c in string))
    # In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    print(any(c.isalpha() for c in string))
    # In the third line, print True if  has any digits. Otherwise, print False.
    print(any(c.isdigit() for c in string))
    # In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    print(any(c.islower() for c in string))
    # In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    print(any(c.isupper() for c in string))


if __name__ == '__main__':
    s = input()
    string_format(s)
