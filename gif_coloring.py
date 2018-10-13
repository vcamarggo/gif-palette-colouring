import numpy as np
import cv2

ENTRY_COLOR_HUE = 360

HEIGHT= 128
WIDTH= HEIGHT*2 #O dobro pq vai dar append na altura com a segunda imagem

MIN_VALUE=0
MAX_VALUE=255
for i in range(180):
    ENTRY_COLOR_HUE= i
    h= np.repeat(np.repeat(ENTRY_COLOR_HUE, HEIGHT),WIDTH).reshape(HEIGHT,-1)
    s= np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::-2],WIDTH).reshape(HEIGHT,-1)
    v= np.repeat(np.repeat(MAX_VALUE, HEIGHT),WIDTH).reshape(HEIGHT,-1)
    
    color_white = cv2.merge([h.astype(np.uint8), s.astype(np.uint8), v.astype(np.uint8)])
    
    h= np.repeat(np.repeat(ENTRY_COLOR_HUE, HEIGHT),WIDTH).reshape(HEIGHT,-1)
    s= np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::2],WIDTH).reshape(HEIGHT,-1)
    v = np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::2],WIDTH).reshape(HEIGHT,-1)
    
    black_color = cv2.merge([h.astype(np.uint8), s.astype(np.uint8), v.astype(np.uint8)])
    
    full_image = np.append(black_color,color_white, axis=0)
    full_image_bgr = cv2.cvtColor(full_image,cv2.COLOR_HSV2BGR)
    
    cv2.imwrite('result/full-color-'+ str(i)+ '.jpg', full_image_bgr)