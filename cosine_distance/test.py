'''
Created on Feb 1, 2018

@author: mmp
'''

total = 0 # This is a global variable
# Function definition is here
def sum_( arg1, arg2 ):
	total = arg1 + arg2 # Here total is local variable
	print("Inside the function local total : ", total)
	return total

# Now you can call sum function
print(sum_( 10, 20 ))
print("Outside the function global total : ", total)

