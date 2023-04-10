import bpy

# Создание мягкого тела
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
bpy.ops.object.modifier_add(type='SOFT_BODY')
bpy.context.object.modifiers["Softbody"].settings.goal_default = 0.0
bpy.context.object.modifiers["Softbody"].settings.use_goal = True
bpy.context.object.modifiers["Softbody"].settings.spring_length = 0.5
bpy.context.object.modifiers["Softbody"].settings.use_edges = True
bpy.context.object.modifiers["Softbody"].settings.use_faces = True
bpy.context.object.modifiers["Softbody"].settings.use_volume = True
bpy.context.object.modifiers["Softbody"].settings.use_pressure = True
bpy.context.object.modifiers["Softbody"].settings.use_bending = True

# Создание анимации мягкого тела
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 50

bpy.context.object.modifiers["Softbody"].settings.goal_default = 1.0
bpy.context.object.modifiers["Softbody"].point_cache.frame_start = 0
bpy.context.object.modifiers["Softbody"].point_cache.frame_end = 50

for frame in range(0, 50):
    bpy.context.scene.frame_set(frame)
    bpy.context.object.modifiers["Softbody"].settings.goal_default = 1.0
    bpy.context.object.modifiers["Softbody"].point_cache.update()
