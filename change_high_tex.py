import os
import maya.cmds as mc

'''
3. Write a script to change all texture paths from 'low' folder to 'high' folder?
solution ------------------------------
here I am assuming that both low and high texture folders are in same folder with same name and extn
'''

def changeToHighTex():
    tex_files = mc.ls(et='file')
    if tex_files:
        for t_file in tex_files:
            t_path = mc.getAttr(t_file + '.fileTextureName')
            # print t_path
            # -- change the names according the folder structure 
            # -- here I am assuming that both low and high texture folders are in same folder with same name and extn
            high_path = t_path.replace('/low/', '/high/')
            # print (high_path)
            if t_path:
                if os.path.isfile(high_path):
                    try:
                        mc.setAttr(t_file + '.fileTextureName', high_path, typ='string')
                        print ('high tex found changing low to high--')
                        print (high_path)
                    except Exception as te:
                        print ('--error---')
                        print (te)
                        print ('--error---')
                else:
                    print ('high tex not found -- keeping low tex')
                    print(t_path)

    else:
        print ('No tex nodes found----')

# uncomment the below line to run from maya script editor
# changeToHighTex()