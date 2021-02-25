from plugins import Plugin
from diffimg import diff


class Image(Plugin):

    def __init__(self):
        super().__init__()

    def compare(self, image1, image2):
        difference = round(diff(image1, image2), 3)
        return difference
        # print(f"{difference}%")
