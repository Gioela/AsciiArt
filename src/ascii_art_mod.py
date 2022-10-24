from os import sep
from PIL import Image

class GegAsciiArt:

    def __init__(self, img_pth, img_name, img_type = 'jpg', scale_factor = 4, save_result = True, save_pth = None) -> None:
        self.img_name = img_name
        self.img_type = img_type
        self.img_pth = img_pth
        self.save_result = save_result
        self.save_img_pth = save_pth
        self.scale_factor = scale_factor
        self._setup()

    def _setup(self):
        self.ascii_chars = ['@', '#', '|', '$', '.', '_', ' ', '-']
        self.image = ''
        self.gray_image = ''
        self.resized_image = ''
        self.ascii_image = ''
        # if not declared, ascii_image will be saved in same path of the source image
        if self.save_result and self.save_img_pth == None:
            self.save_img_pth = self.img_pth

    def load_image(self):
        self.image = Image.open(sep.join([self.img_pth, self.img_name + '.' + self.img_type]))
        print(f'Loaded image with dimensions: {self.image.width}x{self.image.height} (W x H)')

    def convert_image_to_gray(self):
        self.gray_image = self.image.convert('LA')

    def resize_gray_image(self):
        scale_tuple = (int(self.gray_image.width / self.scale_factor), int(self.gray_image.height / self.scale_factor))
        self.resized_image = self.gray_image.resize(scale_tuple)

    def get_ascii_image(self):
        pixel_gray_intervals = int(256 / len(self.ascii_chars))
        self.ascii_image = ''
        try:
            for px in self.resized_image.getdata():
                pos = int(px[0] / pixel_gray_intervals) if int(px[0] / pixel_gray_intervals) < len(self.ascii_chars) else len(self.ascii_chars) - 1
                self.ascii_image += self.ascii_chars[pos]
        except IndexError as e:
            print(f'{px[0]} % {pixel_gray_intervals} = {int(px[0] / pixel_gray_intervals)}')
            print(f'len(self.ascii_chars) = {len(self.ascii_chars)}')
            exit(-1)

    def save_image(self):
        if self.save_result:
            with open(sep.join([self.save_img_pth, f'{self.img_name}_{self.scale_factor}.txt']), 'w') as f:
                for e in range(0, len(self.ascii_image), self.resized_image.width):
                    f.write(self.ascii_image[e : e + self.resized_image.width] + '\n')
    
    def print_image(self):
        for e in range(0, len(self.ascii_image), self.resized_image.width):
            print(self.ascii_image[e: e + self.resized_image.width])


    def setup(self, imgtype = None, scale_fact = None, save_res = None, save_img_pth = None):
        if imgtype != None:
            self.img_type = imgtype

        if scale_fact != None:
            self.scale_factor = int(scale_fact)

        if save_res != None:
            self.save_result = False if save_res.lower()[0] == 'n' else True

        if self.save_result and save_img_pth != None:
            self.save_img_pth = save_img_pth

    def run(self):
        self.load_image()
        self.convert_image_to_gray()
        self.resize_gray_image()
        self.get_ascii_image()
        self.save_image()
        if self.save_result == False:
            self.print_image()

if __name__ == '__main__':
    from sys import argv
    for idx, el in enumerate(argv):
        print(idx, el)
    ascii_art = GegAsciiArt(argv[1], argv[2])
    if len(argv) == 4:
        ascii_art.setup(argv[3])
    elif len(argv) == 5:
        ascii_art.setup(argv[3], argv[4])
    elif len(argv) == 6:
        ascii_art.setup(argv[3], argv[4], argv[5])
    elif len(argv) == 7:
        ascii_art.setup(argv[3], argv[4], argv[5], argv[6])
    ascii_art.run()
