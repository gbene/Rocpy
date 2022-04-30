from PyQt5.QtGui import QColor,QKeyEvent
from PyQt5.QtCore import QEventLoop, QEvent, Qt, QAbstractTableModel,QCoreApplication
from import_window_ui import Ui_ImportOptionsWindow
from PyQt5.QtWidgets import QListWidgetItem,QApplication,QMainWindow, QFileDialog,QTableWidgetItem,QComboBox,QLineEdit,QHeaderView

from mi_gui import Ui_pickMi
from sci_gui import Ui_sciWindow
import pandas as pd
from difflib import SequenceMatcher
import utils as ut


class miGui(Ui_pickMi):

    def __init__(self,parent=None, *args, **kwargs):
        super(miGui, self).__init__(parent,*args, **kwargs)
        self.setupUi(self)
        self.parent = parent


        rock_list = ['All','Sedimentary','Metamorphic','Igneous']
        texture_list = ['All','Coarse','Medium','Fine','Very fine']

        self.rockCombo.addItems(rock_list)
        self.textureCombo.addItems(texture_list)

        self.rockCombo.activated.connect(self.sel_changed)
        self.textureCombo.activated.connect(self.sel_changed)
        self.miList.itemDoubleClicked.connect(self.sel_item)
        self.buttonBox.accepted.connect(self.sel_mi)
        self.buttonBox.rejected.connect(self.close)


        text_value_dict = {'Coarse':['Conglomerates: 21±3',
                                     'Breccias: 19±5',
                                     'N.a.',
                                     'Crystalline Limestone: 12±3',
                                     'N.a.',
                                     'N.a.',
                                     'Marble: 9±3',
                                     'N.a.',
                                     'Migmatite: 29±3',
                                     'Gneiss: 28±5',
                                     'Granite: 32±3',
                                     'Granodiorite: 29±3',
                                     'Gabbro: 27±3',
                                     'Norite: 20±5',
                                     'Porphyrites: 20±5',
                                     'N.a.',
                                     'N.a.',
                                     'Agglomerate: 19±5 '],
                         'Medium':['Sandstones: 17±4',
                                     'N.a.',
                                     'N.a.',
                                     'Sparitic limestones: 10±2',
                                     'Gypsum: 8±2',
                                     'N.a.',
                                     'Hornfels: 19±4',
                                     'Metasandstones: 19±3',
                                     'Amphibolites: 26±6',
                                     'Schists: 12±3',
                                     'Diorite: 25±5',
                                     'N.a.',
                                     'Dolerite: 16±5',
                                     'N.a.',
                                     'N.a.',
                                     'Rhyolite: 25±5',
                                     'Andesite: 25±5',
                                     'Breccia: 19±5'],
                            'Fine':['Siltstones: 7±2',
                                        'Graywakes: 18±3',
                                        'N.a.',
                                        'Micritic Limestones: 9±2',
                                        'Anhydrite: 12±2',
                                        'N.a.',
                                        'Quarzites: 20±3',
                                        'N.a.',
                                        'N.a.',
                                        'Phyllites: 7±3',
                                        'N.a.',
                                        'N.a.',
                                        'N.a.',
                                        'N.a.',
                                        'Diabase: 15±5',
                                        'Dacite: 25±3',
                                        'Basalt: 25±5',
                                        'Tuff: 13±5'],
                            'Very fine':['Claystones: 4±2',
                                        'Shales: 6±2',
                                        'Marls: 7±2',
                                        'Dolomites: 9±3',
                                        'N.a.',
                                        'Chalk: 7±2',
                                        'N.a.',
                                        'N.a.',
                                        'N.a.',
                                        'Slates: 7±4',
                                        'N.a.',
                                        'N.a.',
                                        'N.a.',
                                        'N.a.',
                                        'Peridotite: 25±5',
                                        'Obsidian: 19±3',
                                        'N.a.',
                                        'N.a.']}
        index = ['Sedimentary',
                 'Sedimentary',
                 'Sedimentary',
                 'Sedimentary',
                 'Sedimentary',
                 'Sedimentary',
                 'Metamorphic',
                 'Metamorphic',
                 'Metamorphic',
                 'Metamorphic',
                 'Igneous',
                 'Igneous',
                 'Igneous',
                 'Igneous',
                 'Igneous',
                 'Igneous',
                 'Igneous',
                 'Igneous']

        # value_dict = {'Conglomerates': 21,
        #               'Breccias': 19,
        #               'Crystalline Limestone': 12,
        #               'Marble': 9,
        #               'Migmatite': 29,
        #               'Gneiss': 28,
        #               'Granite': 32,
        #               'Granodiorite': 29,
        #               'Gabbro': 27,
        #               'Norite': 20,
        #               'Porphyrites': 20,
        #               'Agglomerate': 19,
        #               'Sandstones': 17,
        #               'Sparitic limestones': 10,
        #               'Gypsum': 8,
        #               'Hornfels': 19,
        #               'Metasandstones': 19,
        #               'Amphibolites': 26,
        #               'Schists': 12,
        #               'Diorite': 25,
        #               'Dolerite': 16,
        #               'Rhyolite': 25,
        #               'Andesite': 25,
        #               'Breccia': 19,
        #               'Siltstones': 7,
        #               'Graywakes': 18,
        #               'Micritic Limestones': 9,
        #               'Anhydrite': 12,
        #               'Quarzites': 20,
        #               'Phyllites': 7,
        #               'Diabase': 15,
        #               'Dacite': 25,
        #               'Basalt': 25,
        #               'Tuff': 13,
        #               'Claystones': 4,
        #               'Shales': 6,
        #               'Marls': 7,
        #               'Dolomites': 9,
        #               'Chalk': 7,
        #               'Slates': 7,
        #               'Peridotite': 25,
        #               'Obsidian': 19}

        self.text_values_df = pd.DataFrame(text_value_dict,index=index)
        # self.text_values_df_filt = self.text_values_df
        self.compile_list(self.text_values_df)

        self.show()

    def compile_list(self,values_df):
        self.miList.clear()
        for i in values_df.to_numpy().flatten():
            if i != 'N.a.':
                QListWidgetItem(i,self.miList)

    def sel_changed(self):

        type_rock = self.rockCombo.currentText()
        type_texture = self.textureCombo.currentText()


        if type_rock == 'All' and type_texture!= 'All':
            text_values_df_filt = self.text_values_df.loc[:,type_texture]
        elif type_texture == 'All' and type_rock != 'All':
            text_values_df_filt = self.text_values_df.loc[type_rock,:]
        elif type_rock == 'All' and type_texture == 'All':
            text_values_df_filt = self.text_values_df
        else:
            text_values_df_filt = self.text_values_df.loc[type_rock,type_texture]

        self.compile_list(text_values_df_filt)

    def sel_item(self):
        sel_line = self.miList.currentItem().text()
        value = sel_line.split(':')[1].split('±')[0].strip()
        self.miBox.setText(value)
        # print()

    def sel_mi(self):
        value = self.miBox.toPlainText()
        if value != '':
            self.parent.HB_in['value_mi'] = float(value)
            self.parent.value_mi.setText(value)
            self.parent.value_mi.setFocus()
            return_event = QKeyEvent(
                                QEvent.KeyPress,
                                Qt.Key_Return,
                                Qt.NoModifier
                            )
            QCoreApplication.postEvent(self.parent.value_mi,return_event)
            # print(self.parent.HB_in)

