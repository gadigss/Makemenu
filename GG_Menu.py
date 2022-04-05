from glob import glob
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import maya.cmds as mc
import maya.mel as mel
import maya.OpenMayaUI as omui



def selectFkCtrls(*args):
    import Fk_ctrls
    Fk_ctrls.select_Fk_ctrls()

def prefixHkCtrls(*args):
    import Hk_ctrls
    Hk_ctrls.prefix_Hk_ctrls()

def createDirsTool(*args):
    from CDT import CreateDirsTool
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)
    app = QApplication.instance()
    wdg = QMainWindow(parent=mayaMainWindow)
    pbw = CreateDirsTool()
    wdg.setWindowTitle(pbw.windowTitle())
    wdg.setCentralWidget(pbw)
    wdg.show()

def changeTexToHigh(*args):
    import change_high_tex
    change_high_tex.changeToHighTex()

def exportBgGeos(*args):
    import BG_Export
    BG_Export.bg_Export()

def xGenASNExport(*args):
    import export_to_astd
    export_to_astd.export_Sel_To_ArStdn()

MainMenuName = 'GG_Test'

def GGT_menu():
    if mc.menu(MainMenuName, ex=True, p='MayaWindow'):
        mc.deleteUI(MainMenuName)
    parent_menu = mc.menu(MainMenuName, p='MayaWindow')
    mc.menuItem('Select Fk Ctrls', c=selectFkCtrls, p=MainMenuName)
    mc.menuItem('Prefix Hk Ctrls', c=prefixHkCtrls, p=MainMenuName)
    mc.menuItem('Create Directories', c=createDirsTool, p=MainMenuName)
    mc.menuItem('Change Tex To High', c=changeTexToHigh, p=MainMenuName)
    mc.menuItem('Export BG Geos', c=exportBgGeos, p=MainMenuName)
    mc.menuItem('Xgen TO Arnold StandIn', c=xGenASNExport, p=MainMenuName)
