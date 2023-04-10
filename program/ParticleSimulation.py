import bpy

# Создание объекта-эмиттера
emitter = bpy.data.objects.new("Emitter", None)
bpy.context.scene.collection.objects.link(emitter)

# Создание системы частиц на основе объекта-эмиттера
particle_system = emitter.modifiers.new(type='PARTICLE_SYSTEM', name='Particle System')
particle_system.particle_system.settings.count = 1000
particle_system.particle_system.settings.frame_start = 1
particle_system.particle_system.settings.frame_end = 50

# Настройка системы частиц
particle_settings = particle_system.particle_system.settings
particle_settings.emit_from = 'VERT'
particle_settings.physics_type = 'NEWTONIAN'
particle_settings.normal_factor = 0.5
particle_settings.tangent_factor = 0.5

# Создание эмиттера частиц
particle_emitter = particle_system.particle_system.emitters[0]
particle_emitter.emit_from_vertices = True
particle_emitter.particle_size = 0.05

# Создание эффекта частиц
particle_effect = particle_system.particle_system.point_cache
particle_effect.name = "Particle Effect"
particle_effect.frame_start = 1
particle_effect.frame_end = 50
