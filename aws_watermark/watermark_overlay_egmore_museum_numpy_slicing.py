import cv2
import numpy as np

"""To combine the two images you can make use of numpy slicing to select the portion of the background image 
where you want to blend the foreground, then insert the newly blended portion in your background again."""

#image1 = cv2.imread("Egmore Museum Theatre-16.png")
#image2 = cv2.imread("Radiant-Watermark-Transparent-copy.png") #,cv2.IMREAD_UNCHANGED

def combine_two_color_images(image1, image2):
    """image1 = cv2.imread("Egmore Museum Theatre-16.png")
    image2 = cv2.imread("Radiant-Watermark-Transparent-copy.png") #,cv2.IMREAD_UNCHANGED"""
    
    foreground, background = image1.copy(), image2.copy()

    foreground_height = foreground.shape[0]
    foreground_width = foreground.shape[1]
    alpha =0.5

    # do composite on the upper-left corner of background image.
    blended_portion = cv2.addWeighted(foreground,
                alpha,
                background[:foreground_height,:foreground_width,:],
                1 - alpha,
                0,
                background)
    background[:foreground_height,:foreground_width,:] = blended_portion
    cv2.imshow("image", background)

    cv2.waitKey(10000)

image1 = cv2.imread("Egmore Museum Theatre-16.png")
image2 = cv2.imread("Radiant-Watermark-Transparent-copy.png", cv2.IMREAD_UNCHANGED)
combine_two_color_images(image1, image2)