
'''

Main gui module

'''

# Imports 

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import matplotlib.pyplot as plt
import numpy as np

import rocpy_hoek as r_h
import rocpy_mohr as r_m



def file_export():
	print("export")
def file_exit():
	if messagebox.askokcancel("Exit","Do you want to exit?"):
		plt.close('all')
		window.destroy()


#------------------ CONSTRUCTORS -----------------------------------
# used to build entry boxes and text for the GUI


def entry_constructor(frame,text_var,row,col):
	label = tk.Label(frame,text=text_var)
	entry = tk.Entry(master=tools_frame)
	label.grid(row=row,column=col)
	entry.grid(row=row,column=col+1)
	entry.bind('<KeyRelease>',lambda event: register_value(text_var,entry))
	entry.insert(0,dict_values[text_var])
	return label,entry

def output_constructor(frame,text_var,row,col):
	label = tk.Label(frame,text = f'{text_var}:')
	label.grid(row=row,column=col)
	entry = tk.Label(frame,text=str(round(dict_ind[text_var],3)))
	entry.grid(row=row,column=col+1)
	return label,entry
	


#--------------------- MAIN FUNCTIONS --------------------------------------


# Calculate the H-B indices 

def main_var(dict_values):
	
	s_ci,mi,GSI,D,E_i,MR,_,_,_,_,_= dict_values.values()
	
	dict_ind['mb'] = mi*np.exp((GSI-100)/(28-(14*D)))
	dict_ind['s'] = np.exp((GSI-100)/(9-(3*D)))
	dict_ind['a'] = 0.5+((1/6)*(np.exp(-GSI/15)-np.exp(-20/3)))
	dict_ind['E_i'] = dict_values['E_i']
	
	hoek_crit()
	mohr_crit()
	dict_ind['s_1max'] = r_m.mohr_circle(dict_ind['c'],dict_ind['phi'],dict_values['s_3max'])
	
	#return dict_ind.values()
	

# Calculate the H-B rock mass parameters
def hoek_crit():
	dict_ind['s_t'],dict_ind['s_u'],dict_ind['s_cm'],_ = r_h.hoek(dict_values['s_ci'],dict_ind['mb'],dict_ind['s'],
							     dict_ind['a'],dict_values['case'],dict_values['H'],dict_values['gamma'],
							     dict_values['s_3max'],dict_values['x_value'])
	
	dict_ind['E_rm'] = dict_ind['E_i']*(0.02+((1-(dict_values['D']/2))/(1+np.exp((60+(15*dict_values['D'])-dict_values['GSI'])/11))))
	

	#print(s_t,s_u,s_cm,E_rm,s_3max)


# Calculate the M-C equivalent rock mass parameters
def mohr_crit():
	_,_,_,dict_values['s_3max'] = r_h.hoek(dict_values['s_ci'],dict_ind['mb'],dict_ind['s'],
				      dict_ind['a'],dict_values['case'],dict_values['H'],dict_values['gamma'],
				      dict_values['s_3max'],dict_values['x_value'])
	
	dict_ind['phi'],dict_ind['c'] = r_m.mohr(dict_values['s_ci'],dict_ind['mb'],dict_ind['s'],dict_ind['a'],dict_values['s_3max'],dict_values['x_value'])
	

	
	#print(np.rad2deg(phi), c)
	

# Rock mass Mohr circle display plot function
def mohr_circle_plot():
	 r_m.mohr_circle_plot()

