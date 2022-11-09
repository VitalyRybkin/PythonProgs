from array import *
a = array('i', [1,2,3,4])
b = array('i', [9,8,7,6])
c = array('i')

#import array
#a = array.array('i', [1, 2, 3, 4, 5])

#import array as arr
#a = arr.array('i', [4,3,2,1])

#ARRAY LENGTH
print("\nARRAY LENGTH", len(a))

#APPEND ARRAY
a.append(5)
print("\nAPPEND ARRAY", a)

#INSERT ELEMENT
a.insert(2,44)
print("\nINSERT ELEMENT", a)

#ARRAY CUT
print("\nARRAY CUT", a[:2])
print("ARRAY CUT", a[1:4])
a[2:4] = array('i', [11,22])
print("\nARRAY CUT & CHANGE", a)

#DELETE ELEMENT
del a[0]
print("\nDELETE ELEMENT", a)

#REVERSE ARRAY
a.reverse()
print('\nREVERSE ARRAY', a)

#REMOVE ELEMENT BY VALUE FROM ARRAY
a.remove(22)
print("\nREMOVE FROM ARRAY", a)

#REMOVE ELEMENT BY INDEX FROM ARRAY
a.pop(1)
print("\nREMOVE FROM ARRAY", a)
a.append(11)
a.append(11)

#COUNT ELEMENTS IN ARRAY
print('\nCOUNT ELEMENTS IN ARRAY', a.count(11), "(count 11's in this case)")



#print(a, b, c)