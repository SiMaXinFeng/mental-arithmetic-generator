import random     #引入库函数
import time            #引入库函数
score=0                  #得分初始化
i=1                           
t1=time.time()        #时间值起点
while(i<11):
                a=random.randint(0,100)      #随机生成一个数
                b=random.randint(0,100)
                print(a,"+",b,)
                c=int(input("answer="))
                if c==a+b:          #判断答案是否正确
                                score=score+10
                i=i+1         #题目数量加1
t2=time.time()        #时间值终点
print("用时：",t2-t1)      #打印所用时间
print("得分：",score)  #打印分数
input()#双击运行时，程序结束不闪退