# Register the input value written in one of the boxes (called every key release)
def register_value(key,value):
	dict_values[key]=float(value.get())
	
	
	#mb,s,a,Ei = main_var(dict_values)
	if not ei_var.get():
		dict_values['E_i'] = dict_values['MR']*dict_values['s_ci']
		E_i.configure(state='normal')
		E_i.delete(0,'end')
		E_i.insert(0,dict_values['E_i'])
		E_i.configure(state='disabled')
	else:
		dict_values['MR'] = dict_values['E_i']/dict_values['s_ci']
		MR.configure(state='normal')
		MR.delete(0,'end')
		MR.insert(0,dict_values['MR'])
		MR.configure(state='disabled')
		
	main_var(dict_values)


	
	if dict_values['case'] != 'custom':
		s_3max.configure(state='normal')
		s_3max.delete(0,'end')
		s_3max.insert(0,round(dict_values['s_3max'],3))
		s_3max.configure(state='disabled')
		
	# update output text values
	mb['text'] = str(round(dict_ind['mb'],3))
	s['text'] = str(round(dict_ind['s'],3))
	a['text'] = str(round(dict_ind['a'],3))
	s_t_val['text'] = str(round(dict_ind['s_t'],3))
	s_c_val['text'] = str(round(dict_ind['s_u'],3))
	s_cm_val['text'] = str(round(dict_ind['s_cm'],3))
	e_rm_val['text'] = str(round(dict_ind['E_rm'],3))
	c_val['text'] = str(round(dict_ind['c'],3))
	phi_val['text'] = str(round(np.rad2deg(dict_ind['phi']),3))
	s_1_val['text'] = str(round(dict_ind['s_1max'],3))
	
	if plt.fignum_exists('Failure Mohr circle'):
		r_m.mohr_circle_plot()


# Switch between E_i and MR
def toggle_ei():
	MR["state"] = "disabled"
	MR_button.toggle()
	E_i["state"] = "normal"
	if not ei_var.get():
		MR["state"] = "normal"
		E_i["state"] = "disabled"
def toggle_mr():
	MR["state"] = "normal"
	E_i_button.toggle()
	E_i["state"] = "disabled"
	if not mr_var.get():
		E_i["state"] = "normal"
		MR["state"] = "disabled"

# Modify GUI depending on the different types of application
def switch_case(event):
	dict_values['case'] = case_box.get()
	
	if dict_values['case'] == 'general':
		mohr_crit()
		s_3max.configure(state='normal')
		s_3max.delete(0,'end')
		s_3max.insert(0,dict_values['s_3max'])
		s_3max.configure(state='disabled')
		gamma.configure(state='disabled')
		H.configure(state='disabled')
				
	elif dict_values['case'] == 'tunnel' or dict_values['case'] == 'slope':
		mohr_crit()
		gamma.configure(state='normal')
		H.configure(state='normal')
		s_3max.configure(state='normal')
		s_3max.delete(0,'end')
		s_3max.insert(0,str(round(dict_values['s_3max'],3)))
		s_3max.configure(state='disabled')
	elif dict_values['case'] == 'custom':
		s_3max.configure(state='normal')
		gamma.configure(state='disabled')
		H.configure(state='disabled')

# Standard values
dict_values = {'s_ci': 30, 'mi': 10 , 'GSI': 50, 'D': 0, 'E_i': 12000,'MR': 400,'case': 'general','H':50,'gamma':0.026,'s_3max':7.5,'x_value': 5}
dict_ind = dict()


main_var(dict_values)



if __name__ == "__main__":
	
	# Menu entries
	
	file_dict = {
	"Export": file_export,
	"Exit": file_exit,
	}

	tools_dict = {
	"Hoek criterion": r_h.hoek_plot,
	"Mohr criterion": r_m.mohr_plot,
	"Mohr circle": mohr_circle_plot,
	}

	menu = [["File",file_dict],["Plots",tools_dict]]

	window = tk.Tk()
	window.geometry("500x500")

	menubar = tk.Menu(window)
	
	# cascading menu
	for entry in menu:
		menu_entry = tk.Menu(menubar,tearoff=0)
		for name,function in entry[1].items():
			menu_entry.add_command(label=name,command=function)
		menubar.add_cascade(label=entry[0],menu=menu_entry)

	window.config(menu=menubar)


	
	
