import cv2 as cv
import numpy as np
import copy

origin = cv.imread('/home/hack/PycharmProjects/keras-yolo3-master/data/th-2.png')
print(origin.shape)
black = np.zeros([*origin.shape])
copied = copy.deepcopy(origin)

detected = [(289, 3), (371, 63), (252, 10), (411, 272)]
detected = [(1143, 353), (1232, 496), (846, 451), (1009, 669), (473, 432), (661, 929), (973, 326), (1069, 460),
            (1181, 519), (1424, 808), (212, 265), (417, 462), (664, 375), (880, 562), (487, 452), (643, 619),
            (809, 373), (897, 517), (1359, 408), (1535, 651), (929, 670), (1253, 941)]
# rectangle
for i in range(len(detected) // 2):
    cv.rectangle(origin, detected[2 * i], detected[2 * i + 1], (0, 0, 255), 2)

# roi
for i in range(len(detected) // 2):
    color = np.ones(
        [detected[2 * i + 1][1] - detected[2 * i][1], detected[2 * i + 1][0] - detected[2 * i][0], 3]) * 255
    if i <= 2:
        color[:, :, 1:2] = 0
    else:
        color[:, :, 0:1] = 0
    print(detected[2 * i], detected[2 * i + 1])
    copied[detected[2 * i][1]:detected[2 * i + 1][1], detected[2 * i][0]:detected[2 * i + 1][0]] = color

    black[detected[2 * i][1]:detected[2 * i + 1][1], detected[2 * i][0]:detected[2 * i + 1][0]] = color
cv.imshow('bim', origin)
cv.imshow('copied', copied)
cv.imshow('black', black)
cv.waitKey()
