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
        layout.operator("colour.operator", text = "Change Colour")
        
class ColourOperator(bpy.types.Operator):
    bl_idname = "colour.operator"
    bl_label = "Set Colour in Red, Green, Blue"
    redValue = bpy.props.IntProperty(name="Red", description ="Red Proportion", max = 255, min = 0)
    greenValue = bpy.props.IntProperty(name="Green", description ="Green Proportion", max = 255, min = 0)
    blueValue = bpy.props.IntProperty(name="Blue", description ="Blue Proportion", max = 255, min = 0)
    
    def execute(self,context):
        SetColour(int(self.redValue), int(self.greenValue), int(self.blueValue))
        return{'FINISHED'}
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self,"redValue")
        col.prop(self,"greenValue")
        col.prop(self,"blueValue")        
        
class BrightnessOperator(bpy.types.Operator):
    bl_idname = "brightness.operator"
    bl_label = "Set Luminosity"
    defaultValue = 0
    brightnessValue = bpy.props.IntProperty(name="Luminosity", description ="the actual brightness", min = 10, default = defaultValue) #default remains 0 ? why?
    
    def execute(self,context):
        self.report({'INFO'}, str(self.brightnessValue))
        SetLampStrength(context, int(self.brightnessValue))
        return{'FINISHED'}
    def invoke(self,context,event):
        wm = context.window_manager
        BrightnessOperator.defaultValue = int(GetLampStrength(context.object)) #proof that the value is set correctly
        print (BrightnessOperator.defaultValue) # print proof, still - doesnt work.
        return wm.invoke_props_dialog(self)
    def draw(self, context):
        print(BrightnessOperator.brightnessValue)
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
    
    
    
def SetColour(red, green, blue):
    print(red, green, blue)
    sce = bpy.context.scene
    for object in sce.objects:
        if object.type == "LAMP":
            bpy.data.lamps[object.name].node_tree.nodes["Emission"].inputs[0].default_value = (red, green, blue, 1)

        
def SetLampStrength(context, lampStrength):
    helligkeit = lampStrength
    sce = bpy.context.scene
    for object in sce.objects:
        if object.type == "LAMP":
            bpy.data.lamps[object.name].node_tree.nodes["Emission"].inputs[1].default_value = helligkeit

def GetLampStrength(lamp):
    return bpy.data.lamps[lamp.name].node_tree.nodes["Emission"].inputs[1].default_value

    
# function for operator
def SelectAllLamps(context):
    sce = bpy.context.scene
    for object in sce.objects:
        if object.type != "LAMP":
            object.select = False 
        else:
            object.select = True
        
        
        
def register():
    #bpy.utils.register_class(LampAdjustPanel)
    #bpy.utils.register_class(SelectAllLampsOperator)
    #bpy.utils.register_class(SwitchOffAllLampsOperator)
    #bpy.utils.register_class(BrightnessOperator)
    #bpy.utils.register_class(ColourOperator)
    bpy.utils.register_module(__name__)


def unregister():
    #bpy.utils.unregister_class(LampAdjustPanel)
    #bpy.utils.unregister_class(SelectAllLampsOperator)
    #bpy.utils.unregister_class(SwitchOffAllLampsOperator)
    #bpy.utils.unregister_class(BrightnessOperator)
    #bpy.utils.unregister_class(ColourOperator)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
    # seems to be needed (?)
    # bpy.ops.object.simple_operator()
    