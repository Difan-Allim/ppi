import bpy
import os

# Создание сцены и камеры
scene = bpy.context.scene
camera = bpy.data.objects.new('Camera', bpy.data.cameras.new('Camera'))
scene.collection.objects.link(camera)
scene.camera = camera

# Добавление освещения
sun = bpy.data.lights.new('Sun', type='SUN')
light = bpy.data.objects.new('Sun', sun)
light.location = (0, 0, 10)
scene.collection.objects.link(light)

# Импорт модели здания
file_path = os.path.join(os.getcwd(), 'building.obj')
bpy.ops.import_scene.obj(filepath=file_path)

# Создание материалов для здания
building_material = bpy.data.materials.new(name='Building')
building_material.use_nodes = True
nodes = building_material.node_tree.nodes
links = building_material.node_tree.links
diffuse_node = nodes.new('ShaderNodeBsdfDiffuse')
diffuse_node.inputs['Color'].default_value = (0.8, 0.8, 0.8, 1)
output_node = nodes.new('ShaderNodeOutputMaterial')
links.new(diffuse_node.outputs['BSDF'], output_node.inputs['Surface'])

# Применение материала к зданию
building_object = bpy.context.selected_objects[0]
for face in building_object.data.polygons:
    face.material_index = 0
building_object.data.materials.append(building_material)

# Рендеринг сцены
render_settings = scene.render
render_settings.resolution_x = 1920
render_settings.resolution_y = 1080
render_settings.resolution_percentage = 100
render_settings.image_settings.file_format = 'PNG'
render_settings.filepath = os.path.join(os.getcwd(), 'render.png')
bpy.ops.render.render(write_still=True)
