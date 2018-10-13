import numpy as np
import cv2
import imageio

INIT_COLOR_HUE = 0
END_COLOR_HUE = 120
FRAMES =10

HEIGHT= 128
WIDTH= HEIGHT*2 #O dobro pq vai dar append na altura com a segunda imagem

MIN_VALUE=0
MAX_VALUE=255

for idx in range(FRAMES):
    
    current_hue = ((END_COLOR_HUE-INIT_COLOR_HUE)/FRAMES)*idx
    
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
    
    img = cv2.imread('img2.png',0)
    
    final_img = cv2.imread('img2.png',1)
    
    bgr_indexes = bgr_palette[::,0]
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            final_img[i][j] = bgr_indexes[img[i][j]]
            
    cv2.imwrite('result/img-'+str(idx)+'-colored.jpg', final_img)
    

images = []
filenames=['result/img-0-colored.jpg',
           'result/img-1-colored.jpg',
           'result/img-2-colored.jpg',
           'result/img-3-colored.jpg',
           'result/img-4-colored.jpg',
           'result/img-5-colored.jpg',
           'result/img-6-colored.jpg',
           'result/img-7-colored.jpg',
           'result/img-8-colored.jpg',
           'result/img-9-colored.jpg']
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('result/movie.gif', images)

def write_palettes():    
    for i in range(180):
        hue= i
        h= np.repeat(np.repeat(hue, HEIGHT),WIDTH).reshape(HEIGHT,-1)
        s= np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::-2],WIDTH).reshape(HEIGHT,-1)
        v= np.repeat(np.repeat(MAX_VALUE, HEIGHT),WIDTH).reshape(HEIGHT,-1)
        
        color_white = cv2.merge([h.astype(np.uint8), s.astype(np.uint8), v.astype(np.uint8)])
        
        h= np.repeat(np.repeat(hue, HEIGHT),WIDTH).reshape(HEIGHT,-1)
        s= np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::2],WIDTH).reshape(HEIGHT,-1)
        v = np.repeat(np.array(np.arange(MIN_VALUE, MAX_VALUE))[::2],WIDTH).reshape(HEIGHT,-1)
        
        black_color = cv2.merge([h.astype(np.uint8), s.astype(np.uint8), v.astype(np.uint8)])
        
        full_image = np.append(black_color,color_white, axis=0)
        full_image_bgr = cv2.cvtColor(full_image,cv2.COLOR_HSV2BGR)
        
    cv2.imwrite('palettes/full-color-'+ str(i)+ '.jpg', full_image_bgr)