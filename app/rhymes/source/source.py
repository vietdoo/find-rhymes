import cv2
import numpy as np 
import os
from keras.models import load_model


def run_model(img, model5):
    faces = detect_faces_with_ssd(img)
    mask_label = {0:'MASK',1:'NO MASK'}
    if len(faces) >= 1:
        label = [0 for i in range(len(faces))]
        for i in range(len(faces)):
            (x,y,w,h) = faces[i]["rect"]
            yy = h - y
            xx = w - x
            if (xx > yy):
                y = y - (xx - yy) // 2
                h = y + xx
            if (xx < yy):
                x = x - (yy - xx) // 2
                w = x + yy
            crop = img[y:h,x:w]
            crop = cv2.resize(crop,(128,128))
            crop = np.reshape(crop,[1,128,128,3])/255.0
            mask_result = model5.predict(crop)
            faces[i]['status'] = mask_label[mask_result.argmax()]
    return faces