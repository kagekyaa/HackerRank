'''https://www.hackerrank.com/challenges/python-loops
Read an integer N. For all non-negative integers i<N, print i^2. See the sample for details.
Sample Input
5
Sample Output
0
1
4
9
16
'''

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0, n):
        print i * i

'''
A for loop:

for i in range(0, 5):
    print i

And a while loop:

i = 0
while i < 5:
    print i
    i += 1

Here, the term range(0,5) returns a list of integers from 1 to 5: [0,1,2,3,4].
'''
