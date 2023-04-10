import bpy

# Выбор объекта-меша для ретопологии
bpy.context.scene.objects.active = bpy.data.objects['my_mesh']

# Создание нового объекта-меша для ретопологии
new_mesh = bpy.data.meshes.new(name='new_mesh')
new_object = bpy.data.objects.new(name='new_object', object_data=new_mesh)
bpy.context.scene.objects.link(new_object)

# Установка нового объекта-меша для ретопологии в режиме ретопологии
bpy.context.scene.tool_settings.mesh_select_mode = (True, False, False)  # Режим ребер
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.delete(type='ONLY_FACE')
bpy.ops.mesh.reveal()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.edge_face_add()
bpy.ops.object.editmode_toggle()

# Копирование данных геометрии существующего объекта-меша в новый объект-меш
new_mesh.from_mesh(bpy.context.object.data)