#--------------------- INPUT -------------------------------------

	main_frame = tk.Frame(master=window)
	main_frame.pack(fill=tk.BOTH,expand=True)
	tools_frame = tk.Frame(master=main_frame)
	tools_frame.pack()
	
	tools_frame.rowconfigure(0,minsize=50,weight=1)
	tools_frame.columnconfigure([0,1,2,3,4,5],minsize=50,weight=1)
	input_label = tk.Label(tools_frame,text = 'H-B classification')
	input_label.grid(row=0,column=1)
	
	s_ci_label,s_ci=entry_constructor(tools_frame,'s_ci',1,0)
	
	mi_label,mi = entry_constructor(tools_frame,'mi',2,0)
	
	GSI_label,GSI = entry_constructor(tools_frame,'GSI',3,0)
	
	D_label,D = entry_constructor(tools_frame,'D',4,0)
	
	
	ei_var = tk.BooleanVar()	
	E_i_label,E_i = entry_constructor(tools_frame,'E_i',5,0)
	E_i.config(state='disabled')
	E_i_button = tk.Checkbutton(tools_frame,var=ei_var,command=toggle_ei)
	E_i_button.grid(row=5,column=2)
	
	mr_var = tk.BooleanVar()
	MR_label,MR = entry_constructor(tools_frame,'MR',6,0)
	MR_button = tk.Checkbutton(tools_frame,var=mr_var,command=toggle_mr)
	MR_button.toggle()
	MR_button.grid(row=6,column=2)
	
	failure_label = tk.Label(tools_frame,text = 'Failure envelope')
	failure_label.grid(row=7,column=1)
	
	case_label = tk.Label(tools_frame,text = 'Application')
	case_label.grid(row=8,column=0)
	case_box = ttk.Combobox(tools_frame,values=['general','tunnel','slope','custom'])
	case_box.bind('<<ComboboxSelected>>',switch_case)
	case_box.grid(row=8,column=1)
	case_box.set('general')
	
	gamma_label,gamma = entry_constructor(tools_frame,'gamma',9,0)
	gamma["state"]='disabled'
	
	H_label,H = entry_constructor(tools_frame,'H',10,0)
	H["state"]='disabled'
	
	
	s3_label,s_3max = entry_constructor(tools_frame,'s_3max',11,0)
	s_3max["state"]='disabled'
	
	x_label,x_value = entry_constructor(tools_frame,'x_value',12,0)
	
#--------------------- OUTPUT -------------------------------------

	
	hb_label = tk.Label(tools_frame,text = 'H-B criterion')
	hb_label.grid(row=0,column=4)
	
	mb_label,mb = output_constructor(tools_frame,'mb',1,3)

	s_label,s = output_constructor(tools_frame,'s',2,3)

	a_label,a = output_constructor(tools_frame,'a',3,3)
	
	
	mc_label = tk.Label(tools_frame,text = 'M-C fit')
	mc_label.grid(row=4,column=4)
	
	c_label,c_val = output_constructor(tools_frame,'c',5,3)
	phi_label,phi_val = output_constructor(tools_frame,'phi',6,3)
	
	rmp_label = tk.Label(tools_frame,text = 'Rock mass paramaters')
	rmp_label.grid(row=7,column=4)
	
	s_t_label,s_t_val = output_constructor(tools_frame,'s_t',8,3)
	s_c_label,s_c_val = output_constructor(tools_frame,'s_u',9,3)
	s_cm_label,s_cm_val = output_constructor(tools_frame,'s_cm',10,3)
	e_rm_label,e_rm_val = output_constructor(tools_frame,'E_rm',11,3)
	s_1_label,s_1_val = output_constructor(tools_frame,'s_1max',12,3)
	hoek_crit()
	mohr_crit()

	
	
	
	
	
	
	window.protocol("WM_DELETE_WINDOW",file_exit) #when closed propt the exit warning
	window.mainloop()
