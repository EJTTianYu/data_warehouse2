#coding=utf-8
'''
@author=Wangminhao Gou
'''
import csv
import math
import random

input_csv=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/bank-additional-full.csv'
output_csv=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/bank_full_age_process.csv'
output_csv2=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/bank_full_duration_process.csv'
output_csv3=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/bank_full_euribor3m_process.csv'
output_csv4=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/bank_full_process.csv'
output_csv5=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/bank_train.csv'
output_csv6=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/bank_test.csv'


#从原始的csv中获取年龄数据，输出年龄数据的最大最小值，以便后续处理
def age_read():
    with open(input_csv,'r') as inp1:
        lines=list(csv.reader(inp1,delimiter=';'))
        #print(lines[0])
        age=[]
        for i in range(1,len(lines)):
            age.append(lines[i][0])
        print(min(age))
        print(max(age))
#从原始的csv中获取各种行数的数据,观察数据的形式
def atti_read(k):
    with open(output_csv3,'r') as inp1:
        lines=list(csv.reader(inp1))
        result=[]
        for i in range(1,len(lines)):
            result.append(lines[i][k])
    print(list(set(result)))
    return list(set(result))
#对数据的年龄进行离散化处理，将数据存储到新的csv中以便后续处理
def age_process():
    with open(input_csv,'r') as inp1,open(output_csv,'w') as out1:
        lines=list(csv.reader(inp1,delimiter=';'))
        writer=csv.writer(out1)
        writer.writerow(lines[0])
        for i in range(1,len(lines)):
            lines[i][0]=int(lines[i][0])//10
            writer.writerow(lines[i])
        print('complete')
#对euribor3m进行离散化处理，将数据存储到新的csv以便后续处理
def euribor3m_process():
    with open(output_csv2,'r') as inp1,open(output_csv3,'w') as out1:
        lines = list(csv.reader(inp1))
        writer=csv.writer(out1)
        writer.writerow(lines[0])
        for i in range(1,len(lines)):
            lines[i][17]=int(float(lines[i][17])//0.5)
            writer.writerow(lines[i])
        print('complete')
#查看duration的值空间
def duration_read():
    with open(output_csv,'r') as out1:
        lines=list(csv.reader(out1))
        duration=set()
        for i in range(1,len(lines)):
            duration.add(lines[i][10])
        print(duration)
#删除duration的属性列
def duration_delete():
    with open(output_csv,'r') as inp1,open(output_csv2,'w') as out1:
        lines=list(csv.reader(inp1))
        writer = csv.writer(out1)
        for i in range(0,len(lines)):
            lines[i].pop(10)
            writer.writerow(lines[i])
        print('complete')
#总体信息量计算函数，用于筛选出比较重要的列
def cal_i_full():
    p=0
    n=0
    with open(output_csv2,'r') as out1:
        lines=list(csv.reader(out1))
        for i in range(1,len(lines)):
            if(lines[i][19]=='yes'):
                p+=1
            else:
                n+=1
    I=-p/(p+n)*math.log(p/(p+n),2)-n/(p+n)*math.log(n/(p+n),2)
    print(I,p,n)
#单信息量计算函数
def cal_i(p,n):
    if(p==0 or n==0):
        i=0
        return i
    else:
        i=-p/(p+n)*math.log(p/(p+n),2)-n/(p+n)*math.log(n/(p+n),2)
        return i
#e值的计算
def cal_e(value_list,m):
    e=0
    p_list=[0]*len(value_list)
    n_list=[0]*len(value_list)
    with open(output_csv3,'r') as out1:
        lines=list(csv.reader(out1))
        for i in range(1,len(lines)):
            for k in range(0,len(value_list)):
                if(lines[i][m]==value_list[k]):
                    if(lines[i][19]=='yes'):
                        p_list[k]+=1
                    else:
                        n_list[k]+=1
    for j in range(0,len(p_list)):
        e+=(p_list[j]+n_list[j])*cal_i(p_list[j],n_list[j])
    print(p_list)
    print(n_list)
    print(e)
#选取信息增益值比较大的几列
def data_ex():
    with open(output_csv3,'r') as inp1,open(output_csv4,'w') as out1:
        lines = list(csv.reader(inp1))
        writer=csv.writer(out1)
        for i in range(0,len(lines)):
            p=[]
            p.append(lines[i][0])
            p.append(lines[i][8])
            for k in range(11,20):
                p.append(lines[i][k])
            writer.writerow(p)
#将数据集随机分为训练集以及测试集
def data_div():
    row_num=int(41188*0.3)
    with open(output_csv3,'r') as inp1,open(output_csv5,'w') as out1,open(output_csv6,'w') as out2:
        lines = list(csv.reader(inp1))
        writer1=csv.writer(out1)
        writer2=csv.writer(out2)
        writer1.writerow(lines[0])
        writer2.writerow(lines[0])
        lines.pop(0)
        test=random.sample(lines,row_num)
        for item in test:
            lines.remove(item)
        for line in lines:
            writer1.writerow(line)
        for row in test:
            writer2.writerow(row)
    print(len(lines)+len(test))
if __name__=="__main__":
    data_div()