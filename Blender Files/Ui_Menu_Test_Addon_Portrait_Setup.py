bl_info = {
    "name": "NVoll krasses Menu",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 75, 0),
    # define a keyboard shortcut on which the menu should appear
    "location": "View3D > alt A",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }
    
import bpy

class uiMenuTest(bpy.types.Menu):
    bl_label = "Lighting Setups Menu"
    # the id is important for calling the menu via the shortcut
    # user preferences -> input
    # https://www.youtube.com/watch?v=GD0AiEMTuyY
    bl_idname = "testUiMenu"

    def draw(self, context):
        layout = self.layout
        
        # call menu for single lamps
        layout.operator("wm.call_menu", text="Add Lamp", icon ='LAMP_SPOT').name = "INFO_MT_lamp_add"
        
        # call menu for setups
        layout.operator("wm.call_menu", text="Add Setup", icon ='LAMP_SPOT').name = "INFO_MT_lamp_add"
        
        # stolen from template just for testing
        # use an operator enum property to populate a sub-menu
        layout.operator_menu_enum("object.select_by_type",
                                  property="type",
                                  text="Select All by Type...",
                                  )
def add_portrait_setup():

    #Führung hinzufügen
    bpy.ops.object.lamp_add(type='AREA', radius=1, view_align=False, location=(-    2.75, -2.00, 2.3), layers=(True, False, False, False, False, False, False,      False, False, False, False, False, False, False, False, False, False,           False, False, False))
    #distance
    bpy.context.object.data.distance = 15
    #energy
    bpy.context.object.data.energy = 0.2
    #color
    bpy.context.object.data.color = (1, 0.828055, 0.649111)

    #Aufhellung hinzufügen
    bpy.ops.object.lamp_add(type='AREA', view_align=False, location=(3.11, -        2.02, 1.35), layers=(True, False, False, False, False, False, False, False,     False, False, False, False, False, False, False, False, False, False,           False, False))
    #distance
    bpy.context.object.data.distance = 15
    #energy
    bpy.context.object.data.energy = 0.1
    #color
    bpy.context.object.data.color = (1, 0.828055, 0.649111)

    #Spitze hinzufügen
    bpy.ops.object.lamp_add(type='SPOT', view_align=False, location=(-3.85,         2.44, 2.26), layers=(True, False, False, False, False, False, False, False,     False, False, False, False, False, False, False, False, False, False,           False, False))
    #distance
    bpy.context.object.data.distance = 15
    #energy
    bpy.context.object.data.energy = 0.1
    #color
    bpy.context.object.data.color = (1, 0.828055, 0.649111)
        
def register():
    bpy.utils.register_class(uiMenuTest)

def unregister():
    bpy.utils.unregister_class(uiMenuTest)
    

if __name__ == "__main__":
    register()
    
    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=uiMenuTest.bl_idname)

    # create new portrait setup
    lampData = add_portrait_setup()
