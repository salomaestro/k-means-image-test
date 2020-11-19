import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

class Post_prod(object):
    """
    Does some resize, cropping, and greytones on many images.
    """
    def __init__(self, foldername):
        self.folder = foldername

        images = []
        for image in os.listdir(self.folder):
            images.append(Image.open(os.path.join(os.getcwd(), self.folder, image)))

        self.images = images
        self.orig_size = self.images[0].size

    def crop(self):
        images = []
        for image in self.images:
            # size of image
            width, height = image.size

            # setting the points for cropped image
            left = width / 3
            top = height / 5
            right = 3 * width / 4
            bottom = 7 * height / 8

            images.append(image.crop((left, top, right, bottom)))

        # Update images
        self.images = images

    def pixellate(self, newpix=64, resample=Image.BOX):
        images = []
        for image in self.images:
            size = image.size
            scale = size[1] / size[0]

            small = image.resize((64, int(64 * scale)), resample)
            images.append(small.resize((size), resample))

        # update images
        self.images = images

    def grayscale(self, g1=0.2989, g2=0.5870, g3=0.1140):
        images = []
        for image in self.images:
            image = np.array(image)
            images.append(np.dot(image, [g1, g2, g3]))

        self.images = np.asarray(images)

    def make_2d(self):
        self.images = self.images.reshape(len(self.images), -1)

    def write_to_csv(self, filename, delimiter=" ", header="Processed images"):
        with open(str(filename), "w+") as f:
            np.savetxt(f, self.images, delimiter=delimiter, header=str(header + "reshape to: {}\n".format(self.orig_size)))

def main():
    folder = str(input("Folder which contain images: "))
    res = Post_prod(folder)
    res.crop()
    res.pixellate()
    res.grayscale()

    fig, axs = plt.subplots()
    axs.imshow(res.images[0])
    plt.show()

    res.make_2d()

    storage = str(input("Name of file to store data (.csv): "))
    res.write_to_csv(storage)


if __name__ == "__main__":
    main()
