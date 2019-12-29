import sys

for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    if (splits[2]=='Q'):
      docList= splits[5:]
      for doc in docList:
        print("{0}\t{1}\t{2}".format(doc,splits[2],1))
    elif (splits[2]=='C'):
      print('{0}\t{1}\t{2}'.format(splits[3],splits[2],1))