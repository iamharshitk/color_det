import cv2 as cv
import numpy as np
import glob

colour_holder=np.array([0,0,0])


def main():
    lower_lim=colour_holder-15
    upper_lim=colour_holder+15
    bin_img=cv.inRange(img, lower_lim, upper_lim)
 
    contours, _ = cv.findContours(bin_img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    op_img=img.copy()

    cv.drawContours(op_img, contours, -1, (57, 255, 20), -1)
    cv.imshow(winname,op_img)



def change_red(val):
    colour_holder[2]=val
    main()

def change_blue(val):
    colour_holder[0]=val
    main()

def change_green(val):
    colour_holder[1]=val
    main()

#Enter the path of the folder where the images are stored
#Example: "C:\\Users\\XYZ\\*.png"
folder_path="C:\\Users\\harsh\\OneDrive\\Desktop\\TestIP\\*.png"

for file in glob.glob(folder_path):

    winname="Task 1"
    cv.namedWindow(winname)

    img=cv.imread(file)


    cv.imshow(winname,img)

    set_low=0
    set_high=255

    cv.createTrackbar("R:", winname, set_low, set_high, change_red)
    cv.createTrackbar("G:", winname, set_low, set_high, change_green)
    cv.createTrackbar("B:", winname, set_low, set_high, change_blue)

    cv.waitKey(0)
    cv.destroyAllWindows()




