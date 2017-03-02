'''https://www.hackerrank.com/challenges/np-mean-var-and-std
Input Format
The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.
Output Format
First, print the mean.
Second, print the var.
Third, print the std.
Sample Input
2 2
1 2
3 4
Sample Output
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
'''
import numpy
n, _ = map(int, raw_input().split())
a = numpy.array([raw_input().split() for _ in range(n)], int)
print numpy.mean(a, axis = 1)
print numpy.var(a, axis = 0)
print numpy.std(a)