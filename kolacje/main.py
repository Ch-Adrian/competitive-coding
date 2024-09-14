import numpy as np 

TEST = True

def read_line():
    return [ int(a) for a in input().split(" ")]

def read_data():
    n, r = read_line() 
    if TEST:
        print(n, r)
    t = read_line() 
    if TEST:
        print(t)
    for _ in range(n-1):
        a, b, c = read_line() 
        if TEST:
            print(a, b, c)  

    q = int(input())
    if TEST:
        print(q)

    for _ in range(q):
        a, b, c = read_line() 
        if TEST:
            print(a, b, c)

if __name__ == "__main__":
    read_data()
