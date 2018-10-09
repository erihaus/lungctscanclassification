#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 01:10:47 2017

@author: erihaus
"""
import numpy as np
import cv2
import scipy.misc

file_name = "0a38e7597ca26f9374f8ea2770ba870d.npy"
img = np.load(file_name)
maximum = img.max()
minimum = img.min()
img2 = cv2.convertScaleAbs(img, None, 255/(maximum))
res, img3= cv2.threshold(img2, 70, 255, cv2.THRESH_TOZERO)
scipy.misc.toimage(img3, cmin=0.0, cmax=255).save("yes")
    