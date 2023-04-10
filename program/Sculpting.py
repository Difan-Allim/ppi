import bpy

# Выбор объекта-меша для скульптинга
bpy.context.scene.objects.active = bpy.data.objects['my_mesh']

# Переключение в режим скульптинга
bpy.ops.sculpt.sculptmode_toggle()

# Выбор инструмента для скульптинга
bpy.context.scene.tool_settings.sculpt.brush = bpy.data.brushes['Clay']

# Скульптирование
bpy.ops.sculpt.sculpt()

# Сохранение изменений в меше
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.wm.save_as_mainfile(filepath='new_mesh.blend')
