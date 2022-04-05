import os, sys
from glob import glob
import maya.cmds as mc
import maya.mel as mel
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

'''
2. Create a tool as shown in the image below using PySide or PySide2 according to your maya 
version and assign a function to 'Create Folders' button to create folders in the given path with the 
names listed above in list widget?
solution ---------------------------------
hardcoded the list of scenes for which directories are required - ----------
'''


class CreateDirsTool(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.setWindowTitle("Create Directories Tool")
        self.make_layouts()
        self.go_btn = QPushButton("Create Folders")
        self.list_wdg = QListWidget()
        self.list_wdg.setSelectionMode(QAbstractItemView.MultiSelection)
        list_wdg_font = QFont()
        list_wdg_font.setFamily(u"Arial Black")
        list_wdg_font.setPointSize(12)
        list_wdg_font.setBold(True)
        list_wdg_font.setWeight(75)
        self.list_wdg.setFont(list_wdg_font)
        self.src_path = QLineEdit("")
        self.src_path.setPlaceholderText("Enter path to create selected folders")
        src_path_font = QFont()
        src_path_font.setPointSize(10)
        self.src_path.setFont(src_path_font)
        self.go_btn.setFont(src_path_font)
        self.add_layouts()
        self.add_widgets()
        self.setLayout(self.main_lay)
        self.set_signals()
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        self.all_scenes = ['sc00' + str(x) for x in range(1, 10)]
        self.fill_list()
        self.show()

    def make_layouts(self):
        self.main_lay = QVBoxLayout()
        self.list_lay = QHBoxLayout()
        self.path_lay = QHBoxLayout()

    def add_layouts(self):
        self.main_lay.addLayout(self.list_lay)
        self.main_lay.addLayout(self.path_lay)

    def add_widgets(self):
        self.list_lay.addWidget(self.list_wdg)
        self.path_lay.addWidget(self.src_path)
        self.path_lay.addWidget(self.go_btn)

    def set_signals(self):
        self.go_btn.clicked.connect(self.create_dirs)

    def fill_list(self):
        for i in self.all_scenes:
            sc_item = QListWidgetItem()
            sc_item.setText(i)
            self.list_wdg.addItem(sc_item)

    def create_dirs(self):
        print('clicked - go ')
        sel_ref = self.list_wdg.selectedItems()
        sel_refind = self.list_wdg.selectedIndexes()
        all_count = self.list_wdg.count()
        all_indexes = []
        for i in range(all_count):
            all_indexes.append(i)
        sel_items = []
        for r in range(len(sel_refind)):
            sel_item = self.list_wdg.selectedIndexes()[r]
            idx = sel_item.row()
            itex = self.list_wdg.item(idx).text()
            sel_items.append(itex)
        tar_path = self.src_path.text()
        tar_folders = []
        tar_folders_exist = []
        if tar_path and os.path.exists(tar_path):
            tar_path = tar_path.replace('\\', '/')
            print('tar path -- ', tar_path)
            for itm in sel_items:
                tar_dir = '{0}/{1}'.format(tar_path, itm)
                if not os.path.exists(tar_dir):
                    try:
                        os.makedirs(tar_dir)
                        tar_folders.append(tar_dir)
                    except Exception as te:
                        print('check error-- ', te)
                        return
                elif os.path.exists(tar_dir):
                    tar_folders_exist.append(tar_dir)
            if tar_folders_exist:
                print('the following folders already existing ---')
                for fldx in tar_folders_exist:
                    print(fldx)
            if tar_folders:
                print('the following folders created---')
                for fld in tar_folders:
                    print(fld)
            else:
                print('no folders created---')

        else:
            print('path is empy OR given path not exist - check -- ', tar_path)
            return


# uncomment the below lines to run from maya script editor

# from shiboken2 import wrapInstance
#
# mayaMainWindowPtr = omui.MQtUtil.mainWindow()
# mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)
# app = QApplication.instance()
# wdg = QMainWindow(parent=mayaMainWindow)
# pbw = CreateDirsTool()
# wdg.setWindowTitle(pbw.windowTitle())
# wdg.setCentralWidget(pbw)
# wdg.show()
