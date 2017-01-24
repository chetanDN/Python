print("Hello World!")
s=input().split()
print(s)

#1
#s.reverse()    #revese() returns None after reversing not list
#print(' '.join(s))

#2
#print(" ".join(list(reversed(s))))

#few more
print(' '.join(s[::-1]))    #s[::-1] return reversed list if list or reversed string if its string

s2=input()
print(s2[::-1]) #now string reverse


"""
input:
keep moving forward
keep moving forward2

output:
Hello World!
['keep', 'moving', 'forward']
forward moving keep
2drawrof gnivom peek

"""

"""
#other way list comprehension
s=input().split()
print(' '.join(x for x in reversed(s)))
"""
