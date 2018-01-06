import bpy
for i in range(10):
    for j in range(10):
        bpy.ops.object.lamp_add(type='AREA', radius=1, view_align=False, location=(i*2,j*2,0.0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.context.object.data.distance = 15
        bpy.context.object.data.energy = 0.2
        bpy.context.object.data.color = (1, 0.828055, 0.649111)