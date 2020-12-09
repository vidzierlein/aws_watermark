import cv2
import numpy as np
#importing the main image
image = cv2.imread("Egmore Museum Theatre-16.png")
oH,oW = image.shape[:2]
image = np.dstack([image, np.ones((oH,oW), dtype="uint8") * 255])
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 


#importing the logo image
lgo_img = cv2.imread("Egmore Museum Theatre copy.png",cv2.IMREAD_UNCHANGED)
#print(lgo_img)


#Resizing the image
scl = 10
w = int(lgo_img.shape[1] * scl / 100)
h = int(lgo_img.shape[0] * scl / 100)
dim = (w,h)
lgo = cv2.resize(lgo_img, dim, interpolation = cv2.INTER_AREA)
lH,lW = lgo.shape[:2]


#Blending
ovr = np.zeros((oH,oW,4), dtype="uint8")
ovr[oH - lH - 60:oH - 60, oW - lW - 10:oW - 10] = lgo
final = image.copy()
final = cv2.addWeighted(ovr,0.5,final,1.0,0,final)

"""img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dst = cv2.addWeighted(img1, 0.7, img2_resized, 0.3, 0)"""

# ShoWing the result
cv2.imshow("Combine Image",final)
cv2.waitKey(0)
cv2.destroyAllWindows()


#img2 = cv2.imread('messi.jpg')

# Read about the resize method parameters here: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html?highlight=resize#resize
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dst = cv2.addWeighted(img1, 0.7, img2_resized, 0.3, 0)