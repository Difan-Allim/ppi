import bpy

# Выбор объекта-меша для раскраски
bpy.context.scene.objects.active = bpy.data.objects['my_mesh']

# Создание нового материала для объекта-меша
new_material = bpy.data.materials.new(name='new_material')
bpy.context.object.data.materials.append(new_material)

# Создание новой текстурной кисти
new_paint_brush = bpy.data.brushes.new(name='new_paint_brush', type='PAINT_TEXTURE')
new_paint_brush.texture_slot = new_material.texture_slots[0]
new_paint_brush.use_alpha = True

# Применение раскраски к объекту-мешу
bpy.ops.paint.texture_paint_toggle()
bpy.ops.paint.image_paint_toggle()
bpy.context.scene.tool_settings.image_paint.brush = new_paint_brush
