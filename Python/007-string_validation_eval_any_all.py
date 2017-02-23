'''
https://www.hackerrank.com/challenges/string-validators

https://docs.python.org/2/library/functions.html
http://stackoverflow.com/questions/9383740/what-does-pythons-eval-do
http://stackoverflow.com/questions/19389490/how-do-pythons-any-and-all-functions-work

Input Format
A single line containing a string S.
Output Format
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
Sample Input
qA2
Sample Output
True
True
True
True
True
'''
import re

if __name__ == '__main__':
    s = raw_input()

    print(bool(re.search(r'\w', s)))
    print(bool(re.search(r'[a-zA-Z]', s)))
    print(bool(re.search(r'\d', s)))
    print(bool(re.search(r'[a-z]', s)))
    print(bool(re.search(r'[A-Z]', s)))

    '''
    func = [".isalnum()",".isalpha()",".isdigit()",".islower()",".isupper()"]
    for i in func:
        print eval("(any(char" + i + " for char in s))")

    print(any(map(lambda x: x.isalnum(), s)))
    print(any(map(lambda x: x.isalpha(), s)))
    print(any(map(lambda x: x.isdigit(), s)))
    print(any(map(lambda x: x.islower(), s)))
    print(any(map(lambda x: x.isupper(), s)))
    '''