class sciGui(Ui_sciWindow):
    def __init__(self,parent=None, *args, **kwargs):
        super(sciGui, self).__init__(parent,*args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.Button250.clicked.connect(lambda: self.update_spin(250))
        self.Button100.clicked.connect(lambda: self.update_spin(175))
        self.Button50.clicked.connect(lambda: self.update_spin(75))
        self.Button25.clicked.connect(lambda: self.update_spin(35))
        self.Button5.clicked.connect(lambda: self.update_spin(15))
        self.Button1.clicked.connect(lambda: self.update_spin(3))
        self.Button025.clicked.connect(lambda: self.update_spin(0.625))

        self.sciButtonBox.accepted.connect(self.sel_sci)
        self.sciButtonBox.rejected.connect(self.close)

        self.show()

    def update_spin(self,value):
        self.sciBox.setValue(value)

    def sel_sci(self):
        value = self.sciBox.value()
        if value != '':
            self.parent.HB_in['value_sci'] = value
            self.parent.value_sci.setText(str(value))
            self.parent.value_sci.setFocus()
            return_event = QKeyEvent(
                                QEvent.KeyPress,
                                Qt.Key_Return,
                                Qt.NoModifier
                            )
            QCoreApplication.postEvent(self.parent.value_sci,return_event)

class DataModel(QAbstractTableModel):
    '''[Gabriele]  Abstract table model that can be used to quickly display imported pc files data  from a pandas df. Taken from this stack overflow post https://stackoverflow.com/questions/31475965/fastest-way-to-populate-qtableview-from-pandas-data-frame
    '''

    def __init__(self, data, index_list, parent=None, *args, **kwargs):
        super(DataModel, self).__init__(*args, **kwargs)

        self.data = data
        self.index_list = index_list

    def columnCount(self, parent=None):  # [Gabriele] the n of columns is = to the number of columns of the input data set (.shape[1])
        return self.data.shape[1]

    def rowCount(self, parent=None):  # [Gabriele] the n of rows is = to the number of rows of the input data set (.shape[0])
        return self.data.shape[0]

    def data(self, index, role):
        # print(index.column())
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.data.iloc[index.row(), index.column()])  # if role == Qt.BackgroundRole and index.column() in self.index_list:  # return QColor(Qt.green)
            if role == Qt.BackgroundRole and index.column() in self.index_list:
                return QColor(Qt.green)  # [Gabriele] Set the color
        return None

    '''[Gabriele] Set header and index If the "container" is horizontal (orientation index 1) and has a display role (index 0) (-> is the header of the table). If the "container" is vertical (orientation index 2) and has a display role (index 0) (-> is the index of the table).'''

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return str(self.data.columns[col])  # [Gabriele] Set the header names
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self.data.index[col]  # [Gabriele] Set the indexes
        return None


