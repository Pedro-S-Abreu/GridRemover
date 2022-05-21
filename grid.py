import numpy as np
import cv2, random
import matplotlib.pyplot as plt
grid_width= 141
grid_height= 141
grid_x_offxet= 139
grid_y_offset= 139
y_thicknesss=5
X_thicknesss=5

# %matplotlib inline  # if you are running this code in Jupyter notebook

# reads image 'opencv-logo.png' as grayscale
img = cv2.imread('jdu8mhqck4961.jpg') 
#cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height,width,_ = img.shape
y = grid_y_offset
linemid_x  = round((y_thicknesss-1 )/2)
thick_range_y = round((y_thicknesss-1 )/2)
thick_range_x = round((X_thicknesss-1 )/2)
print(thick_range_y);
def mark(img):
    for y in range(grid_y_offset, height, grid_height-1 ):
        for x in range(0,width-1):
            for y_ in range((y-thick_range_y),(y+thick_range_y+1)):
                    try:
                        img[y_, x]=[255, 0, 0]
                    except:
                        pass    
    for x in range(grid_x_offxet, width, grid_width-1 ):
        for y in range(0,height-1):
            for x_ in range((x-thick_range_x),(x+thick_range_x+1)):
                    try:
                        img[y, x_]=[255, 0, 0]
                    except:
                        pass 
def clear_grid(img):
    for y in range(grid_y_offset, height, grid_height-1 ):
        for x in range(0,width-1):
            cl1=None
            cl2=None
            try: cl1=np.square(img[y-thick_range_y-1, x]/255)
            except:pass
            try: cl2=np.square(img[y+thick_range_y+1, x]/255)
            except:pass
            if cl1 is None:
                cl1 = cl2
            if cl2 is None:
                cl2 = cl1    
            for i in range((-thick_range_y),(+thick_range_y+1)):
                    ratio= (i+thick_range_y)/(thick_range_y+1) 
                    try:      
                        img[y+i, x]=np.sqrt(cl1*(1-ratio)+cl2*ratio)*255#[255, 0, 0]
                        #print(img[y+i, x])
                    except:
                        pass    
    for x in range(grid_x_offxet, width, grid_width-1 ):
        for y in range(0,height-1):
            cl1=None
            cl2=None
            try: cl1=np.square(img[y, x-thick_range_x-1]/255)
            except:pass
            try: cl2=np.square(img[y, x+thick_range_x+1]/255)
            except:pass
            if cl1 is None:
                cl1 = cl2
            if cl2 is None:
                cl2 = cl1    
            for i in range((-thick_range_x),(+thick_range_x+1)):
                    ratio= (i+thick_range_x)/(thick_range_x+1) 
                    try:
                        img[y, x+i]=np.sqrt(cl1*(1-ratio)+cl2*ratio)*255
                        
                    except:
                        pass   
if 0:                     
    for y in range(0, height, 135 ):  
        for x in range(0, width, 135 ):

            # font
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            # org
            org = (x+random.randint(-10, 10), y+random.randint(-10, 10))
            
            # fontScale
            fontScale =  random.randint(1, 3)
            
            # Blue color in BGR
            color = (255, 255, 255)
            
            # Line thickness of 2 px
            thickness = random.randint(1, 3)
            
            # Using cv2.putText() method
            img = cv2.putText(img, 'pwlae', org, font, 
                            fontScale, color, thickness, cv2.LINE_AA)


clear_grid(img)
filename = 'out.jpg'
cv2.imwrite(filename, img, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow('1',img)
print('Image Dimensions :', img.shape)
cv2.waitKey(0) 

#closing all open windows 
cv2.destroyAllWindows() 
