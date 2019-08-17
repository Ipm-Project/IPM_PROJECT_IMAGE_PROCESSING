
import cv2
import numpy as np
import glob
import os

image_folder = 'images'
video_name = 'narges.avi'
a=[]
b=[]
image_sorted=[]
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
for i in range(len(images)):
    a.append(images[i].split("."))
    b.append(int(a[i][0]))
b.sort()
for i in range(len(b)):
    image_sorted.append(str(b[i])+".png")
images=image_sorted

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'DIVX'), 15,(width,height))
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
