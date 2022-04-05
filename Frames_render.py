import os, sys
from glob import glob
import maya.cmds as mc
import maya.mel as mel
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance


class FrameRenderTool(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.setWindowTitle("Frame Render Tool")
        self.make_layouts()
        self.go_btn = QPushButton("Render Frames")
        self.label_st = QLabel()
        self.label_ef = QLabel()
        self.label_st.setObjectName(u"label_st")
        self.label_ef.setObjectName(u"label_ef")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_st.setFont(font)
        self.label_ef.setFont(font)
        self.label_st.setText("Start Frame")
        self.label_ef.setText("End Frame")
        self.go_btn.setFont(font)
        self.sf_box = QSpinBox()
        self.ef_box = QSpinBox()
        self.sf_box.setMaximum(5000)
        self.ef_box.setMaximum(5000)

        self.add_layouts()
        self.add_widgets()
        self.setLayout(self.main_lay)
        self.set_signals()
        self.setFixedHeight(200)
        self.setFixedWidth(300)
        self.show()

    def make_layouts(self):
        self.main_lay = QVBoxLayout()
        self.lbl_lat = QHBoxLayout()
        self.spn_lay = QHBoxLayout()

    def add_layouts(self):
        self.main_lay.addLayout(self.lbl_lat)
        self.main_lay.addLayout(self.spn_lay)

    def add_widgets(self):
        self.spn_lay.addWidget(self.label_st)
        self.spn_lay.addWidget(self.sf_box)
        self.spn_lay.addWidget(self.label_ef)
        self.spn_lay.addWidget(self.ef_box)
        self.main_lay.addWidget(self.go_btn)

    def set_signals(self):
        self.go_btn.clicked.connect(self.frame_Render)

    def frame_Render(self):
        print 'clicked Go'
        startFrom = self.sf_box.value()
        renderTill = self.ef_box.value()
        print 'startFrom---- ', startFrom
        print 'renderTill--- ', renderTill

        if startFrom < renderTill:

            mel.eval('currentTime %s ;' % (startFrom))
            while (startFrom < renderTill):
                mel.eval('renderWindowRender redoPreviousRender renderView;')
                startFrom += 1
                mel.eval('currentTime %s ;' % (startFrom))
        else:
            print 'start frame should be less than end frame--'


# uncomment the below lines to run from maya script editor

# from shiboken2 import wrapInstance
#
# mayaMainWindowPtr = omui.MQtUtil.mainWindow()
# mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)
# app = QApplication.instance()
# wdg = QMainWindow(parent=mayaMainWindow)
# pbw = FrameRenderTool()
# wdg.setWindowTitle(pbw.windowTitle())
# wdg.setCentralWidget(pbw)
# wdg.show()
