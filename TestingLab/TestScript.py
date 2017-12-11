import bpy
# always import bpy --> blender python connection

# generate 10 point lamps on top of each other starting at 0 0 0
for i in range(10):

    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(0,0,i), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
