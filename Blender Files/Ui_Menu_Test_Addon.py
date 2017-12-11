bl_info = {
    "name": "NVoll krasses Menu",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > alt A",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }
    
import bpy

class uiMenuTest(bpy.types.Menu):
    bl_label = "Voll krasses Menu"
    bl_idname = "testUiMenu"

    def draw(self, context):
        layout = self.layout
        
        # call another menu
        layout.operator("wm.call_menu", text="Add Lamp", icon ='LAMP_SPOT').name = "INFO_MT_lamp_add"
        
        # stolen from template just for testing
        # use an operator enum property to populate a sub-menu
        layout.operator_menu_enum("object.select_by_type",
                                  property="type",
                                  text="Select All by Type...",
                                  )
        
        
def register():
    bpy.utils.register_class(uiMenuTest)

def unregister():
    bpy.utils.unregister_class(uiMenuTest)
    

if __name__ == "__main__":
    register()
    
    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=uiMenuTest.bl_idname)