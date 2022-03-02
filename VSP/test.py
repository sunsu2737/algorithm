# import cv2
# import numpy as np
# lenna = cv2.imread("lenna.png",)
# lenna_gray = cv2.cvtColor(lenna, cv2.COLOR_BGR2GRAY)
# # lenna = cv2.cvtColor(lenna, cv2.COLOR_BGR2RGB)
# # lenna[:,:lenna.shape[1]//2]=np.array([0,0,0])
# lenna = lenna[:, :, 2]*0.3 + lenna[:, :, 1]*0.5 + lenna[:, :, 0]*0.2
# lenna = lenna
# print(lenna_gray[:10, :10])
# cv2.imshow("lenna", lenna_gray)
# cv2.waitKey(0)
print(dict(["apple","banana","lion","computer"],["사과","바나나","사자","컴퓨터"]))
