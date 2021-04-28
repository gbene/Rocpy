
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


def tool_mohr():
	print("Morh Circle!")


def main_var(dict_values):
	s_ci,mi,GSI,D,E_i,MR = dict_values.values()
	dict_ind['mb'] = mi*np.exp((GSI-100)/(28-(14*D)))
	dict_ind['s'] = np.exp((GSI-100)/(9-(3*D)))
	dict_ind['a'] = 0.5+((1/6)*(np.exp(-GSI/15)-np.exp(-20/3)))
	dict_ind['E_i'] = dict_values['E_i']
	
	#return dict_ind.values()
	

def hoek_crit():
	s_t,s_u,s_cm,s_3max = r_h.hoek(dict_values['s_ci'],dict_ind['mb'],dict_ind['s'],dict_ind['a'],dict_ind['E_i'],case,H,gamma)
	E_rm = dict_ind['E_i']*(0.02+((1-(dict_values['D']/2))/(1+np.exp((60+(15*dict_values['D'])-dict_values['GSI'])/11))))
	print(s_t,s_u,s_cm,E_rm,s_3max)

def mohr_crit():
	_,_,_,s_3max = r_h.hoek(dict_values['s_ci'],dict_ind['mb'],dict_ind['s'],dict_ind['a'],dict_ind['E_i'],case,H,gamma)
	phi,c = r_m.mohr(dict_values['s_ci'],dict_ind['mb'],dict_ind['s'],dict_ind['a'],s_3max)
	c_val['text'] = str(round(c,3))
	phi_val['text'] = str(round(np.rad2deg(phi)))
	
	#print(np.rad2deg(phi), c)

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
	mohr_crit()
	mb['text'] = str(round(dict_ind['mb'],3))
	s['text'] = str(round(dict_ind['s'],3))
	a['text'] = str(round(dict_ind['a'],3))
	print(dict_ind)

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
	


dict_values = {'s_ci': 30, 'mi': 10 , 'GSI': 50, 'D': 0, 'E_i': 12000,'MR': 400}
dict_ind = dict()

H = 50
gamma = 0.026
case = 'tunnel'

main_var(dict_values)




if __name__ == "__main__":
	
	# Menu entries
	
	file_dict = {
	"Export": file_export,
	"Exit": file_exit,
	}

	tools_dict = {
	"Hoek criterion": hoek_crit,
	"Mohr criterion": mohr_crit,
	"Mohr circle": tool_mohr,
	}

	menu = [["File",file_dict],["Tools",tools_dict]]

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


	# define a main frame to which a secondary frame (tool frame) is attached. On the tool frame all of the tools can be attached

	main_frame = tk.Frame(master=window)
	main_frame.pack(fill=tk.BOTH,expand=True)
	tools_frame = tk.Frame(master=main_frame)
	tools_frame.pack()
	
	tools_frame.rowconfigure(0,minsize=50,weight=1)
	tools_frame.columnconfigure([0,1,2,3,4,5],minsize=50,weight=1)
	input_label = tk.Label(tools_frame,text = 'Input variables')
	input_label.grid(row=0,column=1)
	s_ci_label = tk.Label(tools_frame,text='s_ci')
	s_ci = tk.Entry(master=tools_frame)
	s_ci_label.grid(row=1,column=0)
	s_ci.grid(row=1,column=1)
	s_ci.bind('<KeyRelease>',lambda event: register_value('s_ci',s_ci))
	s_ci.insert(0,dict_values['s_ci'])
	
	mi_label = tk.Label(tools_frame,text='mi')
	mi = tk.Entry(master=tools_frame)
	mi_label.grid(row=2,column=0)
	mi.grid(row=2,column=1)
	mi.bind('<KeyRelease>',lambda event: register_value('mi',mi))
	mi.insert(0,dict_values['mi'])
	
	GSI_label = tk.Label(tools_frame,text='GSI')
	GSI = tk.Entry(master=tools_frame)
	GSI_label.grid(row=3,column=0)
	GSI.grid(row=3,column=1)
	GSI.bind('<KeyRelease>',lambda event: register_value('GSI',GSI))
	GSI.insert(0,dict_values['GSI'])
	
	D_label = tk.Label(tools_frame,text='D')
	D = tk.Entry(master=tools_frame)
	D_label.grid(row=4,column=0)
	D.grid(row=4,column=1)
	D.bind('<KeyRelease>',lambda event: register_value('D',D))
	D.insert(0,dict_values['D'])
	
	
	ei_var = tk.BooleanVar()	
	E_i_label = tk.Label(tools_frame,text='E_i')
	E_i = tk.Entry(master=tools_frame)
	E_i_label.grid(row=5,column=0)
	E_i.grid(row=5,column=1)
	E_i.bind('<KeyRelease>',lambda event: register_value('E_i',E_i))
	E_i.insert(0,dict_values['E_i'])
	E_i.config(state='disabled')
	E_i_button = tk.Checkbutton(tools_frame,var=ei_var,command=toggle_ei)
	E_i_button.grid(row=5,column=2)
	
	mr_var = tk.BooleanVar()
	MR_label = tk.Label(tools_frame,text='MR')
	MR = tk.Entry(master=tools_frame)
	MR_label.grid(row=6,column=0)
	MR.grid(row=6,column=1)
	MR.bind('<KeyRelease>',lambda event: register_value('MR',MR))
	MR.insert(0,dict_values['MR'])
	MR_button = tk.Checkbutton(tools_frame,var=mr_var,command=toggle_mr)
	MR_button.toggle()
	MR_button.grid(row=6,column=2)	
	
	hb_label = tk.Label(tools_frame,text = 'Hoek-Brown\ncriterion')
	hb_label.grid(row=0,column=4)
	
	mb_label = tk.Label(tools_frame,text = 'mb:')
	mb_label.grid(row=1,column=3)
	mb = tk.Label(tools_frame,text=str(round(dict_ind['mb'],3)))
	mb.grid(row=1,column=4)

	
	s_label = tk.Label(tools_frame,text = 's:')
	s_label.grid(row=2,column=3)
	s = tk.Label(tools_frame,text=str(round(dict_ind['s'],3)))
	s.grid(row=2,column=4)

	
	a_label = tk.Label(tools_frame,text = 'a:')
	a_label.grid(row=3,column=3)
	a = tk.Label(tools_frame,text=str(round(dict_ind['a'],3)))
	a.grid(row=3,column=4)
	
	mc_label = tk.Label(tools_frame,text = 'Mohr-Coulomb fit')
	mc_label.grid(row=4,column=4)
	
	c_label = tk.Label(tools_frame,text = 'c:')
	c_label.grid(row=5,column=3)
	c_val = tk.Label(tools_frame)
	c_val.grid(row=5,column=4)
	phi_label = tk.Label(tools_frame,text = 'phi:')
	phi_label.grid(row=6,column=3)
	phi_val = tk.Label(tools_frame)
	phi_val.grid(row=6,column=4)
	mohr_crit()
	
	
		
	
	
	
	window.protocol("WM_DELETE_WINDOW",file_exit) #when closed propt the exit warning
	window.mainloop()
