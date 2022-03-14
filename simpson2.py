
# Program to calculate integral with Simpson's formula (3/8)

import math
import matplotlib.pyplot as plt 
import numpy as np 

def simpson(func,low,up):		# function for Simpson's 3/8 formulae
	sum=((up-low)/8)*(func(low)+3*func((2*low+up)/3)+3*func((low+2*up)/3)+func(up)) # formulae 
	return sum

def func1(x):					# function for x^2 
	return x*x
def func2(x):					# function for sin(x)
	return math.sin(x)
def func3(x):					# function for cos(x)
	return math.cos(x)

def main():
	print('====================')
	print('Simpson\'s 3/8 formula Result:') 
	a1=simpson(func1,0,9)					# Integrate x^2 from 0 to 9
	print('x^2:'+str(a1))
	a2=simpson(func2,0,math.pi/2) 			# Integrate sin(x) from 0 to PI/2
	print('sin(x):'+str(a2))
	a3=simpson(func3,0,math.pi/2) 			# Integrate cos(x) from 0 to PI/2
	print('cos(x):'+str(a3))

	print('====================')
	print('Analytical result:')
	b1=(math.pow(9,3)/3) - (math.pow(0,3)/3)		# x^2 integrates to (x^3)/3
	print('x^2:'+str(b1))
	b2=(-1)*(math.cos(math.pi/2)-math.cos(0))		# sin(x) integrates to -cos(x) 
	print('sin(x):'+str(b2))
	b3=math.sin(math.pi/2)-math.sin(0)				# cos(x) integrates to sin(x)
	print('cos(x):'+str(b3))

	print('====================')
	print('Printing the difference:')				# difference in 15 digits after decimal point
	print('x^2:'+str(round(b1-a1,15)))
	print('sin(x):'+str(round(a2-b2,15)))
	print('cos(x):'+str(round(a3-b3,15)))

main()		# program starts here
