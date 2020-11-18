import os

def main():
    for i, filename in enumerate(os.listdir(r"C:\Users\Christian Salomonsen\github\k-means-test\Clustering_test_photos")):
        dst = "Image" + str(i) + ".jpg"
        src = r"C:\Users\Christian Salomonsen\github\k-means-test\Clustering_test_photos" + "\{}".format(filename)
        dst = r"C:\Users\Christian Salomonsen\github\k-means-test\Clustering_test_photos" + "\{}".format(dst)

        os.rename(src, dst)

if __name__ == "__main__":
    main()
