#coding=utf-8
'''
@author=Wangminhao Gou
'''
import csv

inputFile1=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/test/bank_test.csv'
inputFile2=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/test/bank_train_result_ALG1.csv'
inputFile3=r'/Users/tianyu/PycharmProjects/data_warehouse_task2/dataset/data_set/test/bank_train_result_ALG2.csv'
#计算TP,FN,FP,TN并返回
def cal_para(file):
    TP = FN = FP = TN = 0
    with open(inputFile1,'r') as inp1,open(file,'r') as inp2:
        lines=list(csv.reader(inp1))
        rows=list(csv.reader(inp2))
        for i in range(1,len(lines)):
            if (lines[i][19]=='yes') and (rows[i][19]=='yes'):
                TP+=1
            elif (lines[i][19]=='yes') and (rows[i][19]=='no'):
                FN+=1
            elif (lines[i][19]=='no') and (rows[i][19]=='yes'):
                FP+=1
            else:
                TN+=1
    precision=TP/(TP+FP)
    recall=TP/(TP+FN)
    print(TP,FN,FP,TN)
    return precision,recall
#计算最后结果的F-score
def fscore(pre,rec,k):
    f_score=(1+k**2)*pre*rec/(k**2*pre+rec)
    print(f_score)

if __name__=='__main__':
    a,b=cal_para(inputFile3)
    fscore(a,b,3)