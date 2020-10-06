# -*- coding: utf-8 -*-
# @Time    : 2020/10/4
# @Author  : Lafe
# @Email   : wangdh8088@163.com
# @File    : visualization.py

import os
import cv2
import time
import numpy as np

def loopshow(res, savep=None):
    if len(res) == 0:
        return False
    ind = 0
    if savep is not None:
        os.makedirs(savep, exist_ok=True)
    while True:
        cv2.imshow('img', res[ind])
        # cv2.imshow("raw, fake, enmap", np.concatenate(res, axis=1))
        k = cv2.waitKey(0)
        if k == ord('d'):
            ind += 1
        elif k == ord('a'):
            ind -= 1
        elif k == ord('c'):
            ind += 10
        elif k == ord('z'):
            ind -= 10
        elif k == ord('q'):
            cv2.destroyAllWindows()
            raise TypeError(" ******** STOP *********")
        elif k == ord('s'):
            save_path = f'{savep}/{int(time.time())}_{int(ind)}.png'
            cv2.imwrite(save_path, res[ind])
            print(' * save image into ', save_path)
        if ind >= len(res) or ind < 0:
            ind = 0


def vis_bgr_data(imgs):
    img_tmp = []
    for img_ins in imgs:
        img, color_type, name = img_ins
        if img is None:
            continue
        if len(img.shape) >3:
            img = img[0]
        if isinstance(img, np.ndarray):
            img_np = img
        else:
            img_np = img.permute(1, 2, 0).cpu().detach().numpy()
        if 'rgb' in color_type:
            img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
            if 'norm' in color_type:
                img_np = (img_np + 1) / 2.0 * 255.0
                img_np = np.clip(img_np, 0, 255)
            if 'heat' in color_type or len(img.shape) == 2:
                img_np = cv2.applyColorMap(img_np, cv2.COLORMAP_JET)

        img_np = img_np.astype(np.uint8)
        try:
            cv2.putText(img_np, name, (20, 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 1)
        except:
            pass
        img_tmp.append(img_np)
    return img_tmp

