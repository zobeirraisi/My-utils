import os
import shutil

ROOT = "."

#  EAST
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/EAST/EAST-IC13.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/EAST/EAST-15.zip"
INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/EAST/EAST-coco.zip"

# # PixelLink
# INPUT = (
#     "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PixelLink/Pixel-IC13.zip"
# )
# INPUT = (
#     "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PixelLink/Pixel_IC15.zip"
# )
INPUT = (
    "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PixelLink/Pixel-COCO.zip"
)

# #
# # PAN
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PAN/PAN-IC13.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PAN/PAN-15.zip"
INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PAN/PAN-COCO.zip"


# # MB
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/MB/MB-13.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/MB/MB-15.zip"
INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/MB/MB-COCO.zip"

# # PSENet
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PSENET/PSE-13.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PSENET/PSE-15.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PSENET/PSE-COCO.zip"

# # CRAFT
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/CRAFT/CRAFT-IC13.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/CRAFT/CRAFT-IC15.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/CRAFT/CRAFT-COCO.zip"

# # PMTD
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PMTD/PMTD-IC13.zip"
# INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PMTD/IC15_15.zip"
INPUT = "/media/karim/Data/Me/My-Utils/convertpolyrec/IOU_Python3/PMTD/PMTD-Coco.zip"


INPUT_PATH = os.path.join(INPUT)
BASE = os.path.basename(INPUT_PATH)
EXTRACTED = str(BASE).split(".")[0]
shutil.unpack_archive(INPUT, EXTRACTED, "zip")

gt = os.path.join(ROOT, EXTRACTED)
OUT = f"{EXTRACTED}_REC"
os.makedirs(OUT, exist_ok=True)
out = os.path.join(ROOT, OUT)
# # print(os.listdir(gt))

for txt in os.listdir(gt):
    basename = os.path.splitext(txt)[0]
    # print(basename)
    with open(out + "/" + txt, "w") as f_o:
        with open(gt + "/" + txt) as f:
            lines = [line for line in f.readlines() if line.strip()]
            for line in lines:
                line = line.split(",")
                # print(line)
                p1, p2, p3, p4, p5, p6, p7, p8 = line
                xmin = min(int(p1), int(p3), int(p5), int(p7))
                ymin = min(int(p2), int(p4), int(p6), int(p8))

                xmax = max(int(p1), int(p3), int(p5), int(p7))
                ymax = max(int(p2), int(p4), int(p6), int(p8))

                f_o.write(f"{xmin},{ymin},{xmax},{ymin},{xmax},{ymax},{xmin},{ymax}\n")

        # break

shutil.make_archive(OUT, "zip", OUT)
OUT2 = os.path.join(ROOT, f"{OUT}.zip")
os.system(f"python IOU_Python3/script.py –g=IOU_Python3/gt/gt-pmtd.zip –s={OUT2}")
os.system(f"rm -rf {OUT}")

