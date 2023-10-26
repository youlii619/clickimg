import cv2
import numpy as np
import sys

if len(sys.argv) < 2:
    print('Usage: python3 clickimg.py <image_file>')
    sys.exit(1)

file_name = sys.argv[1]

img=cv2.imread(file_name,cv2.IMREAD_COLOR)
img=cv2.resize(img,(600,600))
def click_pos(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        img2=np.copy(img)
        cv2.circle(img2,center=(x,y),radius=10,color=(0,0,0),thickness=-1)
        # Assume the read image is in a greyscale so values of B,G,R are all the same = here I use just B
        B1=img[y,x,0]
        B2=img[y,x+5,0] # 5 pixels to right
        B3=img[y,x-5,0] # 5 pixels to left
        B4=img[y+5,x,0] # 5 pixels to top
        B5=img[y-5,x,0] # 5 pixels to bottom
        B6=img[y+3,x+3,0] # top right
        B7=img[y+3,x-3,0] # top left
        B8=img[y-3,x+3,0] # bottom right
        B9=img[y-3,x-3,0] # bottom left
        B=round(((int(B1)+int(B2)+int(B3)+int(B4)+int(B5)+int(B6)+int(B7)+int(B8)+int(B9))/9),2)
        bgr_str='Avg. = '+str(B)
        bgr_ave=' ('+str(B1)+', '+str(B2)+', '+str(B3)+', '+str(B4)+', '+str(B5)+', '+str(B6)+', '+str(B7)+', '+str(B
8)+', '+str(B9)+')'

        cv2.putText(img2,bgr_str,(20, 20),cv2.FONT_HERSHEY_PLAIN,1.7,(56,48,239),2,cv2.LINE_AA)
        cv2.putText(img2,bgr_ave,(20, 35),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2,cv2.LINE_AA)
        cv2.imshow('window', img2)

cv2.imshow('window', img)
cv2.setMouseCallback('window', click_pos)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
