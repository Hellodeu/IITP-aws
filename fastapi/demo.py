from typing import List
from fastapi import FastAPI,Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
import os
import os.path as osp
import buildingCollapse
import random
import gunicorn


UPLOAD_DIR = "C:\\Users\\uSER\\Desktop\\fastapi\\static"
UPLOAD_DIR_original = "C:\\Users\\uSER\\Desktop\\fastapi\\staticoriginal"

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") 
app.mount("/staticoriginal", StaticFiles(directory="staticoriginal"), name="staticoriginal") 
templates = Jinja2Templates(directory="templates")
@app.get("/imagedown")
async def imagedownload(request:Request):
    length = int(len(os.listdir(UPLOAD_DIR))-1)
    n = random.randint(0,length)
    if 0 <= n < 5:
        img_original=os.listdir(UPLOAD_DIR_original)[0]
        
    if 4 < n < 11:
        img_original=os.listdir(UPLOAD_DIR_original)[1]
        
    if 10 < n < 16:
        img_original=os.listdir(UPLOAD_DIR_original)[2]
        
    if 15 < n < 21:
        img_original=os.listdir(UPLOAD_DIR_original)[3]
          
    if 20< n <26:
        img_original=os.listdir(UPLOAD_DIR_original)[4]    
             
    img=os.listdir(UPLOAD_DIR)[n]
    real_img = (osp.realpath(img))
    print(real_img)
    test_real_path = osp.realpath(osp.join(UPLOAD_DIR,img))    
    original_real_path = osp.realpath(osp.join(UPLOAD_DIR_original,img_original))    
    mean = buildingCollapse.match_images(original_real_path,test_real_path)
    if mean<45:
        check = "Normal"
    else:
        check = "Abnormal"
    return templates.TemplateResponse("imagedown.html",{'request':request,'img':img,'img_original':img_original,"check":check})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)