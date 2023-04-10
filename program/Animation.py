import bpy

# Выбор объекта для анимации
obj = bpy.context.scene.objects['my_object']

# Создание ключевых кадров анимации
for i in range(0, 100, 10):
    bpy.context.scene.frame_set(i)
    obj.location.x += 1.0
    obj.keyframe_insert(data_path="location", index=-1)

# Воспроизведение анимации
bpy.ops.screen.animation_play()
