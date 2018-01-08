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
        layout.operator("object.switchoffalllamps_operator", text = "Switch Off All Lamps")
        layout.operator("brightness.operator", text = "Change Luminosity")
        
        
        
class BrightnessOperator(bpy.types.Operator):
    bl_idname = "brightness.operator"
    bl_label = "Set Luminosity"
    brightnessValue = bpy.props.IntProperty(name="Luminosity", description ="the actual brightness", default = 555, min = 10)
    
    def execute(self,context):
        self.report({'INFO'}, str(self.brightnessValue))
        SetLampStrength(context, int(self.brightnessValue))
        return{'FINISHED'}
    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self,"brightnessValue")

# operator for button
class SelectAllLampsOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.lamp_selection_operator"
    bl_label = "Simple Lamp Selection Operator"

    def execute(self, context):
        SelectAllLamps(context)
        return {'FINISHED'}
    
class SwitchOffAllLampsOperator(bpy.types.Operator):
    bl_idname = "object.switchoffalllamps_operator"
    bl_label = "Simple Lamp Switch Off Operator"
    
    def execute(self, context):
        SetLampStrength(context, 0)
        return {'FINISHED'}
    
    

def SetLampStrength(context, lampStrength):
    helligkeit = lampStrength
    sce = bpy.context.scene
    for object in sce.objects:
        if object.type == "LAMP":
            bpy.data.lamps[object.name].node_tree.nodes["Emission"].inputs[1].default_value = helligkeit

    
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
    bpy.utils.register_class(SwitchOffAllLampsOperator)
    bpy.utils.register_class(BrightnessOperator)


def unregister():
    bpy.utils.unregister_class(LampAdjustPanel)
    bpy.utils.unregister_class(SelectAllLampsOperator)
    bpy.utils.unregister_class(SwitchOffAllLampsOperator)
    bpy.utils.unregister_class(BrightnessOperator)


if __name__ == "__main__":
    register()
    # seems to be needed (?)
    # bpy.ops.object.simple_operator()
    