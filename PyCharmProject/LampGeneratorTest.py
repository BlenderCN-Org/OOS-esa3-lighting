# -*- coding: utf-8 -*-

__author__ = 'dk taege'


import bpy

scene = bpy.context.scene

# create new lamp datablock
lampData = bpy.data.lamps.new(name="new lamp data", type = 'POINT')

# create new object with lamp datablock
lampObject = bpy.data.objects.new(name="new lamp object", object_data = lampData)

# link lamp object to the scene so it appears
scene.objects.link(lampObject)

# place lamp to position
lampObject.location = (0,0,0)

# select it and activate
lampObject.select = True
scene.objects.active = lampObject