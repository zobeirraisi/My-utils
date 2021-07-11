import json
import os

file1='instances_train2017.json'
file2='instances_val2017.json'



dataset = {
    'licenses': [],
    'info': {},
    'categories': [],
    'images': [],
    'annotations': []
}


with open(file2) as f:
    file=json.load(f)
    c=1255 # chanhe here for second file
    print(len(file['images']))
    for i in range(len(file['images'])):
        # pass
        file['images'][i]['id']=c
        file['images'][i]['file_name']=f'000{c}.jpg' # chanhe here for second file
        c+=1

    for j in range(len(file['annotations'])):
        file['annotations'][j]['image_id']+=1255 # chanhe here for second file
        file['annotations'][j]['id']+=9722 # chanhe here for second file



    dataset['images']=file['images']
    dataset['annotations']=file['annotations']
    dataset['categories']=file['categories']

with open('new.json', 'w') as f:
  json.dump(dataset, f)
