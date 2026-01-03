import os
import cv2
from PIL import Image

os.chdir("C:\OpenCV with python\MergeImages\Images")
path = "C:\OpenCV with python\MergeImages\Images"

meanHeight = 0
meanWidth = 0
num_of_images = len(os.listdir('.'))

#Calculating total width and height of the images
for file in os.listdir('.'):
    img = Image.open(os.path.join(path,file))
    width,height = img.size
    meanHeight = meanHeight + height
    meanWidth = meanWidth + width

meanWidth = meanWidth // num_of_images
meanHeight = meanHeight // num_of_images

print(meanWidth, meanHeight)

#Resizing all the images to the same size
for i in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path,file))
        width,height = img.size
        print(width,height)

        resize = img.resize((meanWidth,meanHeight),Image.Resampling.LANCZOS)
        print(img.filename.split('\\')[-1]," isresized")

#Create the video
def videoGenerator():
    video_name = "Landscapes.avi"
    os.chdir("C:\OpenCV with python\MergeImages\Images")
    images = []
    for i in os.listdir('.'):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            images.append(i)
            print(images)
    
    frame = cv2.imread(os.path.join(".",images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name,0,1,(width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(".",image)))
    cv2.destroyAllWindows()
    video.release()

videoGenerator()