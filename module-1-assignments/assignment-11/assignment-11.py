import numpy as np
a = np.ones((10,2,2))
print(a)

# fourDArray = np.array([[
#               [[1,2],[3,4]],
#               [[5,6],[7,8]],
#               [[9,10],[11,12]]
#               ],
#               [
#               [[13,14],[15,16]],
#               [[17,18],[19,20]],
#               [[21,22],[23,24]]
#               ]])
# twoDArray = fourDArray.reshape(6,4)**2
# print(twoDArray)
# value = 0

# thousandEleArray = list()
# for i in range(0,1000):
#     value+=0.001
#     formatted_string = "{:.4f}".format(value)
#     float_value = float(formatted_string)
#     thousandEleArray.append(float_value)
# thousandSquEleArray = [i**2 for i in thousandEleArray]


ones = np.ones((5,5))
zeros = np.zeros((3,3))
ones[1:4 , 1:4] = zeros
print(ones)
