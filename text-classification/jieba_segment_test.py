# -*- coding: utf-8 -*-

import jieba

# cut_all = false 表示精确分词模式 lcut返回list
seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=False)
print("Default Mode:", " ".join(seg_list))  # 默认模式

# 默认是精确粉刺模式
seg_list = jieba.cut("小明1995年毕业于北京清华大学")
print("  ".join(seg_list))

# 全模式分出来的词更多些
seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=True)
print("Full Mode:", "/ ".join(seg_list))  # 全模式

#
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print("/  ".join(seg_list))

