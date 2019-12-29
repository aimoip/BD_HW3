import sys

data = None
current_doc = None
final_views = 0
final_clicks = 0


for line in sys.stdin:
  line = line.strip()
  data = line.split('\t')
  if current_doc == data[0]:
    if data[1]=='Q':
      final_views += int(data[2])
    else:
      final_clicks += int(data[2])
  else:
    if current_doc and final_clicks != 0:
      print('For DocID: {0}\t CTR Is {1}'.format(current_doc,final_clicks/final_views))
    if data[1]=='Q':
      final_views = int(data[2])
      final_clicks = 0
    else:
      final_clicks = int(data[2])
      final_views = 0
    current_doc = data[0]