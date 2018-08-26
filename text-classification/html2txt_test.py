# -*- coding: utf-8 -*-

import sys
import os
import time
from lxml import html
from imp import reload

# 设置utf-8 unicode环境
reload(sys)

# htm文件路径，以及读取文件
path = "1.htm"
content = open(path, "rb").read()
print ('content:{0}'.format(content))
page = html.document_fromstring(content)  # 解析文件
text = page.text_content()  # 去除所有标签
print ('text:{0}'.format(text))  # 输出去除标签后解析结果
