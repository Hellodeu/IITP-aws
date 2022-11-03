import os
import buildingCollapse
import os.path as osp
import random
import cv2

UPLOAD_DIR = "C:\\Users\\uSER\\Desktop\\fastapi\\static"
UPLOAD_DIR_original = "C:\\Users\\uSER\\Desktop\\fastapi\\staticoriginal"
#list = []
#for i in UPLOAD_DIR:
#    list.append(i)
#print(UPLOAD_DIR)    
#length = int(len(list))
size = int(len(os.listdir(UPLOAD_DIR)))
print(size)
n = random.randint(0,size)
print(n)
#if 0 < n < 23:
#    print("no")
if 0 <= n < 5:
        print('ok')
        
elif 4 < n < 11:
        print('ok')
        
elif 10 < n < 16:
       print('ok')
        
elif 15 < n < 21:
        print('ok')
          
elif 20< n <27:
        print('ok')
else:
    print('no')
#img=os.listdir(UPLOAD_DIR_original)[0]
#test_real_path = osp.realpath(osp.join(UPLOAD_DIR_original,img))
#img1 = cv2.imread(test_real_path)
#height, width, channel = img1.shape
#m = cv2.getRotationMatrix2D((width/2, height/2), 15, 1)
#img2 = cv2.warpAffine(img1, m, (width, height))
#cv2.imshow("hanc",img2)