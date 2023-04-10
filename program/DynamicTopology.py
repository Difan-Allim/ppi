import bpy

# Выбор объекта и переключение в режим редактирования
bpy.context.view_layer.objects.active = bpy.data.objects['my_object']
bpy.ops.object.mode_set(mode='EDIT')

# Включение динамической топологии
bpy.context.tool_settings.mesh_dynamic_topology_toggle.use_dynamic_topology_sculpting = True

# Настройка параметров динамической топологии
bpy.context.tool_settings.mesh_dynamic_topology_sculpt.use_detail_falloff = True
bpy.context.tool_settings.mesh_dynamic_topology_sculpt.detail_type = 'SUBDIVISION'

# Изменение геометрии с помощью динамической топологии
bpy.ops.brush.sculptdetail(True)
