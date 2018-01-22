
import bpy
#make a plane for setting up a table top
bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.transform.resize(value=(-5.0, -5.0, -5.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

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
bpy.context.object.data.color = (1, 0)