import cv2
import numpy as np


cap = cv2.VideoCapture("sport-2.mp4")

if cap.isOpened() == False:
    print("Error opening Video")
else:
    print("Reading the video ...")
i = 0
while cap.isOpened:
    # capture frame by frame
    ret, frame = cap.read()

    if ret == True:

        # cv2.imshow("Video", frame)
        img = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        filename = "video2/frame_" + str(i) + ".jpg"
        # filename1 = "video_brightLAB/frame_" + str(i) + ".jpg"
        # filename2 = "video_darkLAB/frame_" + str(i) + ".jpg"

        # brightLAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        # darkLAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        # L = brightLAB[:, :, 0]
        # A = brightLAB[:, :, 1]
        # B = brightLAB[:, :, 2]

        cv2.imwrite(filename, frame)
        # cv2.imwrite(filename2, darkLAB)
        i += 1

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break

    # cap.release()
    # cv2.destroyAllWindows()
print('Done')
