'''
https://www.hackerrank.com/challenges/np-zeros-and-ones
Sample Input 0
3 3 3
Sample Output 0
[[[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
'''

import numpy as np
import string
'''
line = raw_input().split()
row = int(line[0])
row2 = int(line[1])
col = int(line[2])
print np.zeros((row,row2,col),int)
print np.ones((row,row2,col),int)
'''
x = eval(raw_input().replace(" ",","))

print np.zeros((x), dtype = np.int)
print np.ones((x), dtype = np.int)