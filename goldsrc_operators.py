from pathlib import Path

import bpy
from bpy.props import StringProperty, CollectionProperty
from .goldsrc.bsp.import_bsp import BSP
from .goldsrc.mdl.import_mdl import import_model


class GBSPImport_OT_operator(bpy.types.Operator):
    """Load GoldSrc BSP"""
    bl_idname = "source_io.gbsp"
    bl_label = "Import GoldSrc BSP file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)
    filter_glob: StringProperty(default="*.bsp", options={'HIDDEN'})

    def execute(self, context):

        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()
        for n, file in enumerate(self.files):
            print(f"Loading {n}/{len(self.files)}")
            bsp = BSP(directory / file.name)
            bsp.load_map()
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

class GMDLImport_OT_operator(bpy.types.Operator):
    """Load GoldSrc MDL"""
    bl_idname = "source_io.gmdl"
    bl_label = "Import GoldSrc MDL file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)
    filter_glob: StringProperty(default="*.mdl", options={'HIDDEN'})

    def execute(self, context):

        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()
        for n, file in enumerate(self.files):
            print(f"Loading {n}/{len(self.files)}")
            import_model(directory / file.name)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}