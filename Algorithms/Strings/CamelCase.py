import sys

if __name__ == '__main__':

    s = input().strip()
    n=1
    for l in s:
        if l.isupper():
            n+=1
    print(n)
