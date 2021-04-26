
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


def main_var(mi,GSI,D,s_ci,MR):
	
	mb = mi*np.exp((GSI-100)/(28-(14*D)))
	s = np.exp((GSI-100)/(9-(3*D)))
	a = 0.5+((1/6)*(np.exp(-GSI/15)-np.exp(-20/3)))
	Ei = MR*s_ci
	return(mb,s,a,Ei)
	

def hoek_crit():
	s_t,s_u,s_cm,s_3max = r_h.hoek(s_ci,mb,s,a,Ei,case,H,gamma)
	print(s_t,s_u,s_cm,E_rm,s_3max)

def mohr_crit():
	_,_,_,s_3max = r_h.hoek(s_ci,mb,s,a,Ei,case,H,gamma)
	phi,c = r_m.mohr(s_ci,mb,s,a,s_3max)
	print(np.rad2deg(phi), c)

mi = 10
GSI = 50
D=0
s_ci = 30
MR = 400

H = 50
gamma = 0.026
case = 'tunnel'

mb,s,a,Ei = main_var(mi,GSI,D,s_ci,MR)

E_rm = Ei*(0.02+((1-(D/2))/(1+np.exp((60+(15*D)-GSI)/11))))


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
	window.geometry("400x500")

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
	tools_frame = tk.Frame(master=window)
	tools_frame.pack(fill=tk.BOTH,expand=True)	
    
	window.protocol("WM_DELETE_WINDOW",file_exit) #when closed propt the exit warning
	window.mainloop()
