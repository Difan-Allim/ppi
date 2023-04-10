import bpy

# Создание нового объекта-меша
new_mesh = bpy.data.meshes.new('new_mesh')
new_object = bpy.data.objects.new('new_object', new_mesh)
bpy.context.scene.objects.link(new_object)

# Создание вершин
verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)]
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
faces = [(0, 1, 2, 3)]

# Заполнение меша вершинами, ребрами и гранями
new_mesh.from_pydata(verts, edges, faces)
new_mesh.update()
