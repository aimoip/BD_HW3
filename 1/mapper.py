import sys
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    if (splits[2]=='Q'):
      print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}'.format(splits[3],splits[5],splits[6],splits[7],splits[8],splits[9],splits[10],splits[11],splits[12],splits[13],splits[14]))