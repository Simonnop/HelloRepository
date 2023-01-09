import jieba
from collections import Counter

filepath=r'C:\Users\admin\OneDrive\Python.code\mainFiles\Assignments\Chapter 7_练习\远东朝鲜战争.txt'
x=open(filepath,encoding='utf-8')
content=x.read()

all_words=jieba.lcut(content)
all_fre=Counter(all_words)
words_fre=all_fre.most_common(100)
words_fre

exclude_list=['\n','！','：','，','—','“','”','、','《','》','。',' ','的','了','在','和','是','我', '上','他','就','也','中','被','人','一个','有','向','到','地','都','没有','他们','着','时','与','第','后','里','又', '1', '对','要','我们','不','把','为','说', '3','但', ' 2','从','这','个','们','将','以','下','并', '10', '还','来','4','5','这个','已经','时候', '而','开始']

for j in exclude_list:
    for i in words_fre:
        if i[0]==j:
            words_fre.remove(i)

for i in range(15):
    print(words_fre[i])