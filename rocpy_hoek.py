
'''
Hoek & Brown failure module. This module contains the functions used to calculate the Hoek-Brown failure Criterion (2002).





RAW DATA:

mi: material constant calculated in lab or tabulated
GSI: Geologic Strength Index calculated or tabulated
D: Security factor, depends on the application (tabulated).
s_ci [MPa]: intact uniaxial compression (calculated or tabulated).
MR/Ei (introduced in Hoek 2006): Modulus ratio (calculated or tabulated).

To calculate s_3max:

H [m]: depth
gamma [MN/m3]: unit weight (calculated or tabulated)



ELAB DATA:

mb
a
s

s_1 [MPa]
s_t [MPa] (traction strength)
s_cm [MPa] (Mass strength)
s_n [MPa] (normal stress)
tau [MPa] (shear stress)
E_rm [MPa] (rock mass Young modulus) 
s_3max [MPa] (failure s_3 value)




'''
#Imports

import numpy as np
import matplotlib.pyplot as plt



def hoek(s_ci,mb,s,a,Ei,case,H,gamma,s3):
	
	#fig_hoek, ax_hoek = plt.subplots(1,num='H-B criterion')
	

		
	s_u = s_ci*np.power(s,a) #rock mass uniaxial compressive strength
	s_t = (-s*s_ci)/mb #rock mass tensile strength (s_1 = s_3)
	s_cm = s_ci*((mb+(4*s)-(a*(mb-(8*s))))*np.power(((mb/4)+s),(a-1)))/(2*(1+a)*(2+a)) #mass strength
	s_3 = np.arange(s_t,1,0.01)
	print(s_3)
	s_1 = s_3+(s_ci*np.power(((mb*s_3)/s_ci)+s,a))
	
	print(f's_1: {s_1}')
	#ax_hoek.plot(s_3,s_1,'-k')

	ratio = 1+(a*mb*((mb*s_3)/(s_ci)+s)**(a-1))

	s_n = (s_1+s_3)/2-(((s_1-s_3)/2)*(ratio-1)/(ratio+1))
	tau = (s_1-s_3)*(np.sqrt(ratio)/(ratio+1))

	

	if case == 'tunnel':
		s_3max = 0.47*np.power(s_cm/(gamma*H),-0.94)*s_cm
	elif case == 'slope':
		s_3max = 0.72*np.power(s_cm/(gamma*H),-0.91)*s_cm
	elif case == 'general':
		s_3max = s_ci/4
	elif case == 'custom':
		s_3max = s3
	return s_t,s_u,s_cm,s_3max






