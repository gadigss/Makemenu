import maya.cmds as mc
import maya.mel as mel
import os

'''
5. Write a script to list out all meshes inside a group named 'BG_rig' , select those meshes and 
export alembic cache for selected meshes?
solution ------------------------------------------
it is assumed that no namespaces are there in scene 
'''


def bg_Export():
    # select the group named as BG_rig if it exists in scene
    ex_geos = []
    if mc.objExists('BG_rig'):
        grp_childs = mc.listRelatives('BG_rig', ad=True)
        for geo in grp_childs:
            geo_shp = mc.listRelatives(geo, s=True)
            if geo_shp and geo_shp is not None:
                if mc.nodeType(geo_shp) == 'mesh':
                    print('bg geos --', geo)
                    ex_geos.append(geo)

        # ----------- export listed geos to alembic-----------
        if ex_geos:
            sc_fl = mc.file(q=True, loc=True)
            sc_dir = os.path.dirname(sc_fl)
            b_name = os.path.basename(sc_fl).replace('.ma', '')
            abc_path = '{0}/abc_cache'.format(sc_dir)
            if not os.path.exists(abc_path):
                os.makedirs(abc_path)

            # --- make sure abc plugin loaded
            if not mc.pluginInfo("AbcExport.mall", l=True, q=True):
                mc.loadPlugin("AbcExport.mall")
            sf = mc.playbackOptions(ast=True, q=True)
            ef = mc.playbackOptions(aet=True, q=True)
            root_str = ''
            for obj in ex_geos:
                root_str += ' -root {} '.format(obj)
            # print ('root_str--',root_str)

            cache_file = '{0}/abc_cache/{1}_BG_geos.abc'.format(sc_dir, b_name)
            mc.AbcExport(
                j="-frameRange {0} {1} -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa {2} -file {3}".format(
                    sf, ef, root_str, cache_file))

        else:
            print('no meshes listed for export')

    else:
        print('group named as "BG_rig" not exists')

    return ex_geos

# uncomment the below line to run from maya script editor
# bgex_geos = bg_Export()




