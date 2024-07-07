# lists = [True, "bear", 45, 45.0, None]
# #        0       1      2   3     4

# sliced_list = lists[1::3]
# print(sliced_list)   

# /////////// LIST METHODS ///////////////////

listis= [4,8,2,7,44,5,11,87]
listis.sort()
listis.reverse()
listis.append("This is the last Value")
listis.insert(6,88)
listis.pop(0)
listis.remove("This is the last Value")

"""
1 - Write a program to store seven differnet data types in a list.

2 - Write a program to accept marks of six different students and arrange them (the marks) in a sorted manner.
start the list with an empty list.

3 - Write a program to sum all the marks that were taken in the 2nd question.
"""


"""
//////////////////////////////////////// TUPPLES //////////////////////////////////

=> Numeric Type : int float 
=> Boolean Type : True or False
=> Sequence Type : str list tuple
=> Set Type : set frozenset
=> Mapping Type : dict
=> None

Immutable [Tupples are unchangeable] lists. Collection of items.
"""



""" 
///////////////////////// FUNCTIONS OF TUPPLE ////////////////////

"""

tupp = (1,2,3,4,5,6,3,3,4,5) 
use1 = tupp.count(3)
use2 = tupp.index(4)




"""
H.W

1 - Write a program to count the number of "Mangoes" in the following tupple

("Apple", "Mangoes", "Peach", "Mangoes", "Lichi","Mangoes")

2 - Write and fail a program that ultimately proves the immutability of tupples.

"""