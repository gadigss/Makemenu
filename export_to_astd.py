import maya.cmds as mc
import maya.mel as mel
import os
'''
6. Write a script for Exporting selected xgen description as Arnold Stand-in?
solution ---------------------------------------------
exporting with less options which can be determined at production level configuration 
'''
def export_Sel_To_ArStdn():
    sel_xgen_des = []
    n_sel = mc.ls(sl=True)
    if n_sel:
        for sel in n_sel:
            sel_type = mc.nodeType(sel)
            if sel_type == 'xgmDescription':
                sel_xgen_des.append(sel)
            else:
                pass
    else:
        print('Select one or more xgen description to export')
    if sel_xgen_des:
        sc_fl = mc.file(q=True, loc=True)
        sc_dir = os.path.dirname(sc_fl)
        b_name = os.path.basename(sc_fl).replace('.ma', '')
        for xg in sel_xgen_des:
            asdn_path = '{0}/asdn'.format(sc_dir)
            if not os.path.exists(asdn_path):
                os.makedirs(asdn_path)
            asdn_file = '{0}/asdn/{1}_ARStdn.ass'.format(sc_dir, xg)
            try:
                mc.file(asdn_file, f=True, options="-shadowLinks 0;-mask 6399;-lightLinks 0;-boundingBox",
                        typ="ASS Export", pr=True, es=True)
            except Exception as xe:
                print('cannot export --', xg)
                print('check error --', xe)
    if not sel_xgen_des:
        print('Select one or more xgen description to export')

# uncomment the below line to run from maya script editor
# export_Sel_To_ArStdn()
