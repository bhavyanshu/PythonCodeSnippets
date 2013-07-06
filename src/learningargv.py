import sys #* Read the comment for lines marked with asterisk symbol. (comment this if executing from console)
from sys import argv

sys.argv = raw_input('Enter command line arguments: ').split() #* (comment this if executing from console)

# This i have used because i am using pyDev for eclipse and hence i do not execute the scripts directly. Hence passing arguments like $filename.py scriptname argument1, argument2, argument3, argument 4 is not possible. 
# So i have this workaround in which it interactively asks the user to insert arguments during program execution

script,first,second,third=argv

print"The script is called:",script
print"Your first variable is:",first
print"Your second variable is:",second
print"Your third variable is:",third

# (For those using terminal console):
# Input will be "python learningargv.py argv 1 2 3"
# The script is called: argv
# Your first variable is: 1
# Your second variable is: 2
# Your third variable is: 3