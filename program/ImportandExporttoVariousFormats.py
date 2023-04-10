import bpy

# импорт файла
bpy.ops.import_scene.obj(filepath="file.obj")

# экспорт файла в формат FBX
bpy.ops.export_scene.fbx(filepath="file.fbx")
