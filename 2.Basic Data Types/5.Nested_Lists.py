"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output

Berry
Harry
Explanation

There are  students in this class whose names and grades are assembled to build the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""

import operator
if __name__ == '__main__':
    markslist = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        #markslist[name] = score    #or
        markslist.update({name:score})

    #to know second highest form a set(unique) of marks, sort it, and in [1] will be second highest 
    set1 = set(value for key,value in markslist.items()) #we need sorted values(marks) as set not sorted keys
    list1 = sorted(set1)        #sorted() returns the list, so sort on set as for set {1,2} and {2,1} are same
    second_highest = list1[1]

    
    #It is not possible to sort a dict,  need a sorted representation, which will be a list—probably a list of tuples.
    sorted_dict_acc_keys = sorted(markslist.items(), key=operator.itemgetter(0))    #sorted dictionary according to keys,actually list of tuples 3key=operator.itemgetter(1) -> to sort according to values
    #print(sorted_dict_acc_keys)
    for name,marks in sorted_dict_acc_keys:
        if marks == second_highest:
            print(name)
    
