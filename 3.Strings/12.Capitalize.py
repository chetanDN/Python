"""
You are given a string . Your task is to capitalize each word of .

Input Format

A single line of input containing the string, .

Constraints


The string consists of alphanumeric characters and spaces.

Output Format

Print the capitalized string, .

Sample Input

hello world
Sample Output

Hello World
"""

def capitalize(string):
    str2=string
    for sub_str in string.split(' '):       #converted to mutable 
        if sub_str.isalpha():
            str2 = str2.replace(sub_str, sub_str.capitalize())
        else:
            ''.join(str2)
    
    return str2
    
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
