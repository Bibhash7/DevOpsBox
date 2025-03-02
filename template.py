import sys
import os
import math
import collections
import itertools
import heapq
import bisect
from functools import lru_cache
from typing import List, Tuple
from collections import defaultdict

# Fast Input Functions
def get_int():
    line = sys.stdin.readline().strip()
    return int(line) if line else 0 

def get_list():
    line = sys.stdin.readline().strip()
    return list(map(int, line.split())) if line else []  # Handle empty input safely

def get_string():
    return sys.stdin.readline().strip()

# Output Optimization
sys.setrecursionlimit(10**6)
def print_flush(*args):
    sys.stdout.write(' '.join(map(str, args)) + '\n')
    sys.stdout.flush()

# Utilities
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve(n: int) -> List[int]:
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

# Binary Search
def binary_search(arr: List[int], x: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

# Graph Utilities
def bfs(graph: dict, start: int) -> List[int]:
    queue, visited = collections.deque([start]), set()
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order

def dfs(graph: dict, start: int, visited: set = None) -> List[int]:
    if visited is None:
        visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            stack.extend(reversed(graph[node]))  # Reverse to maintain order
    return order

# Toggle Test Cases
hastestcase = False

def solve():
    pass
    

    
            
    
    
    
    
    
    

def main():
    if os.path.exists("input.txt"):
        with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
            
            sys.stdin, sys.stdout = fin, fout
            if hastestcase:
                t = get_int()
                for _ in range(t):
                    solve()
            else:
                solve()
    else:
        if hastestcase:
            t = get_int()
            for _ in range(t):
                solve()
        else:
            solve()
            

if __name__ == "__main__":
    main()
