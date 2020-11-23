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
        self.new_shape = None

    def pixellate(self, newpix=42, resample=Image.BOX):
        images = []
        for image in self.images:
            size = image.size
            scale = size[1] / size[0]

            small = image.resize((newpix, int(newpix * scale)), resample)
            images.append(small)

        # update images
        self.images = images

    def make_2d(self):
        self.new_shape = np.array(self.images[0]).shape
        self.images = self.images.reshape(len(self.images), -1)
        return self.new_shape

    def write_to_csv(self, filename, delimiter=" ", header="Processed images"):
        with open(str(filename), "w+") as f:
            np.savetxt(f, self.images, delimiter=delimiter, header=str(header + "reshape to: {}\n".format(self.new_shape)))

def random_plot():
    randomimg = np.random.choice(len(res.images), 20)
    randomimg = res.images[randomimg]

    for i, image in enumerate(randomimg):
        if i > 20:
            break
        fig, axs = plt.subplots()
        axs.imshow(image)
        plt.savefig("dataimages_post\image" + str(i) + ".png")

def main():
    folder = str(input("Folder which contain images: "))

    res = Post_prod(folder)
    res.pixellate(newpix=42)
    new_shape = res.make_2d()

    print("Reshape to {}, to see images or use in k-means-algorithm!".format(new_shape))


    storage = str(input("Name of file to store data (.csv): "))
    res.write_to_csv(storage)


if __name__ == "__main__":
    main()
