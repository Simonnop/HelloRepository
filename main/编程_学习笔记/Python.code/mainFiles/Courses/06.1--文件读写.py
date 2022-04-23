'''
    文件读写

    基础案例:读取txt文件
'''
# 将文件赋予变量
filepath=r'C:\Users\admin\OneDrive\Python.code\mainFiles\FilesToRead\诗.txt'

# open函数,注意选择encoding
x=open(filepath,encoding='utf-8')

# 使用read方法,返回一个字符串
# 读完之后指针移至结尾,x会为空
content=x.read()

# 每次读一行
line=x.readline()
line

# 以\n换行符为界分割为列表
y=content.split('\n')
y

# close掉文件
x.close()

'''
    读取CSV文件

    数据之间以 , 隔开
'''

import csv

filepath=r'C:\Users\admin\OneDrive\Python.code\mainFiles\FilesToRead\global-malaria-deaths-by-world-region.csv'
x=open(filepath,encoding='utf-8')

# 使用csv的reader方法快速读取csv文件
# 获得一个嵌套的列表
# 其中数据都是string类型
content=csv.reader(x)
list(content)

# 类型: _csv.reader
type(content)

# next 方法,显示一行,指针会移动,将其移除
# 通常需要移除第一列的表头
next(content)

# 通过列表存储各项数据
# 默认为string,转换为int
year=[]
deaths=[]
for i in content:
    if i[0]=='South-East Asia':
        year.append(int(i[2]))
        deaths.append(int(i[3]))

# zip方法,依照顺序组合
for i in zip(year,deaths):
    print(i)

'''
    词汇统计(英文)
'''

# 将文件赋予变量
filepath=r'C:\Users\admin\OneDrive\Python.code\mainFiles\FilesToRead\Translation.txt'

# open函数,注意选择encoding
x=open(filepath,encoding='utf-8')

# 使用read方法,返回一个字符串
# 读完之后指针移至结尾,x会为空
content=x.read()

# 正则表达式
# 使用正则表达式对单词进行切分
# '\W' 表示除 字母 数字 下划线外的所有字符, + 表示匹配一次或多次
import re
words=re.split(r'\W+',content)
words
from collections import Counter
# 统计字数
y=Counter(words)
# lambda 为次数排序
# 可以用 most_common 代替
y=sorted(y.items(),key=lambda i:i[1],reverse=True)
y

'''
    中文读写
'''
# 中文拆分,使用包:解霸
import jieba
from collections import Counter
passage = '中华人民共和国，简称“中国”，成立于1949年10月1日，位于亚洲东部，太平洋西岸，是工人阶级领导的、以工农联盟为基础的人民民主专政的社会主义国家，以五星红旗为国旗、《义勇军进行曲》为国歌，国徽内容为国旗、天安门、齿轮和麦稻穗，通用语言文字是普通话和规范汉字，首都北京，是一个以汉族为主体、56个民族共同组成的统一的多民族国家。中国陆地面积约960万平方千米，东部和南部大陆海岸线1.8万多千米，内海和边海的水域面积约470多万平方千米。海域分布有大小岛屿7600多个，其中台湾岛最大，面积35798平方千米。中国同14国接壤，与8国海上相邻。省级行政区划为23个省、5个自治区、4个直辖市、2个特别行政区。中国是世界上历史最悠久的国家之一，有着光辉灿烂的文化和光荣的革命传统，世界遗产数量全球领先。1949年新中国成立后，进入社会主义革命和建设时期，1956年实现向社会主义过渡，此后社会主义建设在探索中曲折发展。“文化大革命”结束后实行改革开放，沿着中国特色社会主义道路，集中力量进行社会主义现代化建设。经过长期努力，中国特色社会主义进入了新时代。中国是世界上人口最多的发展中国家，国土面积居世界第三位，是世界第二大经济体，并持续成为世界经济增长最大的贡献者，2020年经济总量突破100万亿元。中国坚持独立自主的和平外交政策，是联合国安全理事会常任理事国，也是许多国际组织的重要成员，被认为是潜在超级大国之一。'
# 使用replace方法，替换文段中的标点为空
for i in ['，','“','”','、','《','》','。',' ']:
    passage=passage.replace(i,'')
# jieba拆分方法
words=jieba.lcut(passage)
fre=Counter(words)
y=sorted(fre.items(),key=lambda i:i[1],reverse=True)
y









