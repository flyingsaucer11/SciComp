
# Program to calculate integral with Simpson's formula (1/3)

import math
import matplotlib.pyplot as plt 
import numpy as np 

def simpson(func,low,up,N):		# function for Simpson's 1/3 formulae
	h=(up-low)/N 				# calculating h from h=(upper value- lower value)/N
	x=np.linspace(low,up,N+1) 	# linear spacing, here N should be even
	func=np.vectorize(func)		# vectorizing the function to work on a numpy array
	y=func(x)					# getting the function's outputs

	list1=[x for x in y[1:] if np.where(y[1:]%3!=0)]
	list2=[x for x in y[1:] if np.where(y[1:]%3==0)]

	sum=h/3*np.sum(y[0:-1:2]+list1*3+list2*2)  	# calculating the sum utilizing the numpy array
	return sum

def func1(x):					# function for x^2 
	return x*x
def func2(x):					# function for sin(x)
	return math.sin(x)
def func3(x):					# function for cos(x)
	return math.cos(x)

def main():
	print('====================')
	print('Simpson\'s 1/3 formula Result:') 	# N is taken as 1000
	a1=simpson(func1,0,9,999)					# Integrate x^2 from 0 to 9
	print('x^2:'+str(a1))
	a2=simpson(func2,0,math.pi/2,999) 			# Integrate sin(x) from 0 to PI/2
	print('sin(x):'+str(a2))
	a3=simpson(func3,0,math.pi/2,999) 			# Integrate cos(x) from 0 to PI/2
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
