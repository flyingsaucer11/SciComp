# -*- coding: utf-8 -*-
print('format:DEG')
T=input('temperature: ')
R=input('humidity: ')

c1=-8.78469475556
c2=1.61139411
c3=2.33854883889
c4=-0.14611605
c5=-0.012308094
c6=-0.0164248277778
c7=0.002211732
c8=0.00072546
c9=-0.000003582

HI= c1+c2*T+c3*R+c4*T*R+c5*T*T+c6*R*R+c7*T*T*R+c8*T*R*R+c9*T*T*R*R

print('feels like: '+str(HI))