# Importing all necessary libraries
import cv2
import os

# path
def main():
    video_name = str(input("Enter name of .mp4: "))
    storage = str(input("Enter filename of new folder: "))

    cwd = os.getcwd()
    path = os.path.join(cwd, video_name)

    # Read the video from specified path
    cam = cv2.VideoCapture(path)

    try:

        # creating a folder named data
        if not os.path.exists(storage):
            os.makedirs(storage)

    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')

    # frame
    currentframe = 0

    while(True):

        # reading from frame
        ret,frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = './' + storage + '/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
