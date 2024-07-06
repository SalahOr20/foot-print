# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:17:53 2023

@author: Thuy-trang
"""

import os
path = "C:/Users/Thuy-trang/Downloads/e6b05a89-44a0-46d5-aa85-dfe73eff11d5"
imgs = os.listdir(path)
for img in imgs :
    if "rabbit" not in img : 
        os.remove(path + "/" + img)
        

