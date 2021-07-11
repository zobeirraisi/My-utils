import json
import os
import json
import glob
from natsort import natsorted

File1='a.json'
File2='b.json'


dataset = {
    'licenses': [],
    'info': {},
    'categories': [],
    'images': [],
    'annotations': []
}



result = []
for f in natsorted(glob.glob("*.json")):
    with open(f, "rb") as infile:
        result.append(json.load(infile))
        # print(result[-1]['images'])


dataset['images']=(result[0]['images']+result[1]['images'])
# print(dataset['images'][0])
dataset['annotations']=(result[0]['annotations']+result[1]['annotations'])
dataset['categories']=result[0]['categories']

with open('instances_train2017.json', 'w') as f:
  json.dump(dataset, f)

