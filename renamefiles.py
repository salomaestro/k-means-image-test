import os

def rename():
    cwd = os.getcwd()
    path = str(input("Enter folder name: "))
    for i, filename in enumerate(os.listdir(path)):
        dst = "Image" + str(i) + ".jpg"
        src = os.path.join(path, filename)
        dst = os.path.join(path, dst)

        os.rename(src, dst)

def main():
    rename()

if __name__ == "__main__":
    main()
