import maya.cmds as mc
import maya.mel as mel
import maya.utils as utils


def main():
    from GG_Menu import GGT_menu
    GGT_menu()
utils.executeDeferred(main)
