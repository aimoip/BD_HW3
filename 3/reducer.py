import sys
currentQueryInProccess = None
currentDocInProccess = None
currentRankInProccess = None
currentPatternInProccess = None
outputList = {}
patternCount = 0

for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    if currentQueryInProccess == data[0] and currentDocInProccess == data[1] and currentRankInProccess == data[2]:
      if currentPatternInProccess == data[3]:
        patternCount += 1
      else:
        if currentPatternInProccess:
          outputList[currentPatternInProccess] = patternCount
        patternCount = 1
        currentPatternInProccess = data[3]
    else:
      if currentQueryInProccess:
        outputList[currentPatternInProccess] = patternCount
        print("for triple [{0} , {1}, {2} ] there exists patterns as follows: {3}".format(int(currentQueryInProccess),int(currentDocInProccess),int(currentRankInProccess), outputList))
      outputList = {}
      currentQueryInProccess,currentDocInProccess,currentRankInProccess,currentPatternInProccess = data
      patternCount = 1
