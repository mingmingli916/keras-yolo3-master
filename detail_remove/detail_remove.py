import cv2 as cv
import numpy as np
import copy

origin = cv.imread('/home/hack/PycharmProjects/keras-yolo3-master/data/th2.jpg')
print(origin.shape)
black = np.zeros([*origin.shape])
copied = copy.deepcopy(origin)

detected = [(81, 247), (97, 261), (52, 250), (74, 273), (430, 337), (519, 428), (115, 295), (153, 355), (233, 315),
            (297, 379), (441, 269), (475, 296), (303, 299), (373, 369), (71, 264), (106, 323), (252, 278), (285, 312),
            (382, 279), (452, 392), (275, 293), (315, 361), (281, 394), (431, 535), (0, 326), (102, 468), (95, 345),
            (242, 522)]

detected = [(1050, 269), (1190, 411), (1212, 242), (1321, 378), (187, 331), (403, 502), (1232, 234), (1329, 383),
            (1050, 269), (1190, 411), (354, 322), (684, 584), (624, 268), (746, 444), (726, 593), (1103, 1062),
            (1052, 349), (1431, 994), (787, 241), (906, 383)]
# rectangle
for i in range(len(detected) // 2):
    cv.rectangle(origin, detected[2 * i], detected[2 * i + 1], (0, 0, 255), 2)

# roi
for i in range(len(detected) // 2):
    color = np.ones(
        [detected[2 * i + 1][1] - detected[2 * i][1], detected[2 * i + 1][0] - detected[2 * i][0], 3]) * 255
    if i <= 2:
        color[:, :, 1:2] = 0
    elif i <= 6:
        color[:, :, (0, 2)] = 0
    else:
        color[:, :, 0:1] = 0
    print(detected[2 * i], detected[2 * i + 1])
    copied[detected[2 * i][1]:detected[2 * i + 1][1], detected[2 * i][0]:detected[2 * i + 1][0]] = color

    black[detected[2 * i][1]:detected[2 * i + 1][1], detected[2 * i][0]:detected[2 * i + 1][0]] = color
cv.imshow('bim', origin)
cv.imshow('copied', copied)
cv.imshow('black', black)
cv.waitKey()
