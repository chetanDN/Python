"""
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum() 
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha() 
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit() 
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower() 
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper() 
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
Task

You are given a string . 
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

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

if __name__ == '__main__':
    s = input()
    
    #for e in ['isalnum','isalpha','isdigit','islower','isupper']: print(any(getattr(c,e)() for c in s))
    
    """
    In the first line, print True if  has {any} alphanumeric characters. Otherwise, print False. 
    In the second line, print True if  has {any} alphabetical characters. Otherwise, print False. 
    In the third line, print True if  has {any} digits. Otherwise, print False. 
    In the fourth line, print True if  has {any} lowercase characters. Otherwise, print False. 
    In the fifth line, print True if  has {any} uppercase characters. Otherwise, print False.
    """
    
    print(any(ch.isalnum()  for ch in s) )      #any() will go as far as the condition required is True, unlike list[] >0 which calulates all items
    print( any(ch.isalpha() for ch in s) )
    print( any(ch.isdigit() for ch in s) )
    print( any(ch.islower() for ch in s) )
    print( any(ch.isupper() for ch in s) )
    
"""
s = raw_input()
commands = "isalnum() isalpha() isdigit() islower() isupper()"
print "\n".join(str(any(eval("c."+cmd)  for c in s)) for cmd in commands.split())


Eval means evaluate, it interprets a string as code.
From string "commands" we are getting commands one by one so eval just run summarized sting "c." + "isalnum()" as command.
eval(c.isalnum()) and in "c" we are getting input value from s = raw_input()


You don't need eval here, remember that a method is only a function, which gets self as it's first argument:
s = input()
for fn in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(fn(c) for c in s))

"""
    
    
    
"""


+-----------------------------------------+---------+---------+
|                                         |   any   |   all   |
+-----------------------------------------+---------+---------+
| All Truthy values                       |  True   |  True   |
+-----------------------------------------+---------+---------+
| All Falsy values                        |  False  |  False  |
+-----------------------------------------+---------+---------+
| One Truthy value (all others are Falsy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| One Falsy value (all others are Truthy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| Empty Iterable                          |  False  |  True   |
+-----------------------------------------+---------+---------+

any

Return True if any element of the iterable is true. If the iterable is empty, return False
Since none of the elements is true, it returns False in this case.

all

Return True if all elements of the iterable are true (or if the iterable is empty).
Since none of the elements is false, it returns True in this case.

"""


