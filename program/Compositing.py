from PIL import Image

# Загрузка изображения
img = Image.open('path/to/image.png')

# Изменение размера
scale = 0.5
width, height = img.size
new_width, new_height = int(scale * width), int(scale * height)
img = img.resize((new_width, new_height))

# Сохранение результата
img.save('path/to/output.png')
