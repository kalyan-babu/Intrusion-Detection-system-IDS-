import numpy as np
import load_test_dataset1 as test
import load_train_dataset1 as train
from sklearn import tree

def get_accuracy(predict,length,testheader):
    dos=0
    u2r=0
    r2l=0
    probe=0
    normal=0
    correct=0
    for x in range(length):
        if testheader[x]==predict[x]:
            correct+=1
            if testheader[x] in test.dos:
                dos+=1
            if testheader[x] in test.r2l:
                r2l+=1
            if testheader[x] in test.u2r:
                u2r+=1
            if testheader[x] in test.probe:
                probe+=1
            if testheader[x] in test.normal:
                normal+=1
           
    return (correct/float(length))*100.0,(dos/float(test.count_dos))*100.0,(r2l/float(test.count_r2l))*100.0,(u2r/float(test.count_u2r))*100.0,(probe/float(test.count_probe))*100.0,(normal/float(test.count_normal))*100.0



trees= tree.DecisionTreeClassifier()

trees=trees.fit(train.X,train.Y)

predict_trees=trees.predict(test.X)

print(predict_trees)

total_accuracy,dos_accuracy,r2l_accuracy,u2r_accuracy,probe_accuracy,normal_accuracy=get_accuracy(predict_trees,len(test.X),test.header)
print("TotalTestSet_dos_attackas="+repr(test.count_dos))
print("TotalTestSet_r2l_attackas="+repr(test.count_r2l))
print("TotalTestSet_u2r_attackas="+repr(test.count_u2r))
print("TotalTestSet_probe_attackas="+repr(test.count_probe))
print("TotalTestSet_normal_attackas="+repr(test.count_normal))
print('\nTotal_Accuracy:'+repr(total_accuracy)+'%')
print('DOS_Accuracy:'+repr(dos_accuracy)+'%')
print('R2L_Accuracy:'+repr(r2l_accuracy)+'%')
print('U2R_Accuracy:'+repr(u2r_accuracy)+'%')
print('PROBE_Accuracy:'+repr(probe_accuracy)+'%')
print('NORMAL_Accuracy:'+repr(normal_accuracy)+'%')
    
    