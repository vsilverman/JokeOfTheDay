import os
import random

filename = "jokes.txt"

# check if file exists
if (not os.path.exists(filename)):
	print("file " + filename + " does not exist")
	quit()

# read file into list of lines
text_file = open(filename, "r")
lines = text_file.readlines()

# find the number of lines in file
nmblines=len(lines)

# generate random int number in defined range
rand=random.randint(0, nmblines-1)

#print random number and close file
print lines[rand]
text_file.close()
