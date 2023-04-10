import bpy

# создание нового проекта
bpy.ops.wm.read_homefile(use_empty=True)

# импорт видеофайла
bpy.ops.sequencer.movie_strip_add(filepath='/path/to/video.mp4', frame_start=1, channel=1)

# добавление звуковой дорожки
bpy.ops.sequencer.sound_strip_add(filepath='/path/to/audio.mp3', frame_start=1, channel=2)

# наложение эффектов
effect_strip = bpy.context.scene.sequence_editor.active_strip
bpy.ops.sequencer.effect_strip_add(frame_start=effect_strip.frame_start, frame_end=effect_strip.frame_end, type='COLOR_BALANCE')

# экспорт готового видеофайла
bpy.ops.render.render(animation=True)
