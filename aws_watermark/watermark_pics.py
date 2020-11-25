""" import cv2

background = cv2.imread('Egmore Museum Theatre-16.png', cv2.IMREAD_UNCHANGED)
foreground = cv2.imread('Radiant-Watermark-Transparent-copy.png', cv2.IMREAD_UNCHANGED) """

import cv2
import numpy as np

background = cv2.imread('Egmore Museum Theatre-16.png', cv2.IMREAD_UNCHANGED)
foreground = cv2.imread('Radiant-Watermark-Transparent-copy.png', cv2.IMREAD_UNCHANGED)

def foregroundOverlay(background, foreground, alpha=1.0,x=0, y=0, scale=1.0):
    (h, w) = foreground.shape[:2]
    background = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
    overlay = cv2.resize(foreground, None,fx=scale,fy=scale)
    (wH, wW) = overlay.shape[:2]
    output = background.copy()
    # blend the two images together using transparent overlays
    try:
        if x<0 : x = w+x
        if y<0 : y = h+y
        if x+wW > w: wW = w-x  
        if y+wH > h: wH = h-y
        print(x,y,wW,wH)
        overlay=cv2.addWeighted(output[y:y+wH, x:x+wW],alpha,overlay[:wH,:wW],1.0,0)
        output[y:y+wH, x:x+wW ] = overlay
    except Exception as e:
        print("Error: foreground position is overshooting image!")
        print(e)
    output= output[:,:,:3]
    return output