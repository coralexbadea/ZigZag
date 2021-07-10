import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui
import numpy as np
#xhost +

pyautogui.PAUSE = 0

print("Press 's' to start playing.")
print("Once started press 'q' to quit.")
keyboard.wait('s')
left = True

sct = mss.mss()
dimensions_left = {
        'left': 600,
        'top': 510,
        'width': 155,
        'height': 220
    }

dimensions_right = {
  	'left': 860,
        'top': 510,
        'width': 155,
        'height': 220
    }
    
 
x = dimensions_left["left"]
y = dimensions_left["top"]

wood_left = cv2.imread('/home/aedab/Desktop/ZigZag-master/wood_left.png')

wood_right = cv2.imread('/home/aedab/Desktop/ZigZag-master/wood_right.png')
w = wood_left.shape[1]
h = wood_left.shape[0]

fps_time = time()

while 1:

	if left:
		scr = numpy.array(sct.grab(dimensions_left))
		wood = wood_left
	else:
		scr = numpy.array(sct.grab(dimensions_right))
		wood = wood_right

	# Cut off alpha
	scr_remove = scr[:,:,:3]

	result = cv2.matchTemplate(scr_remove, wood, cv2.TM_CCOEFF_NORMED)

	_, max_val, _, max_loc = cv2.minMaxLoc(result)
	print(f"Max Val{left}: {max_val} Max Loc: {max_loc}")

	if max_val > .70:
		left = not left
		if left:
		    x=dimensions_left["left"]
		else:
		    x=dimensions_right["left"]
		    
	pyautogui.click(x=x, y=y)
	sleep(0.4)
	if keyboard.is_pressed('q'):
		break
	#print('FPS: {}'.format(1 / (time() - fps_time)))
	#fps_time = time()
