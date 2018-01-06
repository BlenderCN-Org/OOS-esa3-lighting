import bpy

from bpy.types import Menu, Panel, UIList

class ViewLightningPanel():
    # where the new panel will be accessable
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    
# the new panel
class LampAdjustPanel(ViewLightningPanel, Panel):
    bl_idname = "panel_lampadjust"
    bl_label = "Lamp Adjustment"
    bl_context = "objectmode"
    bl_category = "LMD"
    
    # draw a new button, call operator on click
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        layout.operator("object.lamp_selection_operator", text = "Select All Lamps")

# operator for button
class SelectAllLampsOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.lamp_selection_operator"
    bl_label = "Simple Lamp Selection Operator"

    def execute(self, context):
        SelectAllLamps(context)
        return {'FINISHED'}
    
# function for operator
def SelectAllLamps(context):
    sce = bpy.context.scene
    for object in sce.objects:
        if object.type != "LAMP":
            object.select = False 
        else:
            object.select = True
        
        
        
def register():
    bpy.utils.register_class(LampAdjustPanel)
    bpy.utils.register_class(SelectAllLampsOperator)


def unregister():
    bpy.utils.unregister_class(LampAdjustPanel)
    bpy.utils.unregister_class(SelectAllLampsOperator)


if __name__ == "__main__":
    register()
    # seems to be needed (?)
    bpy.ops.object.simple_operator()
    