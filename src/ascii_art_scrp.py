from matplotlib.colors import rgb2hex
import matplotlib.pyplot as plt

from os import getcwd, sep
from PIL import Image

RES_PATH = sep.join(['C:','Users','g.raiano','Desktop','Archivio','Sviluppi','Python','DataMaster','Py4DataScience','resources'])

# jpg_list = ['StephanieWong', 'emma_stone', 'photo']
jpg_list = ['photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5']
name = jpg_list[3]
# img_pth = sep.join([RES_PATH, 'emma_stone.jpg'])
img_pth = sep.join([RES_PATH, name + '.jpg'])

# load image with matplotlib
# img = plt.imread(img_pth)
# print(img.shape)
# plt.imshow(img)

# load image with PIL (from pillow)
pil_img = Image.open(img_pth)
print(f'W x H = {pil_img.width}x{pil_img.height}')

gry_img = pil_img.convert('LA')

# reduced_img = gry_img
# reduced_img = gry_img.resize((96, 96))
tpl_resize = (int(gry_img.width / 2), int(gry_img.height/2))
reduced_img = gry_img.resize(tpl_resize)

ascii_chars = ['@', '#', '|', '$', '.', '_', ' ', '-']

# tuple pixel example from image
pixel_tuple = reduced_img.getdata()[0]
print(pixel_tuple)

# Calcolo del range dei valori pixel in scala di grigi per lista di conversione ascii_chars
pixel_gray_intervals = int(256 / len(ascii_chars))

# calcolo da fare per la sostituzione del pixel con il carattere
#     int(pixel / pixel_gray_intervals) => la parte intera corrispondere alla posizione dell'ascii char
# >>> ascii_chars_index = pixel_tuple[0] / pixel_gray_intervals
# verifica del valore con l'indice della lista di caratteri ascii disponibili
# >>> car_pixel = ascii_chars[ascii_chars_index]

ascii_image = ''
try:
    for px in reduced_img.getdata():
        pos = int(px[0] / pixel_gray_intervals) if int(px[0] / pixel_gray_intervals) < len(ascii_chars) else len(ascii_chars) - 1
        ascii_image += ascii_chars[pos]
except IndexError as e:
    print(f'{px[0]} % {pixel_gray_intervals} = {int(px[0] / pixel_gray_intervals)}')
    print(f'len(ascii_chars) = {len(ascii_chars)}')
    exit(-1)

# rigenerazione della stringa nel formato dell'immagine
# for e in range(0, len(ascii_image), reduced_img.width):
#     print(ascii_image[e:e+reduced_img.width])

with open(sep.join([RES_PATH, name + '.txt']), 'w') as f:
    for e in range(0, len(ascii_image), reduced_img.width):
        f.write(ascii_image[e:e+reduced_img.width] + '\n')
        print(ascii_image[e:e+reduced_img.width])

print('Execution finished...')