# -*- coding: utf-8 -*-
# @Time    : 2020/10/4
# @Author  : Lafe
# @Email   : wangdh8088@163.com
# @File    : visualization.py

import os
import cv2
import time

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

