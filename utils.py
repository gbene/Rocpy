
import numpy as np
import matplotlib.pyplot as plt
import matplotlib






def calc_HB(input_dict):

	out_dict = {}
	s_ci,mi,GSI,D,E_i,MR = input_dict.values()

	out_dict['value_mb'] = mi*np.exp((GSI-100)/(28-(14*D)))
	out_dict['value_s'] = np.exp((GSI-100)/(9-(3*D)))
	out_dict['value_a'] = 0.5+((1/6)*(np.exp(-GSI/15)-np.exp(-20/3)))

	return out_dict

def calc_rockm(HB_in,HB_out):

	out_dict = {}

	E_i = HB_in['value_Ei']
	D = HB_in['value_D']
	GSI = HB_in['value_GSI']
	s_ci = HB_in['value_sci']
	s = HB_out['value_s']
	a = HB_out['value_a']
	mb = HB_out['value_mb']


	out_dict['value_su'] = s_ci*np.power(s,a) #rock mass uniaxial compressive strength
	out_dict['value_st'] = (-s*s_ci)/mb #rock mass tensile strength (s_1 = s_3)
	out_dict['value_scm'] = s_ci*((mb+(4*s)-(a*(mb-(8*s))))*np.power(((mb/4)+s),(a-1)))/(2*(1+a)*(2+a)) #mass strength
	out_dict['value_erm'] = E_i*(0.02+((1-(D/2))/(1+np.exp((60+(15*D)-GSI)/11))))
	out_dict['value_s1max'] = 0

	return out_dict


def calc_MC(HB_in,fail_in,HB_out):

	out_dict = {}
	s_3max = fail_in['value_s3max']
	s_3n = fail_in['value_s3max']/HB_in['value_sci']

	s_ci = HB_in['value_sci']

	a = HB_out['value_a']
	mb = HB_out['value_mb']
	s = HB_out['value_s']

	polyn = (1+a)*(2+a)

	a_1 = 6*a*mb*np.power(s+(mb*s_3n),(a-1))

	phi_rad = np.arcsin(a_1/((2*polyn)+a_1))
	out_dict['value_phi'] = np.rad2deg(phi_rad)

	out_dict['value_c'] = (s_ci*(((1+(2*a))*s)+((1-a)*mb*s_3n))*np.power(s+(mb*s_3n),(a-1)))/(polyn*np.sqrt(1+(a_1/polyn)))

	sigma_t = -out_dict['value_c']/np.tan(phi_rad) #intersection of tangent with the x axis
	r = ((np.abs(sigma_t)+s_3max)*np.sin(phi_rad))/(1-np.sin(phi_rad)) #R length

	out_dict['value_deviatoric'] = 2*r
	out_dict['value_s1max'] = out_dict['value_deviatoric']+s_3max #s_1

	out_dict['value_fail'] = [(s_3max+r)-r*np.sin(phi_rad),r*np.cos(phi_rad)]



	return out_dict





def plot_HB(self,HB_in, HB_out, rockmass_out, mohr_out,graph_opt):

	matplotlib.use('TkAgg')

	s_ci = HB_in['value_sci']
	mb = HB_out['value_mb']
	s = HB_out['value_s']
	a = HB_out['value_a']
	s_u = rockmass_out['value_su']
	s_t = rockmass_out['value_st']
	s_cm = rockmass_out['value_scm']
	x_value = float(graph_opt['value_xres'])

	s3_values = np.arange(s_t,x_value,x_value/(x_value*1000))
	self.canvHB.ax.clear()

	self.canvHB.ax.set_title('Hoek & Brown criterion')
	self.canvHB.ax.set_xlabel(r'$\sigma_3$ [Mpa]')
	self.canvHB.ax.set_ylabel(r'$\sigma_1$ [Mpa]')
	if graph_opt['show_grid']:
		self.canvHB.ax.grid()

	if graph_opt['show_HB']:
		calc = ((mb*s3_values)/s_ci)+s

		if calc[0] < 0:
			calc[0] = -calc[0]
		s1_values = s3_values+(s_ci*np.power(calc,a))
		s1_values[0] = 0
		self.canvHB.ax.plot(np.real(s3_values),np.real(s1_values),'-k')


	if graph_opt['show_MC']:
		c = mohr_out['value_c']
		phi = np.deg2rad(mohr_out['value_phi'])

		s1_values_MC = ((2*c*np.cos(phi))/(1-np.sin(phi)))+(((1+np.sin(phi))/(1-np.sin(phi)))*s3_values)
		s1_values_MC[0] = 0
		self.canvHB.ax.plot(np.real(s3_values),np.real(s1_values_MC),'--k')



	self.canvHB.draw()

def plot_MC_circle(self,fail_in,mohr_out):

	matplotlib.use('TkAgg')

	c = mohr_out['value_c']
	phi = np.deg2rad(mohr_out['value_phi'])
	s_3max = fail_in['value_s3max']
	s_1max = mohr_out['value_s1max']
	sigma_fail, tau_fail = mohr_out['value_fail']
	r = mohr_out['value_deviatoric']/2

	sigmat = -c/np.tan(phi)

	# Circle points
	x = np.arange(s_3max,s_1max,0.00001)
	y_temp = r**2-(x-(s_3max+r))**2
	y_temp[0] = 0
	y = np.sqrt(y_temp)

	# tangent points
	sigma_tangent = np.arange(0,s_1max,0.01)
	tau_tangent = c+sigma_tangent*np.tan(phi)

	# Radius points

	xr = np.arange(sigma_fail,r+s_3max,0.001)
	yr = (-xr/np.tan(phi))+((s_3max+r)/np.tan(phi))

	self.canvMC.ax.clear()
	self.canvMC.ax.plot(x,y,'-k') #plot circle
	self.canvMC.ax.plot(sigma_tangent,tau_tangent,'-k') #plot tangent
	self.canvMC.ax.plot(sigma_fail, tau_fail,'ok') #plot tangent point
	self.canvMC.ax.plot(xr, yr,'-k') #plot radius
	self.canvMC.ax.set_title('Rock mass Mohr failure circle')
	self.canvMC.ax.set_xlabel(r'$\sigma_n$ [Mpa]')
	self.canvMC.ax.set_ylabel(r'$\sigma_\tau$ [Mpa]')

	self.canvMC.ax.set_ylim(bottom=0)
	self.canvMC.ax.set_xlim(left=0)
	self.canvMC.ax.set_aspect("equal")
	self.canvMC.draw()

def auto_sep(filename):
    from csv import Sniffer
    with open(filename,'r') as IN:
        separator = Sniffer().sniff(IN.readline()).delimiter
    return separator
