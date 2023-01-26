from PIL import Image

class image_convert:
    def __init__(self, type):
        self.type = type
        self.imglocation = ""
        self.imgname = ""
    
    def get_img(self):
        self.imglocation = input("Enter the input image location(without image name!!): ")
        self.imgname = input("Enter the image name(without image location!!): ")

    def to_jpg(self):
        img = Image.open(self.imglocation + self.imgname)
        splitted_name = self.imgname.split(".")
        self.imgname = splitted_name[0] + ".jpg"

        img.save(self.imglocation + self.imgname)

    def to_png(self):
        img = Image.open(self.imglocation + self.imgname)
        splitted_name = self.imgname.split(".")
        self.imgname = splitted_name[0] + ".png"

        img.save(self.imglocation + self.imgname)


    def to_webp(self):
        img = Image.open(self.imglocation + self.imgname)
        splitted_name = self.imgname.split(".")
        self.imgname = splitted_name[0] + ".webp"

        img.save(self.imglocation + self.imgname)


    def to_svg(self):
        img = Image.open(self.imglocation + self.imgname)
        splitted_name = self.imgname.split(".")
        self.imgname = splitted_name[0] + ".svg"

        img.save(self.imglocation + self.imgname)


    def main(self):
        self.get_img()
        if self.type == "jpg":
            self.to_jpg()
        
        elif self.type == "png":
            self.to_png()

        elif self.type == "webp":
            self.to_webp()
    
        elif self.type == "svg":
            self.to_svg()
        
        print("image saved in: " + self.imglocation)


def ImageConvert(Type):
    return image_convert(type=Type).main()