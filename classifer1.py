import math
import operator
import numpy as np
import load_test_dataset1 as test
import load_train_dataset1 as train


def euclideandistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)



#finding all the neighbors 
def getneighbors(trainingset,testinstance,trainheader,k):
    distances=[]
    length=len(testinstance)
    for x in range(len(trainingset)):
        dist=euclideandistance(testinstance,trainingset[x],length)
        distances.append((trainingset[x],trainheader[x],dist))
    distances.sort(key=operator.itemgetter(2))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x])
    return neighbors


#finding exact one to the test set prediction
def getresponse(neighbors):
    classvotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][1]
        if response in classvotes:
            classvotes[response]+=1
        else:
            classvotes[response]=1
    sortedvotes=sorted(classvotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedvotes[0][0]


#for finding the accuracy
def getaccuracy(testset,testheader,predictions):
    dos=0
    u2r=0
    r2l=0
    probe=0
    normal=0
    correct=0
    for x in range(len(testset)):
        if testheader[x]==predictions[x]:
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
           
    return (correct/float(len(testset)))*100.0,(dos/float(test.count_dos))*100.0,(r2l/float(test.count_r2l))*100.0,(u2r/float(test.count_u2r))*100.0,(probe/float(test.count_probe))*100.0,(normal/float(test.count_normal))*100.0



def main():
    predictions=[]
    k=5
    for x in range(len(test.dataset)):
        neighbors=getneighbors(train.dataset,test.dataset[x],train.header,k)
        result=getresponse(neighbors)
        predictions.append(result)
        
       
        print('>predicted='+repr(result)+',actual='+repr(test.header[x]))
    total_accuracy,dos_accuracy,r2l_accuracy,u2r_accuracy,probe_accuracy,normal_accuracy=getaccuracy(test.dataset,test.header,predictions)
    
    print("\nTotalTestSet_dos_attackas="+repr(test.header.shape[0]))
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
         
main()