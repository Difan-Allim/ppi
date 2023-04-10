import bpy

# Создание новой композитной схемы
bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree
links = tree.links
for n in tree.nodes:
    tree.nodes.remove(n)

# Создание узлов
image_node = tree.nodes.new(type='CompositorNodeImage')
image_node.image = bpy.data.images.load("path/to/image.png")
scale_node = tree.nodes.new(type='CompositorNodeScale')
output_node = tree.nodes.new(type='CompositorNodeComposite')

# Подключение узлов
links.new(image_node.outputs[0], scale_node.inputs[0])
links.new(scale_node.outputs[0], output_node.inputs[0])
