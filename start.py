from functools import reduce
from pypinyin import pinyin, lazy_pinyin, Style
from gensim.models import word2vec

import re

infile = open("corpus_动物.txt", 'r')        #打开语料库文件
outfile = open("outfile_动.txt", 'w', encoding = 'utf-8')      #创建输出文件

lines = infile.readlines()
for line in lines:
    line = re.sub(r'^\d+\:',"",line)    #去掉句首标号
    line = re.sub(r'\【.+\】',"",line)    #去掉【】中的内容
    for db in line:     #对语料库按单个字符
        if db == ']' or db == '[' or db=='.' or db == ' ' or db == '　' or db == '	':  #去掉特殊字符
            continue
        outfile.write(db)

infile.close()
outfile.close()     #关闭文件
