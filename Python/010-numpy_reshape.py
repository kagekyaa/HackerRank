'''
https://www.hackerrank.com/challenges/np-shape-reshape
Input Format
A single line of input containing space separated integers.
Output Format
Print the X NumPy array.
Sample Input
1 2 3 4 5 6 7 8 9
Sample Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
import numpy as np
print np.reshape(np.array(raw_input().split(" "),int),(3,3))
