from PIL import Image, ImageFilter
from pathlib import Path

path_name = Path.cwd()
names = list(Path(path_name).glob('*'))
Path('new_path').mkdir(parents=True, exist_ok=True)

for file in names:
    if file.suffix in ['.jpg', '.png']:
        with Image.open(file) as img:
            img.load()

            filt_img = img.filter(ImageFilter.EMBOSS)
            filt_img.show()
            filt_img.save(Path('new_path', file))
