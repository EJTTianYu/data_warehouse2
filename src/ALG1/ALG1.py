#coding=utf-8
'''
@author=Wangminhao Gou
'''
import csv
train=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/train/bank_train.csv'
test=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/test/bank_test.csv'
output_csv=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/test/bank_train_result_ALG1.csv'
p_yes_train=3238/28832
a = [3, 'technician', 'married', 'professional.course', 'no', 'yes', 'no', 'cellular', 'sep', 'wed', 1, 999, 0,
     'nonexistent', -1.1, 94.199, -37.5, 1, 4963.6, 'yes']

#返回train的行数和yes的行数
def train_num():
    num_yes=0
    with open(train,'r') as inp1:
        lines=list(csv.reader(inp1))
        for i in range(0,len(lines)):
            if lines[i][19]=='yes':
                num_yes+=1
        return (len(lines)-1),num_yes
#返回test的行数
def test_num():
    with open(test,'r') as inp1:
        lines=list(csv.reader(inp1))
        return (len(lines)-1)
#返回类别为yes时，第m列的值为参数value的概率
def cal_p_yes(value,m):
    t=0
    num_yes=3238
    with open(train,'r') as inp1:
        lines=list(csv.reader(inp1))
        for i in range(0,len(lines)):
            if lines[i][19]=='yes' and lines[i][m]==str(value):
                t+=1
    return t/num_yes
#返回第m列的值为参数value的概率
def cal_p(value,m):
    t=0
    num_all=28832
    with open(train,'r') as inp1:
        lines=list(csv.reader(inp1))
        for i in range(0,len(lines)):
            if lines[i][m]==str(value):
                t+=1
    return t/num_all
#返回一个测试数据属于yes类的概率
def p_yes(data_lst):
    p_intial=1
    for i in range(0,len(data_lst)-1):
        p_up=cal_p_yes(data_lst[i],i)
        p_down=cal_p(data_lst[i],i)
        p_intial=p_intial*p_up/p_down
    if p_intial*p_yes_train>0.5:
        data_lst[len(data_lst)-1]='yes'
    else:
        data_lst[len(data_lst)-1] = 'no'
    return data_lst
if __name__=='__main__':
    with open(test,'r') as inputFil1,open(output_csv,'w') as outputFile1:
        lines = list(csv.reader(inputFil1))
        writer = csv.writer(outputFile1)
        writer.writerow(lines[0])
        for i in range(1,len(lines)):
            writer.writerow(p_yes(lines[i]))
            print(i)
