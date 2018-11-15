import numpy as np
import cv2
import imageio
import os
from PIL import Image

INIT_COLOR_HUE = 0 #Hue (Matiz) de saída inicial
END_COLOR_HUE = 180 #Hue (Matiz) de saída final

HEIGHT= 128
WIDTH= HEIGHT*2 #O dobro pq vai dar append na altura com a segunda imagem

MIN_VALUE=0
MAX_VALUE=255

gif=[]

frame = Image.open('in.gif')
nframes = 0
while frame:
	frame.save( '%s/%s-%s.png' % ('input-img/', os.path.basename('input'), nframes ))
	nframes += 1
	try:
		frame.seek( nframes )
	except EOFError:
		break;

for idx in range(nframes):
    
    current_hue = ((END_COLOR_HUE-INIT_COLOR_HUE)/nframes)*idx
        
    h= np.repeat(np.repeat(current_hue, HEIGHT),WIDTH).reshape(HEIGHT,-1)
    s= np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::-2],WIDTH).reshape(HEIGHT,-1)
    v= np.repeat(np.repeat(MAX_VALUE, HEIGHT),WIDTH).reshape(HEIGHT,-1)
    
    color_white = cv2.merge([h.astype(np.uint8), s.astype(np.uint8), v.astype(np.uint8)])
    
    h= np.repeat(np.repeat(current_hue, HEIGHT),WIDTH).reshape(HEIGHT,-1)
    s= np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::2],WIDTH).reshape(HEIGHT,-1)
    v = np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::2],WIDTH).reshape(HEIGHT,-1)
    
    black_color = cv2.merge([h.astype(np.uint8), s.astype(np.uint8), v.astype(np.uint8)])
    
    palette = np.append(black_color,color_white, axis=0)
    bgr_palette = cv2.cvtColor(palette,cv2.COLOR_HSV2BGR)
    
    img = cv2.imread('input-img/input-'+str(idx)+'.png',0)
    
    final_img = cv2.imread('input-img/input-'+str(idx)+'.png',1)
    
    bgr_indexes = bgr_palette[::,0]
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            final_img[i][j] = bgr_indexes[img[i][j]]
			
    gif.append(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB)) 
     
imageio.mimsave('out.gif', gif)