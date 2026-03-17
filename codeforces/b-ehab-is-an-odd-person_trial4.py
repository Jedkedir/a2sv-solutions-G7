import sys
def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    has_odd = any(num % 2 != 0 for num in arr)
    has_even = any(num % 2 == 0 for num in arr)
    if has_odd and has_even:
        arr.sort()
    print(*arr)
if __name__ == "__main__":
    solution()