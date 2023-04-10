import bpy

# Создаем объект-емкость для жидкости
bpy.ops.mesh.primitive_cube_add(size=2)

# Добавляем физическое тело
bpy.ops.rigidbody.objects_add(type='PASSIVE')

# Создаем объект-источник жидкости
bpy.ops.object.empty_add(type='PLAIN_AXES')
empty = bpy.context.object

# Создаем объект-жидкость
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.mesh.primitive_ico_sphere_add(location=(0, 0, 2), size=1)
bpy.ops.object.modifier_add(type='FLUID_SIMULATION')

# Устанавливаем параметры жидкости
fluid_obj = bpy.context.object
fluid_settings = fluid_obj.modifiers['Fluid'].settings
fluid_settings.type = 'DOMAIN'
fluid_settings.domain_settings.resolution = 32
fluid_settings.domain_settings.use_spray_particles = True

# Устанавливаем параметры источника жидкости
empty.location = (0, 0, 0)
empty.keyframe_insert(data_path="location", frame=1)
empty.location = (0, 0, 5)
empty.keyframe_insert(data_path="location", frame=50)
fluid_settings.flow_settings.flow_type = 'LIQUID'
fluid_settings.flow_settings.flow_object = empty

# Запускаем симуляцию
bpy.ops.ptcache.bake_all(bake=True)
