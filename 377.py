#r/dailyprogrammer #377
#April 25, 2019


'''You have a 2-dimensional rectangular crate of size X by Y, 
and a bunch of boxes, each of size x by y. 
The dimensions are all positive integers.

Given X, Y, x, and y,
determine how many boxes can fit into a single crate
if they have to be placed so that the x-axis of the boxes
is aligned with the x-axis of the crate, and
the y-axis of the boxes is aligned with the y-axis of the crate.
That is, you can't rotate the boxes.
The best you can do is to build a rectangle of boxes
as large as possible in each dimension.

For instance, if the crate is size X = 25 by Y = 18,
and the boxes are size x = 6 by y = 5, then the answer is 12.
You can fit 4 boxes along the x-axis (because 6*4 <= 25),
and 3 boxes along the y-axis (because 5*3 <= 18),
so in total you can fit 4*3 = 12 boxes in a rectangle.'''

def fit1(X, Y, x, y):
    boxesWidth = X//x
    boxesLength = Y//y
    return(boxesWidth * boxesLength)
    
print(fit1(25, 18, 6, 5))
print(fit1(10, 10, 1, 1))
print(fit1(12, 34, 5, 6))
print(fit1(12345, 678910, 1112, 1314))
print(fit1(5, 100, 6, 1))
print(); print()

'''You upgrade your packing robot with the latest
in packing technology: turning stuff.
You now have the option of rotating all boxes by 90 degrees,
so that you can treat a set of 6-by-5 boxes as a set of 5-by-6 boxes.
You do not have the option of rotating some of the boxes but not others.'''

def fit2(X, Y, x, y):
    return( max( fit1(X, Y, x, y),fit1(X, Y, y, x) ) )

print(fit2(25, 18, 6, 5))
print(fit2(12, 34, 5, 6))
print(fit2(12345, 678910, 1112, 1314))
print(fit2(5, 5, 3, 2))
print(fit2(5, 100, 6, 1))
print(fit2(5, 5, 6, 1))
print(); print()

'''You upgrade your warehouse to the third dimension.
You're now given six parameters, X, Y, Z, x, y, and z.
That is, you're given the X, Y, and Z dimensions of the crate,
and the x, y, and z dimensions of the boxes.
There are now six different possible orientations of the boxes.
Again, boxes cannot be rotated independently:
they all have to have the same orientation.'''

def fit3(X, Y, Z, x, y, z):
    
    
print(fit3_1(10, 10, 10, 1, 1, 1))
print(fit3_1(12, 34, 56, 7, 8, 9))
print(fit3_1(123, 456, 789, 10, 11, 12))
print(fit3_1(1234567, 89101112, 13141516, 171819, 202122, 232425))
print(); print()
