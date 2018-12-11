#coding=utf-8
'''
@author=Wangminhao Gou
'''
import csv
train_set=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/train/bank_train.csv'
test_set=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/test/bank_test.csv'
train_result=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/test/bank_train_result_ALG2.csv'

a = [3, 'technician', 'married', 'professional.course', 'no', 'yes', 'no', 'cellular', 'sep', 'wed', 1, 999, 0,
     'nonexistent', -1.1, 94.199, -37.5, 1, 4963.6, 'yes']
nume_distance={'age':8.0,'campaign':55.0,'pdays':999.0,'previous':7.0,'emp.var.rate':4.8,'cons.price.idx':2.566,
               'cons.conf.idx':23.9,'euribor3m':9.0,'nr.employed':264.5}
#对数据型数据读取最大最小值，方便计算距离
def nume_read(k):
    value_lst=[]
    with open(train_set,'r') as inp1:
        lines=list(csv.reader(inp1))
        for i in range(1,len(lines)):
            value_lst.append(float(lines[i][k]))
    print(max(value_lst)-min(value_lst))
    print(min(value_lst))
#对数据进行距离的计算
def dist(item_lst):
    distance=[1.0]*19
    dis_lst=[]
    with open(train_set,'r') as inp1:
        lines = list(csv.reader(inp1))
        for i in range(1,len(lines)):
            sum_dist=0
            distance[1]=abs(float(item_lst[0])-float(lines[i][0]))/8.0
            for k in range(1,10):
                distance[k]=0 if(item_lst[k]==lines[i][k]) else 1
            distance[10]=abs(float(item_lst[10])-float(lines[i][10]))/55.0
            distance[11] = abs(float(item_lst[11]) - float(lines[i][11])) / 999.0
            distance[12]= abs(float(item_lst[12]) - float(lines[i][12])) / 7.0
            distance[13]=0 if(item_lst[13]==lines[i][13]) else 1
            distance[14]=abs(float(item_lst[14])-float(lines[i][14]))/4.8
            distance[15]=abs(float(item_lst[15])-float(lines[i][15]))/2.566
            distance[16]=abs(float(item_lst[16])-float(lines[i][16]))/23.9
            distance[17]=abs(float(item_lst[17])-float(lines[i][17]))/9.0
            distance[18] = abs(float(item_lst[18]) - float(lines[i][18])) / 264.5
            sum_dist=sum(distance)
            dis_lst.append([lines[i][19],sum_dist])
    dis_lst.sort(key=lambda x:x[1])
    #print(dis_lst)
    return dis_lst
#k近邻算法
def kNN(k):
    with open(test_set,'r') as inputFile1,open(train_result,'w') as outputFile1:
        rows=list(csv.reader(inputFile1))
        writer=csv.writer(outputFile1)
        writer.writerow(rows[0])
        for m in range(1,len(rows)):
            neigh=dist(rows[m])
            yes_num=0
            for z in range(0,k):
                if(neigh[z][0]=='yes'):
                    yes_num+=1
            if yes_num>k*0.2:
                rows[m][19]='yes'
            else:
                rows[m][19]='no'
            writer.writerow(rows[m])
            print(m)
if __name__=='__main__':
    kNN(20)