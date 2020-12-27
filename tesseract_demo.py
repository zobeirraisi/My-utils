import os
from PIL import Image
import pytesseract
from natsort import natsorted
from tqdm import tqdm

root = "/media/karim/Data/Me/Datasets/Recognition/coco2/COCO2-Alphanumeric"
filename = root.split("/")[-1] + ".txt"
gt = os.path.join(root, "gt.txt")

count = 0
with open(gt) as gt:
    line = gt.readlines()
    All = len(line)
    t = tqdm(line, total=len(line))
    for l in t:
        img = os.path.join(f"{root}/out", l.split(",")[0])
        label = l.split(",")[1].rstrip()
        image = Image.open(img)
        stR = pytesseract.image_to_string(image)
        line = stR.splitlines()
        word = max(line, key=len)
        if label == word:
            count += 1
        wra = (count / All) * 100
        t.set_description("WRA= %f" % wra)

