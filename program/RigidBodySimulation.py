import bpy

# Создаем объект-сетку
bpy.ops.mesh.primitive_cube_add(size=2)

# Добавляем физическое тело
bpy.ops.rigidbody.objects_add(type='ACTIVE')

# Устанавливаем гравитацию
bpy.context.scene.gravity = (0, 0, -9.81)

# Устанавливаем параметры физического тела
obj = bpy.context.object
obj.rigid_body.mass = 10
obj.rigid_body.friction = 0.5
obj.rigid_body.restitution = 0.2

# Добавляем силу
obj.rigid_body.apply_force((0, 0, 100), True)
