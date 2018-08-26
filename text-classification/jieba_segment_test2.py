# -*- coding: utf-8 -*-

import sys  
import os
import jieba


seg_list = jieba.cut("小明终于在1995年从北京清华大学毕业了。")
print(" ".join(seg_list))

