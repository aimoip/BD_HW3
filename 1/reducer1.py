import sys

query = None
current_query = None
duplicatedIncludedList = []

for line in sys.stdin:
    line = line.strip()
    query = line.split('\t')
    if current_query == query[0]:
      duplicatedIncludedList = duplicatedIncludedList + query[1:]
    else:
      if current_query:
        for i in list(set(duplicatedIncludedList)):
          print("{0}\t{1}".format(i,1))
      duplicatedIncludedList = query[1:]
      current_query = query[0]

if current_query == query[0]: 
  print("{0}\t{1}".format(i,1))