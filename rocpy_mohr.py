'''
Mohr Coulomb module. This module contains the functions used to calculate the corresponding Mohr criterion and circle.

RAW DATA:

mb
a
s
s_ci
s_3max


ELAB DATA:

phi
c
s_1max



'''

#Imports

import numpy as np
import rocpy_gui as r_g
import matplotlib.pyplot as plt


std_value = {'value': False}

def mohr(s_ci,mb,s,a,s_3max,x_value):
	s_3n = s_3max/s_ci
	s_t = (-s*s_ci)/mb #rock mass tensile strength (s_1 = s_3)
	s_3 = np.arange(s_t,x_value,x_value/(x_value*1000),dtype=np.complex)
	
	a_1 = 6*a*mb*np.power(s+(mb*s_3n),(a-1))
	polyn = (1+a)*(2+a)

	phi = np.arcsin(a_1/((2*polyn)+a_1))

	c = (s_ci*(((1+(2*a))*s)+((1-a)*mb*s_3n))*np.power(s+(mb*s_3n),(a-1)))/(polyn*np.sqrt(1+(a_1/polyn)))
	
	s_1= ((2*c*np.cos(phi))/(1-np.sin(phi)))+(((1+np.sin(phi))/(1-np.sin(phi)))*s_3)
	
	
	mohr.s_1 = np.insert(s_1,0,0)
	mohr.s_3 = np.insert(s_3,0,s_t)
	
	if plt.fignum_exists('H-B criterion') and std_value['value']:
		plt.plot(np.real(mohr.s_3),np.real(mohr.s_1),'-k');
		plt.ion()
		plt.show()
		plt.pause(0.001)
	return(phi,c)
	


def mohr_plot():
	std_value['value'] = not std_value['value']
	print(std_value)
	#std_bool = mohr_bool
	if plt.fignum_exists('H-B criterion'):
		plt.plot(np.real(mohr.s_3),np.real(mohr.s_1),'-k');
		plt.ion()
		plt.show()
		plt.pause(0.001)






