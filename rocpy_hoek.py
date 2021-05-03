
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




def hoek(s_ci,mb,s,a,case,H,gamma,s3,x_value):
	
	
	

	
	s_u = s_ci*np.power(s,a) #rock mass uniaxial compressive strength
	s_t = (-s*s_ci)/mb #rock mass tensile strength (s_1 = s_3)
	s_cm = s_ci*((mb+(4*s)-(a*(mb-(8*s))))*np.power(((mb/4)+s),(a-1)))/(2*(1+a)*(2+a)) #mass strength
	hoek.s_3 = np.arange(s_t,x_value,x_value/(x_value*1000),dtype=np.complex)
	hoek.s_1 = hoek.s_3+(s_ci*np.power(((mb*hoek.s_3)/s_ci)+s,a))
	hoek.s_1[0] = 0
	
	if plt.fignum_exists('H-B criterion'):
		
		hoek_plot.ax_hoek.clear()
		hoek_plot.ax_hoek.plot(np.real(hoek.s_3),np.real(hoek.s_1),'-k');
		hoek_plot.ax_hoek.grid();
		hoek_plot.ax_hoek.set_xlabel(r'$\sigma_{3}$[MPa]');
		hoek_plot.ax_hoek.set_ylabel(r'$\sigma_{1}$[MPa]');
		hoek_plot.ax_hoek.set_title('Hoek Brown criterion');
		hoek_plot.fig_hoek.show();

	
	
	ratio = np.nan_to_num(1+(a*mb*(np.power(((mb*hoek.s_3)/(s_ci))+s,a-1)))) #this means that the input values are absurd (the invalid calculated data will be set to 0 to continue)

	s_n = (hoek.s_1+hoek.s_3)/2-(((hoek.s_1-hoek.s_3)/2)*(ratio-1)/(ratio+1))
	tau = (hoek.s_1-hoek.s_3)*(np.sqrt(ratio)/(ratio+1))

	

	if case == 'tunnel':
		s_3max = 0.47*np.power(s_cm/(gamma*H),-0.94)*s_cm
	elif case == 'slope':
		s_3max = 0.72*np.power(s_cm/(gamma*H),-0.91)*s_cm
	elif case == 'general':
		s_3max = s_ci/4
	elif case == 'custom':
		s_3max = s3
	return s_t,s_u,s_cm,s_3max

def hoek_plot():
	hoek_plot.fig_hoek, hoek_plot.ax_hoek = plt.subplots(1,num='H-B criterion');
	hoek_plot.ax_hoek.clear();
	hoek_plot.ax_hoek.plot(np.real(hoek.s_3),np.real(hoek.s_1),'-k');
	hoek_plot.ax_hoek.grid();
	hoek_plot.ax_hoek.set_xlabel(r'$\sigma_{3}$[MPa]');
	hoek_plot.ax_hoek.set_ylabel(r'$\sigma_{1}$[MPa]');
	hoek_plot.ax_hoek.set_title('Hoek Brown criterion');
	hoek_plot.fig_hoek.show();




