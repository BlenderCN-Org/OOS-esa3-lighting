# -*- coding: utf-8 -*-

__author__ = 'dk taege'


"""
in num_empties    s   d=4   n=2
out obj_generated o
"""
import bpy
scene = bpy.context.scene
objects = bpy.data.objects

idx = 0
for i in range(num_empties):
    mt_name = 'empty_sv.' + str("%04d" % i)
    if mt_name not in objects:
        mt = objects.new(mt_name, None)
        mt['origin'] = 'SNLite'
        mt['idx'] = i
        mt.location = (0, 2, 1.2*i )
        mt.empty_draw_size = 2
        scene.objects.link(mt)
        scene.update()
    else:
        mt = objects[mt_name]
    idx = i

for obj in objects:
    if obj.get('origin') == 'SNLite' and obj.get('idx') > idx:
        scene.objects.unlink(obj)
        objects.remove(obj, do_unlink=True)


obj_generated = [o for o in objects if o.get('origin') == 'SNLite']