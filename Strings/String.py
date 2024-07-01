"""
String is a data type in Python

String is a sequence of characters enclosed in quotations

"""

""" ///////////// STRING SLICING ////////// """


"""
varibale[index_start : index_end]
        (INCLUDED)    (NOT INCLUDED)
        
variable[index_start : index_end : how many steps you want to skip]
"""
str = "HELLOWORLD!!"

var = str[::-1]


''' /////////////// STRING FUNCTIONS ////////////////// '''

str1 = "czechoslavakia"

var1 = len(str1)
var2 = str1.endswith("ar") 
var3 = str1.count("a")
var4 = str1.capitalize()
var5 = str1.find("z")

var6 = str1.replace("z", "x")

"""
///////////////////// ESCAPE SEQUENCE CHARACTERS ///////////////////////

"""


string = "My home is in Padrauna \"city\"."
string1 = "Name:\tSherlock"
string2 = "Name:\tJohn\nAge:\t42\nJob:\t\"Doctor\""
a = """Once upon a tim
      tyjytj
      "ghgfhgfhh"
      fghfg
      long long ago"""
      
print(a)
"""
C.W
1 - Write a python program to display an user name followed by Good Afternoon

2 - Write a python program that makes inital Abbrevations from a user's name.


"""

"""
H.W

{1 - Write a program to detect  double spacing in a string.}X
{2 - Write a program that uses all the string functions given in the class notes.}X

3 - Write a program to replace Name and Date format template
4 - Replace the double spaced poblem with a single space.
5 - Write a paragraph using only escape sequence characters.

"""


letter = """
Dear <Name>
You are selected !!
<Date>
"""