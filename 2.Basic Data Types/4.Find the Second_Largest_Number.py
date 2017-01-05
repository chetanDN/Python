"""
You are given  numbers. Store them in a list and find the second largest number.

Input Format 
The first line contains . The second line contains an array [] of  integers each separated by a space.

Constraints 
 

Output Format 
Output the value of the second largest number.

Sample Input

5
2 3 6 6 5
Sample Output

5
"""

if __name__ == '__main__':
    n = int(input())    
    arr = map(int, input().split())

    #smax=fmax= [x for x in arr][0]      #highly not recomended, I just used to get first element from map using [][0]    
    list1 = list(arr);
    #smax=fmax=list1[0]     #not working if 57 57 -57 57
    smax=fmax=float('-inf')     #-infinity
    
    for val in list1:
        if val > fmax:
    	    smax = fmax
    	    fmax = val
        elif (val > smax and val != fmax):
    	    smax = val
 
    #check if all elements are same
    #elif(smax == sys.minint):       
    if(smax == float('-inf')):
       print("no second max")
    else:
        print(smax)
