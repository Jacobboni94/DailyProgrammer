#r/dailyprogrammer #375
#May 8, 2019

'''Print a new number by adding one to each of its digit

A number is input in computer then a new no should get printed by adding one to each of its digit. If you encounter a 9, insert a 10 (don't carry over, just shift things around).

For example, 998 becomes 10109.

This challenge is trivial to do if you map it to a string to iterate over the input, operate, and then cast it back. Instead, try doing it without casting it as a string at any point, keep it numeric (int, float if you need it) only.
'''

def digitwiseAdd(myVar):
    digits = []
    myBool = True
    i = 0
    while myBool:
        digits.insert(i, myVar%10)
        myVar = myVar - myVar%10
        myVar = myVar // 10
        i += 1
        if myVar == 0 :
            myBool = False
            
    ans = 0
    for i in range(0, len(digits)) :
        digits[i] += 1
        ans += digits[i] * 10**i
        
    return ans
