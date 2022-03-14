

#least square method implementation on a given dataset

import matplotlib.pyplot as plt

x= [1,4,7,11,15,20,30,50,77,92,100]
y= [5,20,52,121,228,403,903,2504,5929,8464,10005]

sumXY=0		#summation of X*Y
sumX=0		#summation of X
sumY=0		#summation of Y
sumX2=0		#summation of X^2
N=11		

for i in range(N):		# this loop calculates the summation of X*Y, X, Y, X^2
	sumX=sumX+x[i]  
	sumY=sumY+y[i]
	sumX2=sumX2+(x[i]*x[i])
	sumXY=sumXY+(x[i]*y[i])

M = (N*sumXY-(sumX)*(sumY))/(N*sumX2-(sumX)*(sumX))		#calculates slope 
C = (sumY-M*sumX)/N 									#calculates intercept

y_new=[]		#array for new predicted values of Y from calculated M and C

for i in range(N):
	new_value=M*x[i]+C
	y_new.append(new_value)


plt.plot(x,y,'ro')		#plotting actual data points
plt.plot(x,y_new)		#plotting the predicted line fitting
plt.xlabel('X')
plt.ylabel('Y')
plt.title('LSM')
plt.show()

