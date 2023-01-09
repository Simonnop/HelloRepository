# 2.25 控制流

'''
    Python中的语句块
        - 使用 缩进 来划分语句块
        - 按 Tab 键来进行缩进
'''

'''
    if 语句
        语法
            if 条件:
                ...
            elif 条件:
                ...
            else:
                ...
        - elif 即为 else if
'''

'''
    while 循环
        语法
            while 条件:
                ...
            else:
                ...
        - while语句可以跟else语句,当while循环的条件变为False时执行
        - while被break打断时,不会执行else
'''

# 猜数游戏

answerNum=23
running=True

print('''There is a hidden integer in this program.
You can guess what it is by entering your guess.''')

while running:
    guessNum=int(input('Please enter your guess:'))

    if guessNum==answerNum:
        print('Congratulations! You guessed it!')
        running=False
    elif guessNum<answerNum:
        print('No,the hidden number is larger than',guessNum)
    else:
        print('No,the hidden number is smaller than {}'.format(guessNum))
        
print('Done')

'''
    for 循环
        语法
            for 变量 in range(范围值):
                ...
        - for语句可以跟else语句,当for循环的条件变为False时执行
        - for被break打断时,不会执行else

        - range()是一个函数,用于生成一个序列
            语法 
                range(start,stop[,step])
            其中start默认为0,step(间隔)为可选项,默认为1
'''

for i in range(10):
    print(i)

# 隔一个打印
for i in range(2,10,2):
    print(i)

'''
    break 语句: 终止循环
    continue 语句: 结束本次循环

    Python中没有 switch 循环
'''

