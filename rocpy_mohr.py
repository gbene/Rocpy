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
		plt.figure('H-B criterion')
		plt.plot(np.real(mohr.s_3),np.real(mohr.s_1),'-k');
		plt.ion()
		plt.show()
		plt.pause(0.001)
	return(phi,c)



def mohr_plot():
	std_value['value'] = not std_value['value']
	#std_bool = mohr_bool
	if plt.fignum_exists('H-B criterion'):
		plt.figure('H-B criterion')
		plt.plot(np.real(mohr.s_3),np.real(mohr.s_1),'-k');
		plt.ion()
		plt.show()
		plt.pause(0.001)


def mohr_circle(c,phi,s_3max):




	sigmat = -c/np.tan(phi)
	r = ((np.abs(sigmat)+s_3max)*np.sin(phi))/(1-np.sin(phi)) #R length

	sigma1 = 2*r+s_3max #s_1
	#print(sigma1,r)

	# Build circle

	mohr_circle.x = np.arange(s_3max,sigma1,0.0001) 
	mohr_circle.y = np.nan_to_num(np.sqrt(r**2-(mohr_circle.x-(s_3max+r))**2))
	


	# Tangent point
	mohr_circle.sigmam = (s_3max+r)-r*np.sin(phi)
	mohr_circle.taum = r*np.cos(phi)
	
	mohr_circle.sigman_retta = np.arange(0,sigma1,0.01)
	mohr_circle.tau_retta = c+mohr_circle.sigman_retta*np.tan(phi)
	

	#print(sigmam)

	# Radius
	mohr_circle.xr = np.arange(mohr_circle.sigmam,r+s_3max,0.0001)
	mohr_circle.yr = (-mohr_circle.xr/np.tan(phi))+((s_3max+r)/np.tan(phi))

	#plt.rc('text',usetex=True)
	#plt.rc('font',family='times')

	return(sigma1)

def mohr_circle_plot():

	if plt.fignum_exists('Failure Mohr circle'):
		plt.figure('Failure Mohr circle').clear()

	fig_circle, ax_circle = plt.subplots(1,num='Failure Mohr circle')
	#plt.pause(0.001)
	
	ax_circle.plot(mohr_circle.x,mohr_circle.y,'-k')
	ax_circle.plot(mohr_circle.sigman_retta,mohr_circle.tau_retta,'-k')
	ax_circle.plot(mohr_circle.xr,mohr_circle.yr,'-k',linewidth=1)
	ax_circle.plot(mohr_circle.sigmam,mohr_circle.taum,'ok',markersize=5)
	#ax_circle.annotate(f'({np.around(sigmam,2)};{np.around(taum,2)})',(sigmam,taum),xytext=(2.5,1.2*taum),arrowprops=arrowprops)
	fig_circle.show()
	ax_circle.set_ylim(bottom=0)
	ax_circle.set_xlim(left=0)
	ax_circle.set_aspect("equal")
	ax_circle.set_xlabel(r"$\sigma_n$ [MPa]")
	ax_circle.set_ylabel(r"$\tau$ [MPa]")
	ax_circle.set_title("Rock mass Mohr failure circle")








