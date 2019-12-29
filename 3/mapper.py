import  sys
import numpy as np
proccessingQuerryID=-1
checkIfWeHaveClickPattern = 0
checkIfWeHaveQueeryInProccess = 0
ProccessingDocRankList=np.zeros(10)
ProccessingClickList=np.zeros(10)
for line in sys.stdin:
  data = line.strip().split('\t')
  if data[2]=='C':
    ProccessingClickList[ProccessingDocRankList.index(data[3])] += 1
    checkIfWeHaveClickPattern = 1
    checkIfWeHaveQueeryInProccess = 0

  if data[2]=='Q':
    if checkIfWeHaveClickPattern:
      for i in ProccessingDocRankList:
        print('{0}\t{1}\t{2}\t{3}'.format(proccessingQuerryID,i,ProccessingDocRankList.index(i),''.join(map(str,ProccessingClickList.astype(int)))))
      checkIfWeHaveClickPattern=0
    if checkIfWeHaveQueeryInProccess:
      for i in ProccessingDocRankList:
        print('{0}\t{1}\t{2}\t{3}'.format(proccessingQuerryID,i,ProccessingDocRankList.index(i),''.join(map(str,ProccessingClickList.astype(int)))))
    checkIfWeHaveQueeryInProccess = 1 
    proccessingQuerryID = data[3]
    ProccessingDocRankList = data [5:15]
    ProccessingClickList = np.zeros(10)