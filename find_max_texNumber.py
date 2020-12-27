import os
#root folder of gt text
root='Training_GT'

def remove_notext(lines,remove=None):
    if remove:
        new_lines=[]
        for l in lines:
            if l.split(',')[-1] !='###\n':
                new_lines.append(l)
    else:
        new_lines=lines
    return new_lines

max=0
for txtfie in os.listdir(root):
    with open(os.path.join(root,txtfie)) as T:
        lines=T.readlines()
        newlines=remove_notext(lines,remove=True)
        if len(newlines) > max:
            max= len(newlines)
            print(f'The max line is {max}')

