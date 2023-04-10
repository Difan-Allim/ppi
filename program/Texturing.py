import bpy

# Выбор объекта-меша для текстурирования
bpy.context.scene.objects.active = bpy.data.objects['my_mesh']

# Создание нового материала для объекта-меша
new_material = bpy.data.materials.new(name='new_material')
bpy.context.object.data.materials.append(new_material)

# Загрузка текстуры
texture_path = '/path/to/texture/image.png'
texture_image = bpy.data.images.load(texture_path)

# Создание новой текстурной кисти
new_texture_brush = bpy.data.brushes.new(name='new_texture_brush', type='TEXTURE')
new_texture_brush.texture = texture_image

# Применение текстурной кисти к материалу
new_material.use_textures[0] = True
new_material.texture_slots[0].texture_coords = 'UV'
new_material.texture_slots[0].texture.type = 'IMAGE'
new_material.texture_slots[0].texture.image = texture_image
