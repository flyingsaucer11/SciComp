

#2-dimensional groundwater dynamics

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import math

# Intilize and declare variables
nx=100
ny=50
ni=5

sigma0 = 1 
a= -0.04
phi0 = 200
b= -20
lx=1000
hx=lx/nx
ly=500
hy=ly/ny
phi=[[0 for y in range(ny+1)] for x in range(nx+1)]
sigma=[[0 for y in range(ny+1)] for x in range(nx+1)]
f=[[0 for y in range(ny+1)] for x in range(nx+1)]
p=0.5

def main():
	# Set up boundary values and a trial condition
	for i in range(nx):
		x=i*hx
		for j in range(ny):
			y=j*hy
			sigma[i][j]=sigma0+a*y
			phi[i][j]=phi0+b*math.cos(math.pi*x/lx)*y/ly
			f[i][j]=0
	for step in range(ni-1):
	# Ensure boundary conditions by 4-point formula
		for j in range(ny-1):
			phi[0][j]=(4*phi[1][j]-phi[2][j])/3
			phi[nx][j]=(4*phi[nx-1][j]-phi[nx-2][j])/3
		relax2d(p,hx,hy,phi,sigma,f)

	# output the result
	ls_x=[]
	ls_y=[]
	ls_z=[]

	for i in range(nx):
		x=i*hx
		for j in range(ny):
			y=j*hy
			print("x = "+str(x)+" "+"y = "+str(y))
			print("phi["+str(i)+"]["+str(j)+"] = "+str(phi[i][j]))

			ls_x.append(x)
			ls_y.append(y)
			ls_z.append(phi[i][j])
	fig=plt.figure()
	ax=fig.add_subplot(111, projection='3d')
	ax.scatter(ls_x,ls_y,ls_z)
	plt.show()


def relax2d(p,hx,hy,u,d,s):
	# Method to perform a relaxation step in 2D
	h2=hx*hx
	a=h2/(hy*hy)
	b=1/(4*(1+a))
	ab=a*b
	q=1-p

	for i in range(nx-1):
		for j in range(ny-1):
			xp=b*(d[i+1][j]/d[i][j]+1)
			xm=b*(d[i-1][j]/d[i][j]+1)
			yp=ab*(d[i][j+1]/d[i][j]+1)
			ym=ab*(d[i][j-1]/d[i][j]+1)
			u[i][j]=q*u[i][j]+p*(xp*u[i+1][j]
				+xm*u[i-1][j]+yp*u[i][j+1]
				+ym*u[i][j-1]+h2*s[i][j])

main()   # Now starting the program
