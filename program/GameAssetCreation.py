import bpy

# Очистить сцену
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Создать новый объект-куб
bpy.ops.mesh.primitive_cube_add(location=(0,0,0), scale=(1,1,1))

# Добавить Subdivision Surface модификатор для увеличения разрешения куба
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].render_levels = 2
bpy.context.object.modifiers["Subdivision"].levels = 2

# Применить модификатор
bpy.ops.object.modifier_apply(modifier="Subdivision")

# Создать новый материал для куба
new_mat = bpy.data.materials.new('Material')
new_mat.use_nodes = True

# Добавить ноды для создания текстуры
nodes = new_mat.node_tree.nodes
texture_node = nodes.new(type='ShaderNodeTexImage')
texture_node.image = bpy.data.images.load('texture.png')
diffuse_node = nodes.get('Diffuse BSDF')
links = new_mat.node_tree.links
links.new(texture_node.outputs[0], diffuse_node.inputs[0])

# Назначить материал кубу
bpy.context.object.active_material = new_mat

# Экспортировать куб в формат .fbx
bpy.ops.export_scene.fbx(filepath='cube.fbx')
