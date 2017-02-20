'''https://www.hackerrank.com/challenges/python-arithmetic-operators
Task
Read two integers from STDIN and print three lines where:
    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.
Sample Input
3
2
Sample Output
5
1
6
'''

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a + b
    print abs(a - b)
    print a * b

