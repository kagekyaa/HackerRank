'''
Sample Input
Guido
Rossum
Sample Output
Hello Guido Rossum! You just delved into python.

https://www.hackerrank.com/challenges/whats-your-name
http://stackoverflow.com/questions/517355/string-formatting-in-python
'''
def print_full_name(a, b):
    print "Hello %s %s! You just delved into python." %(a, b)

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)