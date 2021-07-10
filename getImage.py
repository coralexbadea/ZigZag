import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui
import numpy as np

pyautogui.PAUSE = 0
sct = mss.mss()

"""
dimensions = {
        'left': 600,
        'top': 530,
        'width': 155,
        'height': 220
    }
scr = sct.grab(dimensions)
img = np.array(scr)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("./screen_left.png", img)


dimensions = {
		'left': 600,
        'top': 530 ,
        'width': 155,
        'height': 35
    }
scr = sct.grab(dimensions)
img = np.array(scr)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("./wood_left.png", img)
"""

dimensions = {
		'left': 860,
        'top': 530,
        'width': 155,
        'height': 220
    }
scr = sct.grab(dimensions)
img = np.array(scr)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("./screen_right.png", img)


dimensions = {
		'left': 860,
        'top': 530,
        'width': 155,
        'height': 35
    }
scr = sct.grab(dimensions)
img = np.array(scr)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("./wood_right.png", img)

