# import numpy as np
# a=np.array([1,2,3])
# # print(a)
# b=np.array([4,5,6])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# c=[1,2,3]
# d=[4,5,6]
# print(c+d)
# print(c-d)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
# my_image=img.imread("./python_yoorabbit/Day8/img.jpg")
# my_image=img.imread("./python_yoorabbit/Day8/사쿠마레이.jpg")
# plt.imshow(my_image)
# plt.show()

my_matrix=np.array([
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
    [[255,0,0],[255,0,0],[255,255,255],[255,0,0],[255,0,0]],
    [[255,0,0],[255,255,255],[255,255,255],[255,255,255],[255,0,0]],
    [[255,0,0],[255,0,0],[255,255,255],[255,0,0],[255,0,0]],
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
])
plt.imshow(my_matrix)
plt.show()