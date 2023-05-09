from PIL import Image, ImageFilter
from pathlib import Path

names1 = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
path_name = Path.cwd()
names = list(Path(path_name).glob('*.jpg'))
Path('new_path').mkdir(parents=True, exist_ok=True)

print(names)
for file in names:
    with Image.open(file) as img:
        img.load()

        filt_img = img.filter(ImageFilter.EMBOSS)
        filt_img.show()
        filt_img.save('new_path/new_' + names1[names.index(file)])