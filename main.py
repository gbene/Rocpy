# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rocpy.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from numpy import power,round


import utils as ut

from main_ui import Ui_Rocpy
from dialogs import miGui,sciGui,import_dialog


matplotlib.use('TkAgg')



class pltCanvas(FigureCanvasQTAgg):

	def __init__(self,parent=None):
		self.fig= Figure()
		self.ax = self.fig.add_subplot(111)

		super(pltCanvas,self).__init__(self.fig)





class MainWindow(Ui_Rocpy):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)


		self.HB_in = {'value_sci': 30.0,
					  'value_mi': 10.0 ,
					  'value_GSI': 50.0,
					  'value_D': 0.0,
					  'value_Ei': 12000.0,
					  'value_MR': 400.0}

		self.fail_in = {'value_application': 'general',
						'value_H': 50.0,
						'value_gamma':0.026,
						'value_s3max':7.5}

		self.graph_opt = {'value_xres':5.0,
						  'show_HB':2.0,
						  'show_MC':0.0,
						  'show_grid': 1}

		self.HB_out = ut.calc_HB(self.HB_in)
		self.mohr_out = ut.calc_MC(self.HB_in,self.fail_in,self.HB_out)
		self.rockmass_out = ut.calc_rockm(self.HB_in,self.HB_out)

		self.fig= Figure()
		self.ax = self.fig.add_subplot(111)

		self.actionImport_HB_data.triggered.connect(lambda: import_dialog(parent=self))
		self.selectMi.clicked.connect(lambda: miGui(parent=self))
		self.selectSci.clicked.connect(lambda: sciGui(parent=self))

		self.value_sci.returnPressed.connect(lambda: self.value_change(self.value_sci.objectName(),self.value_sci.text()))

		self.value_mi.returnPressed.connect(lambda: self.value_change(self.value_mi.objectName(),self.value_mi.text()))

		self.value_GSI.returnPressed.connect(lambda: self.value_change(self.value_GSI.objectName(),self.value_GSI.text()))

		self.value_D.returnPressed.connect(lambda: self.value_change(self.value_D.objectName(),self.value_D.text()))

		self.value_Ei.returnPressed.connect(lambda: self.value_change(self.value_Ei.objectName(),self.value_Ei.text()))

		self.calc_Ei.stateChanged.connect(lambda: self.check_change(self.calc_Ei.objectName(),self.calc_Ei.checkState()))

		self.value_MR.returnPressed.connect(lambda: self.value_change(self.value_MR.objectName(),self.value_MR.text()))

		self.calc_MR.stateChanged.connect(lambda: self.check_change(self.calc_MR.objectName(),self.calc_MR.checkState()))

		self.value_application.currentIndexChanged.connect(lambda: self.value_appl_change(self.value_application.objectName(),self.value_application.currentText()))

		self.value_gamma.returnPressed.connect(lambda: self.value_changefail(self.value_application.currentText(),self.value_gamma.objectName(),self.value_gamma.text()))

		self.value_H.returnPressed.connect(lambda: self.value_changefail(self.value_application.currentText(),self.value_H.objectName(),self.value_H.text()))

		self.value_s3max.returnPressed.connect(lambda: self.value_changefail(self.value_application.currentText(),self.value_s3max.objectName(),self.value_s3max.text()))

		self.show_HB.stateChanged.connect(lambda: self.options_check(self.show_HB.objectName(),self.show_HB.checkState()))

		self.show_MC.stateChanged.connect(lambda: self.options_check(self.show_MC.objectName(),self.show_MC.checkState()))

		self.show_grid.stateChanged.connect(lambda: self.options_check(self.show_grid.objectName(),self.show_grid.checkState()))

		self.value_xres.valueChanged.connect(lambda: self.value_changegraph(self.value_xres.objectName(),self.value_xres.text()))

		self.update_form(self.HB_class.findChildren(QtWidgets.QLineEdit),self.HB_in)
		self.update_form(self.fenv.findChildren(QtWidgets.QLineEdit),self.fail_in)

		self.update_form(self.form_HBcrit.findChildren(QtWidgets.QLabel),self.HB_out,1)
		self.update_form(self.Form_MCfit.findChildren(QtWidgets.QLabel),self.mohr_out,1)
		self.update_form(self.Form_rockmass.findChildren(QtWidgets.QLabel),self.rockmass_out,1)

		self.canvHB = pltCanvas(self)

		self.toolbarHB = NavigationToolbar(self.canvHB,self.PlotPage1)
		self.Pg1_layout = QtWidgets.QVBoxLayout(self.PlotPage1)
		self.Pg1_layout.addWidget(self.canvHB)
		self.Pg1_layout.addWidget(self.toolbarHB)


		self.canvMC = pltCanvas(self)
		self.toolbarMC = NavigationToolbar(self.canvMC,self.PlotPage1)
		self.Pg2_layout = QtWidgets.QVBoxLayout(self.PlotPage2)
		self.Pg2_layout.addWidget(self.canvMC)
		self.Pg2_layout.addWidget(self.toolbarMC)





		ut.plot_HB(self,self.HB_in, self.HB_out, self.rockmass_out,self.mohr_out,self.graph_opt)
		ut.plot_MC_circle(self,self.fail_in,self.mohr_out)

	def value_change(self,name,text):

		# if self.inQueue.not_empty:
		# 	try:
		# 		self.consoleWindow.append(self.inQueue.get_nowait())
		# 	except:
		# 		True

		self.HB_in[name] = float(text)




		if self.calc_MR.checkState():
			self.HB_in['value_Ei'] = self.HB_in['value_MR']*self.HB_in['value_sci']
			self.value_Ei.setText(str(round(self.HB_in['value_Ei'],3)))
		else:
			self.HB_in['value_MR'] = self.HB_in['value_Ei']/self.HB_in['value_sci']
			self.value_MR.setText(str(round(self.HB_in['value_MR'],3)))


		self.HB_out = ut.calc_HB(self.HB_in)
		self.mohr_out = ut.calc_MC(self.HB_in,self.fail_in,self.HB_out)
		self.rockmass_out = ut.calc_rockm(self.HB_in,self.HB_out)

		self.update_form(self.HB_class.findChildren(QtWidgets.QLineEdit),self.HB_in)
		self.update_form(self.fenv.findChildren(QtWidgets.QLineEdit),self.fail_in,1)
		self.update_form(self.form_HBcrit.findChildren(QtWidgets.QLabel),self.HB_out,1)
		self.update_form(self.Form_MCfit.findChildren(QtWidgets.QLabel),self.mohr_out,1)
		self.update_form(self.Form_rockmass.findChildren(QtWidgets.QLabel),self.rockmass_out,1)

		ut.plot_HB(self,self.HB_in, self.HB_out, self.rockmass_out,self.mohr_out,self.graph_opt)
		ut.plot_MC_circle(self,self.fail_in,self.mohr_out)
	#self.update_forms(forms_opt_list)

	#@profile
	def value_changefail(self,method, name, text):

		# if self.inQueue.not_empty:
		# 	try:
		# 		self.consoleWindow.append(self.inQueue.get_nowait())
		# 	except:
		# 		True

		self.fail_in[name] = float(text)

		self.HB_out = ut.calc_HB(self.HB_in)

		self.rockmass_out = ut.calc_rockm(self.HB_in,self.HB_out)
		if method == 'tunnel':
			self.fail_in['value_s3max'] = 0.47*power(self.rockmass_out['value_scm']/(self.fail_in['value_gamma']*self.fail_in['value_H']),-0.94)*self.rockmass_out['value_scm']
		elif method == 'slope':
			self.fail_in['value_s3max'] = 0.72*power(self.rockmass_out['value_scm']/(self.fail_in['value_gamma']*self.fail_in['value_H']),-0.91)*self.rockmass_out['value_scm']
		elif method == 'general':
			self.fail_in['value_s3max'] = self.HB_in['value_sci']/4
		elif method == 'custom':
			self.fail_in['value_s3max'] = float(text)

		self.mohr_out = ut.calc_MC(self.HB_in,self.fail_in,self.HB_out)

		self.update_form(self.HB_class.findChildren(QtWidgets.QLineEdit),self.HB_in)
		self.update_form(self.fenv.findChildren(QtWidgets.QLineEdit),self.fail_in,1)
		self.update_form(self.form_HBcrit.findChildren(QtWidgets.QLabel),self.HB_out,1)
		self.update_form(self.Form_MCfit.findChildren(QtWidgets.QLabel),self.mohr_out,1)
		self.update_form(self.Form_rockmass.findChildren(QtWidgets.QLabel),self.rockmass_out,1)

		ut.plot_HB(self,self.HB_in, self.HB_out, self.rockmass_out,self.mohr_out,self.graph_opt)
		ut.plot_MC_circle(self,self.fail_in,self.mohr_out)
		#self.update_forms(forms_opt_list)



	#@profile
	def check_change(self,name,value):

		if name == 'calc_MR':
			if value:

				self.calc_Ei.setChecked(False)
				self.value_Ei.setEnabled(False)
				self.value_MR.setEnabled(True)
			else:
				self.calc_Ei.setChecked(True)
				self.value_Ei.setEnabled(True)
				self.value_MR.setEnabled(False)

		elif name== 'calc_Ei':
			if value:
				self.calc_MR.setChecked(False) #we don't need to change the state of value because it's taken care of the calc_MR state change

			else:
				self.calc_MR.setChecked(True)

	#@profile
	def value_changegraph(self,name,text):
		#
		# if self.inQueue.not_empty:
		# 	try:
		# 		self.consoleWindow.append(self.inQueue.get_nowait())
		# 	except:
		# 		True

		self.HB_out = ut.calc_HB(self.HB_in)
		self.mohr_out = ut.calc_MC(self.HB_in,self.fail_in,self.HB_out)
		self.rockmass_out = ut.calc_rockm(self.HB_in,self.HB_out)
		self.graph_opt[name] = text.replace(',','.')
		ut.plot_HB(self,self.HB_in, self.HB_out, self.rockmass_out,self.mohr_out,self.graph_opt)

	#@profile
	def options_check(self,name,value):

		# if self.inQueue.not_empty:
		# 	try:
		# 		self.consoleWindow.append(self.inQueue.get_nowait())
		# 	except:
		# 		True

		self.HB_out = ut.calc_HB(self.HB_in)
		self.mohr_out = ut.calc_MC(self.HB_in,self.fail_in,self.HB_out)
		self.rockmass_out = ut.calc_rockm(self.HB_in,self.HB_out)

		self.graph_opt[name] = value
		ut.plot_HB(self,self.HB_in, self.HB_out, self.rockmass_out,self.mohr_out,self.graph_opt)

	#@profile
	def value_appl_change(self,name,text):

		# if self.inQueue.not_empty:
		# 	try:
		# 		self.consoleWindow.append(self.inQueue.get_nowait())
		# 	except:
		# 		True

		self.fail_in[name] = text

		self.HB_out = ut.calc_HB(self.HB_in)
		self.rockmass_out = ut.calc_rockm(self.HB_in,self.HB_out)
		if text == 'general':
			self.value_gamma.setEnabled(False)
			self.value_H.setEnabled(False)
			self.value_s3max.setEnabled(False)
			self.fail_in['value_s3max'] = self.HB_in['value_sci']/4

		elif text == 'tunnel':
			self.value_gamma.setEnabled(True)
			self.value_H.setEnabled(True)
			self.value_s3max.setEnabled(False)
			self.fail_in['value_s3max'] = 0.47*power(self.rockmass_out['value_scm']/(self.fail_in['value_gamma']*self.fail_in['value_H']),-0.94)*self.rockmass_out['value_scm']
		elif text == 'slope':
			self.value_gamma.setEnabled(True)
			self.value_H.setEnabled(True)
			self.value_s3max.setEnabled(False)
			self.fail_in['value_s3max'] = 0.72*power(self.rockmass_out['value_scm']/(self.fail_in['value_gamma']*self.fail_in['value_H']),-0.91)*self.rockmass_out['value_scm']
		elif text == 'custom':
			self.value_gamma.setEnabled(False)
			self.value_H.setEnabled(False)
			self.value_s3max.setEnabled(True)
			self.fail_in['value_s3max'] = float(self.value_s3max.text())

		self.mohr_out = ut.calc_MC(self.HB_in,self.fail_in,self.HB_out)
		self.update_form(self.HB_class.findChildren(QtWidgets.QLineEdit),self.HB_in)
		self.update_form(self.fenv.findChildren(QtWidgets.QLineEdit),self.fail_in,1)

		self.update_form(self.form_HBcrit.findChildren(QtWidgets.QLabel),self.HB_out,1)
		self.update_form(self.Form_MCfit.findChildren(QtWidgets.QLabel),self.mohr_out,1)
		self.update_form(self.Form_rockmass.findChildren(QtWidgets.QLabel),self.rockmass_out,1)

		ut.plot_HB(self,self.HB_in, self.HB_out, self.rockmass_out,self.mohr_out,self.graph_opt)
		ut.plot_MC_circle(self,self.fail_in,self.mohr_out)
		#self.update_forms(forms_opt_list)

	def update_form(self,form,read_dict,approx=0): #function used to update different entries (e.g mb or E_i)

		# if self.inQueue.not_empty:
		# try:
		# 	self.consoleWindow.append(self.inQueue.get_nowait())
		# except:
		# 	True

		for child in form:
			string = child.objectName()
			if 'value_' in string:
				child.clear()

				if approx:
					child.setText(str(round(read_dict[string],3)))
				else:
					child.setText(str(read_dict[string]))

	#@profile
	# def updateGui(self):
	# 	if self.inQueue.not_empty:
	# 		try:
	# 			self.consoleWindow.append(self.inQueue.get_nowait())
	# 		except:
	# 			True