class import_dialog(QMainWindow,Ui_ImportOptionsWindow):
    '''[Gabriele]  New window class used to display import options and data preview.
    '''

    '''[Gabriele]  Different options that can be changed in the import menu:
        + in_path -> input file path
        + StartRowspinBox -> Start import from row number
        + EndRowspinBox -> End import on row number
        + Separator -> Type of separtor in the data set'''

    import_options_dict = {'in_path': '', 'StartRowspinBox': 0, 'EndRowspinBox': 100, 'SeparatorcomboBox': ' '}

    '''[Gabriele]  Different types of separators. By writing not using the symbol as a display we can avoid possible confusion between similar separators (e.g tab and space)-> now the separator is auto assigned with the auto_sep function'''

    sep_dict = {'<space>': ' ', '<comma>': ',', '<semi-col>': ';', '<tab>': '   '}

    def __init__(self,parent=None, *args, **kwargs):
        super(import_dialog, self).__init__(parent,*args, **kwargs)
        self.setupUi(self)
        self.parent = parent
        self.action = self.sender()  # [Gabriele] Name of the actionmenu from which the import function was called.

        self.args = []

        '''[Gabriele]  To generalize the import menu we can use the import_func_dict that has keys that correspond to the action name (eg actionImportPC) and items to the function (eg import_PC). If a new action needs to use this interface we can add to the dict the object name of the action and add a new function. This gives more flexibility in the importers output since it doesn't depend on a single function.

        To add a new import function (e.g. import_PC -> pc2vtk) add the function in this class and add it to the import_func_dict with this template:
            NameOfActionMenu: self.import_func()'''

        self.import_func_dict = {'actionImport_HB_data': self.import_HB}


        '''[Gabriele]  Different types of signals depending on the field in the import options'''
        self.PathtoolButton.clicked.connect(lambda: self.import_file())
        self.PathlineEdit.editingFinished.connect(lambda: self.import_file(path=self.PathlineEdit.text()))

        self.StartRowspinBox.valueChanged.connect(lambda: self.import_options(self.StartRowspinBox.objectName(), self.StartRowspinBox.value()))

        self.EndRowspinBox.valueChanged.connect(lambda: self.import_options(self.EndRowspinBox.objectName(), self.EndRowspinBox.value()))

        ''' [Gabriele] The text separator value is confronted with the dict values and then assigned the correct symbol. <comma> --> ","'''

        self.SeparatorcomboBox.currentTextChanged.connect(lambda: self.import_options(self.SeparatorcomboBox.objectName(), self.sep_dict[self.SeparatorcomboBox.currentText()]))

        self.PreviewButton.clicked.connect(lambda: self.preview_file(self.input_data_df))

        self.ConfirmBox.accepted.connect(self.import_func_dict[self.action.objectName()])
        self.ConfirmBox.rejected.connect(self.close)

        self.AssignTable.setColumnCount(2)
        self.AssignTable.setHorizontalHeaderLabels(['Column name', 'Property name'])
        self.AssignTable.setColumnWidth(1, 200)

        self.show_qt_canvas()

    def import_options(self, origin, value):
        '''[Gabriele]  Single function that manages all of the signals by adding to the import_options_dict a key,value pair corresponding to the origin object name and the set value.'''
        self.import_options_dict[origin] = value

    def show_qt_canvas(self):
        """Show the Qt Window"""
        self.show()

    def import_file(self, path=None):
        '''[Gabriele] Function used to read and preview a PC data file. The open_file_dialog function is used to obtain the file path. Once the file is chosen a different parser is used depending on the extension. Once the file is read the properties are autoassigned (where possible)'''
        if path == None:
            self.import_options_dict['in_path'] = open_file_dialog(parent=self, caption='Import point cloud data', filter="All supported (*.txt *.csv );; Text files (*.txt);; CSV files (*.csv)")
            self.PathlineEdit.setText(self.import_options_dict['in_path'])
        else:
            self.import_options_dict['in_path'] = path

        try:

            self.input_data_df = self.csv2df(self.import_options_dict['in_path'])

            self.default_attr_list = ['sci', 'mi', 'GSI', 'D', 'Ei', 'MR', 'application', 'gamma', 'H', 's3max', 'N.a.']

            '''[Gabriele]  Auto-assign values using the difflib library (internal). If there is no match then the column is not imported (N.a.). In this step the rename_dict dictionary is compiled where:
            - the keys correspond to the column index of the input df
            - the items correspond to the matched attribute (match score >0.8).
            If there is no match, the item will correspond to the original input column name.

            This dict is then used in the assign_data menu window to fill the corresponding values in each comboBox.
            '''

            col_names = list(self.input_data_df.columns)
            self.rename_dict = {}

            remove_char_dict = {"/": "", "\\": "", "?": "", "!": "", "-": "","_":""}  # [Gabriele] Forbidden characters that are removed from the names using the translate function

            for i, attr in enumerate(col_names):
                table = attr.maketrans(remove_char_dict)
                matches = [SequenceMatcher(None, attr.translate(table).lower(), string.lower()).ratio() for string in self.default_attr_list]
                match = max(matches)

                if match > 0.8:
                    index = matches.index(match)
                    self.rename_dict[i] = self.default_attr_list[index]
                else:
                    self.rename_dict[i] = 'N.a.'
            self.assign_data()  # [Gabriele] Open the assign data ui.
        except ValueError:
            print('Could not preview: invalid column, row or separator')
        except FileNotFoundError:
            print('Could not import: invalid file name')
            # [Gabriele] This clears the AssingTable and dataView table
            self.AssignTable.setRowCount(0)
            self.dataView.setModel(None)

    def preview_file(self, input_data_df):
        '''[Gabriele]  Function used to preview the data using the DataModel. The column and row ranges are obtained to properly slice the preview table.'''
        value_dict = {k: v for k, v in list(self.rename_dict.items()) if v != 'N.a.'}
        index_list = list(value_dict.keys())
        self.model = DataModel(self.input_data_df, index_list)
        self.dataView.setModel(self.model)

    def import_HB(self):

        clean_dict = {k: v for k, v in list(self.rename_dict.items()) if v != 'N.a.'}
        for key,name in clean_dict.items():
                dict_key = f'value_{name}'
                if dict_key == 'value_Ei':
                    print('ciao')
                    self.parent.calc_Ei.setChecked(True)
                elif dict_key == 'value_application':
                    value = self.input_data_df.iloc[0,key]
                    index = self.parent.value_application.findText(value)
                    self.parent.value_application.setCurrentIndex(index)

                else:
                    value = float(self.input_data_df.iloc[:,key])
                    if dict_key in self.parent.HB_in:
                        self.parent.HB_in[dict_key] = value
                    elif dict_key in self.parent.fail_in:
                        self.parent.fail_in[dict_key] = value
                    combo = getattr(self.parent,dict_key)
                    combo.setText(str(value))
                    combo.setFocus()
                    return_event = QKeyEvent(
                                        QEvent.KeyPress,
                                        Qt.Key_Return,
                                        Qt.NoModifier
                                    )
                    QCoreApplication.postEvent(combo,return_event)


    def csv2df(self, path):
        '''[Gabriele]  csv file parser.
        It reads the specified csv file using pd_read_csv. Wrapped in a function so that it can be profiled.
        --------------------------------------------------------
        Inputs:
        - csv file path

        Outputs:
        - Pandas df
        --------------------------------------------------------

        '''
        sep = ut.auto_sep(path)
        self.SeparatorcomboBox.setCurrentIndex(list(self.sep_dict.values()).index(sep))
        df = pd.read_csv(path, sep=sep, engine='c', index_col=False)
        return df


    def assign_data(self):

        df = self.input_data_df
        col_names = list(df.columns)
        LineList = []

        self.AssignTable.setRowCount(len(col_names))

        for i, col in enumerate(col_names):
            '''[Gabriele]  To create the assign menu we cicle through the column names and assign the comboBox text to the corresponding rename_dict item if the item is contained in the default_attr_list'''
            self.ColnameItem = QTableWidgetItem()
            self.ColnameItem.setText(str(col_names[i]))
            self.AttrcomboBox = QComboBox(self)
            self.AttrcomboBox.setObjectName(f'AttrcomboBox{i}')
            self.AttrcomboBox.setEditable(False)
            self.AttrcomboBox.addItems(self.default_attr_list)
            self.AttrcomboBox.activated.connect(lambda: ass_value())
            self.AssignTable.setItem(i, 0, self.ColnameItem)
            self.AssignTable.setCellWidget(i, 1, self.AttrcomboBox)

            self.AssignTable.cellWidget(i, 1).setCurrentText(self.rename_dict[i])

            self.AssignTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # self.resize(750, 600) #[Gabriele] Set appropriate window size

        def ass_value():

            '''[Gabriele] Get column and row of clicked widget in table '''

            clicked = QApplication.focusWidget().pos()
            index = self.AssignTable.indexAt(clicked)
            col = index.column()
            row = index.row()
            sel_combo = self.AssignTable.cellWidget(row, col)  # [Gabriele] Combobox @ row and column

            '''[Gabriele] Use a dict to rename the columns. The keys are the column index of the original df while the values are the new names. '''


            items = list(self.rename_dict.values())
            if sel_combo.currentText() in items and sel_combo.currentText() != 'N.a.':
                print('Item already assigned')
            else:
                self.rename_dict[row] = sel_combo.currentText()
            self.preview_file(self.input_data_df)


    def close_ui(self):
        self.close()
        self.loop.quit()

def open_file_dialog(parent=None, caption=None, filter=None, multiple=False):
    """Open a dialog and input a file or folder name.
    If the dialog is closed without a valid file name, it returns None."""
    if multiple:
        in_file_name = QFileDialog.getOpenFileNames(parent=parent, caption=caption, filter=filter)
        in_file_name = in_file_name[0]
    else:
        in_file_name = QFileDialog.getOpenFileName(parent=parent, caption=caption, filter=filter)
        in_file_name = in_file_name[0]
    return in_file_name
