import bpy

#bpy.ops.mesh.primitive_monkey_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))


#Führung hinzufügen
bpy.ops.object.lamp_add(type='AREA', radius=1, view_align=False, location=(-2.75, -2.00, 2.3), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#distance
bpy.context.object.data.distance = 15
#energy
bpy.context.object.data.energy = 0.2
#color
bpy.context.object.data.color = (1, 0.828055, 0.649111)

#Aufhellung hinzufügen
bpy.ops.object.lamp_add(type='AREA', view_align=False, location=(3.11, -2.02, 1.35), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#distance
bpy.context.object.data.distance = 15
#energy
bpy.context.object.data.energy = 0.1
#color
bpy.context.object.data.color = (1, 0.828055, 0.649111)

#Spitze hinzufügen
bpy.ops.object.lamp_add(type='SPOT', view_align=False, location=(-3.85, 2.44, 2.26), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#distance
bpy.context.object.data.distance = 15
#energy
bpy.context.object.data.energy = 0.1
#color
bpy.context.object.data.color = (1, 0.828055, 0.649111)