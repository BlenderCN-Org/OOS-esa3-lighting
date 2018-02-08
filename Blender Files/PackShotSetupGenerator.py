bl_info = {
    "name": "Packshot Setup Generator",
    "category": "Lighting",
}

import bpy

class PackshotSetupGenerator(bpy.types.Operator):
    bl_idname = "wm.packshot_setup_generator"
    bl_label = "Packshot Setup Generator"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        #make the sides
        bpy.ops.object.lamp_add(type='AREA', radius=1, view_align=False, location=(0, -10, 2.3), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.object.data.distance = 15
        bpy.context.object.data.energy = 0.2
        bpy.context.object.data.color = (1, 0.828055, 0.649111)

        bpy.ops.object.lamp_add(type='AREA', radius=1, view_align=False, location=(0, 10, 2.3), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.object.data.distance = 15
        bpy.context.object.data.energy = 0.2
        bpy.context.object.data.color = (1, 0.828055, 0.649111)

        #make the backlight
        bpy.ops.object.lamp_add(type='AREA', radius=1, view_align=False, location=(-6, 0, 8), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.object.data.distance = 15
        bpy.context.object.data.energy = 0.15
        bpy.context.object.data.color = (1, 0.828055, 0.649111)

        #make some accents
        bpy.ops.object.lamp_add(type='SPOT', view_align=False, location=(5, 3, 5), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.object.data.distance = 15
        bpy.context.object.data.energy = 0.15
        bpy.context.object.data.color = (1, 0.828055, 0.649111)
        
        return {'FINISHED'}

def register():    
    bpy.utils.register_class(PackshotSetupGenerator)
    
def unregister():
    bpy.utils.unregister_class(PackshotSetupGenerator)
    
if __name__ == "__main__":
    register()            