'''
https://www.hackerrank.com/challenges/np-array-mathematics
Input Format
The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.
Output Format
Print the result of each operation in the given order under Task.
Sample Input
1 4
1 2 3 4
5 6 7 8
Sample Output
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
'''
import numpy as np
n, m = map(int, raw_input().split())
A = np.array([raw_input().split() for _ in range(n)], int)
B = np.array([raw_input().split() for _ in range(n)], int)
print A+B
print A-B
print A*B
print A//B
print A%B
print A**B