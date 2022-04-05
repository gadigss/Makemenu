import maya.cmds as mc
import maya.mel as mel
'''
1.Write a script for listing out all the controls with control name starts with 'Fk' inside a group 
named 'CharGroup', must use maya commands like listRelatives and listConnections?
solution ------------------------------------------
it is assumed that no namespaces are there in scene 
'''

def select_Fk_ctrls():
    # select the group named as CharGroup if it exists in scene
    fk_curves = []
    if mc.objExists('CharGroup'):
        grp_childs = mc.listRelatives('CharGroup', ad=True)
        for crv in grp_childs:
            crv_shp = mc.listRelatives(crv, s=True)
            if crv_shp and crv_shp is not None:
                if crv.startswith('Fk'):
                    print('Fk crv --', crv)
                    fk_curves.append(crv)
    else:
        print('group named as "CharGroup" not exists')
    mc.select(cl=True)
    mc.select(fk_curves)
    return fk_curves

# uncomment the below line to run from maya script editor
# Fkcs = select_Fk_ctrls()




