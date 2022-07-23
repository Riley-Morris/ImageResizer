import os
from PIL import Image

def resizer(x, y, folder_name):
    for ima in os.listdir(folder_name):

        image = Image.open(f'{folder_name}\\{ima}')
        image.thumbnail((x, y))
        image.save(f'edited\\{ima}')

# 523, 59 - capture size of syl
#350, 35 - resize size for syl
#408, 513 - capture size images
#200, 250
resizer(200, 250, 'Raw')