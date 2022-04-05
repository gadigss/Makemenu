import maya.cmds as mc
import maya.mel as mel

'''
4. Write a script to find all controls in which each control name starts with 'Hk' and ends with '_L' 
and add a prefix 'Ctrl_' to all listed controls ?
solution --------------------------------------
it is assumed that no namespaces are there in scene 
'''

def prefix_Hk_ctrls():
    # list all curves in scene
    hk_curves = []
    all_crvs = mc.ls(et='nurbsCurve')
    mc.select(cl=True)
    for crv in all_crvs:
        crvt = mc.listRelatives(crv, p=True)
        if crvt and crvt is not None:
            if crvt[0].startswith('Hk') and crvt[0].endswith('_L'):
                crvt1 = crvt[0].replace('Hk', 'Ctrl_Hk')
                mc.rename(crvt[0],crvt1)
                print ('prefixed ',crvt[0],' to ',crvt1)
                hk_curves.append(crvt1)

    return hk_curves

# uncomment the below line to run from maya script editor
# Hkcs = prefix_Hk_ctrls()