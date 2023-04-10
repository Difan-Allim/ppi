import bpy

# Выбор объекта для риггинга
obj = bpy.context.scene.objects['my_object']

# Создание кости-корневого элемента
root_bone = bpy.data.armatures.new('RootBone')
root_bone_obj = bpy.data.objects.new('RootBone', root_bone)
bpy.context.collection.objects.link(root_bone_obj)

# Установка позиции и ориентации корневой кости
root_bone_obj.location = obj.location
root_bone_obj.rotation_euler = obj.rotation_euler

# Создание дочерних костей
bone_1 = root_bone.edit_bones.new('Bone1')
bone_1.head = (0, 0, 0)
bone_1.tail = (0, 0, 1)

bone_2 = bone_1.children.new('Bone2')
bone_2.head = (0, 0, 1)
bone_2.tail = (0, 1, 1)

# Соединение кости-корневого элемента с объектом
obj.parent = root_bone_obj
obj.parent_type = 'BONE'
obj.parent_bone = 'RootBone'

# Привязка объекта к скелету
modifier = obj.modifiers.new('Armature', 'ARMATURE')
modifier.object = root_bone_obj
