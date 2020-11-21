# k-means facial expression clustering.
---
*Author: Christian Salomonsen*
## Table of contents

1. Description
2. Dependencies
3. Current results
4. How to use the algorithm (step-by-step)

## 1. Description
This is a repo constructed as a part of my project to gather my own training data, and apply the knowledge i got from machine learning.
## 2. Dependencies
- [Numpy](https://numpy.org/install/)
- [Matplotlib](https://pypi.org/project/matplotlib/)
- [PILLOW](https://pillow.readthedocs.io/en/stable/installation.html)
- [os-sys](https://pypi.org/project/os-sys/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [time](https://pypi.org/project/python-time/)

## 3. Current results

1. 2 clusters
![Results from 2 clusters](results/cluster2.png "2 clusters")

2. 4 clusters
![Results from 4 clusters](results/cluster4.png "4 clusters")

3. 10 clusters
![Results from 10 clusters](results/cluster10.png "10 clusters")

## 4. How to use the algorithm

1. Take a video of yourself, doing different grimaces, try to stay in the centre of the frame about half a meter from the camera.
2. Drag the video into this directory, the video should be a .mp4 file, if you have something else, try [this](https://cloudconvert.com/mov-to-mp4).
3. Navigate in your console to this directory, then type `python video_to_images.py`. Further instructions appear in console, you will have to give a folder name where individual frames are stored.
4. Type `python image_postprod.py`, then specify the folder name where the frames are stored.
5. Final step: type `python k-means-algorithm.py`. Specify what file (.csv) the data file is stored, and specify the shape as "x, y". From the print of image_postprod.py it will specify the shape (x, y).
