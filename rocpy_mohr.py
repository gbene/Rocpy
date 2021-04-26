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
import rocpy_hoek as r_h




def mohr(s_ci,mb,s,a,s_3max):
	s_3n = s_3max/s_ci

	a_1 = 6*a*mb*np.power(s+(mb*s_3n),(a-1))
	polyn = (1+a)*(2+a)

	phi = np.arcsin(a_1/((2*polyn)+a_1))

	c = (s_ci*(((1+(2*a))*s)+((1-a)*mb*s_3n))*np.power(s+(mb*s_3n),(a-1)))/(polyn*np.sqrt(1+(a_1/polyn)))
	
	return(phi,c)
	









