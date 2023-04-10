import bpy

# установка параметров рендеринга
scene = bpy.context.scene
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "//render.png"

# создание источников света
lamp_data = bpy.data.lamps.new(name="New Lamp", type='POINT')
lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)
bpy.context.collection.objects.link(lamp_object)

# настройка положения источников света
lamp_object.location = (0.0, 0.0, 5.0)
lamp_object.rotation_euler = (0.0, 0.0, 0.0)

# создание 3D-модели
bpy.ops.mesh.primitive_cube_add(size=2.0)

# настройка материала для 3D-модели
mat = bpy.data.materials.new(name="Material")
mat.diffuse_color = (0.8, 0.2, 0.2)
bpy.context.object.data.materials.append(mat)

# настройка камеры
camera_data = bpy.data.cameras.new(name="New Camera")
camera_object = bpy.data.objects.new(name="New Camera", object_data=camera_data)
bpy.context.collection.objects.link(camera_object)

# настройка положения и ориентации камеры
camera_object.location = (0.0, -5.0, 0.0)
camera_object.rotation_euler = (1.5708, 0.0, 0.0)

# рендеринг сцены
bpy.ops.render.render(write_still=True)
