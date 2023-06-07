import sys
import requests
import json
import logging
import time

logging.captureWarnings(True)

def solution(x, y):
    # Your solution here 
    value = 1
    delta = 2
    for i in range(1, x):
        value += delta
        delta += 1
    
    delta = x
    for k in range(1, y):
        value += delta
        delta += 1

    return str(value)

def main():
    print(solution(5, 10))
    print(solution(3, 2))
    print(solution(3, 20000))
    print(solution(1000, 2))

if __name__ == "__main__":
    main()