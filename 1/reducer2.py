import sys

doc = None
current_doc = None
count = 0

for line in sys.stdin:
  line = line.strip()
  doc = line.split('\t')
  if current_doc == doc[0]:
    count += int(doc[1])
  else:
    if current_doc:
      print('For Doc Id: {0}\t There Exists {1} views.'.format(current_doc,count))
    count = int(doc[1])
    current_doc = doc[0]