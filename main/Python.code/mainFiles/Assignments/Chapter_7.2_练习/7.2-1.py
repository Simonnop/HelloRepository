import jieba
from collections import Counter
import matplotlib.pyplot as plt

def FindMostCommon(content,exclude_list):

    x=open(content,encoding='utf-8')
    content=x.read()
    all_words=jieba.lcut(content)
    all_fre=Counter(all_words)
    words_fre=all_fre.most_common(100)

    for j in exclude_list:
        for i in words_fre:
            if i[0]==j:
                words_fre.remove(i)

    return [words_fre[i] for i in range(15)]

def ShowFre(title,content,exclude_list):

    words=[]
    times=[]
    for i in FindMostCommon(content,exclude_list):
        words.append(i[0])
        times.append(i[1])

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False    
    plt.bar(range(len(words)),times)
    plt.xticks(range(len(words)),words)
    plt.title(title)
    plt.xlabel('动词及名词')
    plt.ylabel('词频')
    for x,y in enumerate(times):
        plt.text(x,y,'%s' %round(y,1),ha='center')

filepath1=r'C:\Users\admin\OneDrive\Python.code\mainFiles\Assignments\Chapter_7.2_练习\远东朝鲜战争.txt'
filepath2=r'C:\Users\admin\OneDrive\Python.code\mainFiles\Assignments\Chapter_7.2_练习\志愿军抗美援朝战史.txt'

exclude_list1=['\n','！','：','，','—','“','”','、','《','》','。',' ','的','了','在','和','是','我', '上','他','就','也','中','被','人','一个','有','向','到','地','都','没有','他们','着','时','与','第','后','里','又', '1', '对','要','我们','不','把','为','说', '3','但', ' 2','从','这','个','们','将','以','下','并', '10', '还','来','4','5','这个','已经','时候', '而','开始']
exclude_list2=['\n','！','：','，','—','“','”','、','《','》','。',' ','的','了','在','和','是','我', '上','他','就','也','中','被','人','一个','有','向','到','地','都','没有','他们','着','时','与','第','后','里','又', '1', '对','要','我们','不','把','为','说', '3','但', ' 2','从','这','个','们','将','以','下','并', '10', '还','来','4','5']

ShowFre('远东朝鲜战争',filepath1,exclude_list1)
plt.show()
ShowFre('志愿军抗美援朝战史',filepath2,exclude_list2)
plt.show()






