import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def open_all_images(foldername):
    images = []
    for image in os.listdir(foldername):
        images.append(Image.open(os.path.join(os.getcwd(), foldername, image)))
    return images

def crop_image(image):
    # Size of the image in pixels (size of orginal image)
    width, height = image.size

    # Setting the points for cropped image
    left = width / 3
    top = height / 5
    right = 3 * width / 4
    bottom = 7 * height / 8

    # Cropped image of above dimension
    im1 = image.crop((left, top, right, bottom))
    return np.array(im1)

def pixellate(image):
    small = image.resize((64, 64), resample=Image.BILINEAR)
    return small.resize(image.size,Image.NEAREST)

def rgb_to_gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    return np.dot(rgb, [0.2989, 0.5870, 0.1140])

def flatten_3d_to_2d(arr):
    orig_shape = arr.shape
    return arr.reshape(-1, len(arr)), orig_shape

def write_to_csv(images, reshape_to):
    header = "Numerical representation of images, to retrive original image, reshape to: {}\n".format(reshape_to)
    with open("Images_to_use.csv", "w+") as f:
        np.savetxt(f, images, delimiter=" ", header=header)

def main():
    images = open_all_images("Clustering_test_photos")
    processed = []
    for image in images:
        pixelated = pixellate(image)
        cropped = crop_image(pixelated)
        gray = rgb_to_gray(cropped)
        processed.append(gray)

    processed = np.asarray(processed)
    flat, shape = flatten_3d_to_2d(processed)
    write_to_csv(flat, shape)


    # plt.imshow(processed[0], cmap="gray")
    # plt.show()

if __name__ == "__main__":
    main()




# crop_im = crop_image(im)
# gray_im = rgb_to_gray(crop_im)
#
# plt.imshow(gray_im, cmap="gray")
# plt.show()

# Shows the image in image viewer
# im1.show()
