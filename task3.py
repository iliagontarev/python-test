'''
Chapter 3
Number with certain properties:
There are at least two groups of identical adjacent digits (like 11 and 33 in 1123345).
Going from left to right, the digits never decrease; they only ever increase or stay the same 
It is a number in the range between 372**2 and 809**2 (both ends inclusive).
The code allows to find number of possible passwords that meet the criteria.
'''

digilist = []
for i in range(372002,809003):
    digilist.append(i)

def splitter(number):
    '''
    A function that splits number into strings, returns an iterable list
    '''
    result = [int(i) for i in str(number)]
    return result
				
def doubletrouble(listed):
    '''
    A function that finds two doulbe digits in a password
    '''
    total = 0
    for i in range(0,len(listed)-1):
        if listed[i]== 0 and listed[i+1]==0:
            total += 1
        elif listed[i]== 1 and listed[i+1]==1:
            total += 1
        elif listed[i]== 2 and listed[i+1]==2:
            total += 1
        elif listed[i]== 3 and listed[i+1]==3:
            total += 1
        elif listed[i]== 4 and listed[i+1]==4:
            total += 1
        elif listed[i]== 5 and listed[i+1]==5:
            total += 1
        elif listed[i]== 6 and listed[i+1]==6:
            total += 1
        elif listed[i]== 7 and listed[i+1]==7:
            total += 1
        elif listed[i]== 8 and listed[i+1]==8:
            total += 1
        elif listed[i]== 9 and listed[i+1]==9:
            total += 1
    return total >= 2
				
def increment(lis):
    '''
    Checks for increment in the password sequence. 
    '''
    for i in lis:
        return lis[0] <= lis[1] and lis[1] <= lis[2] and lis[2] <= lis[3] and lis[3] <= lis[4] and lis[4] <= lis[5]

a = [splitter(i) for i in digilist]

def final(a):
    '''
    Calculates the final amount of outcomes; possible combinations that meet criteria.
    '''
    totalamount = 0
    for i in a:
        if increment(i) == True and doubletrouble(i) == True:
            totalamount += 1
    return totalamount
				
final(a)
  
