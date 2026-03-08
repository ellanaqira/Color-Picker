from load_image import Load_image

class Aset:
    def __init__(self):
        self.icon_img = Load_image("aset/full_icon.png", (150,60))
        self.copy_icon = Load_image("aset/copy_icon.png", (19,19))
        self.reverse_icon = Load_image("aset/reverse_icon.png", (19,19))
        self.down_icon = Load_image('aset/down.png', (20,15))