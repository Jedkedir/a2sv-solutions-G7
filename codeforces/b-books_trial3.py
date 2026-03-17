import sys


def solution():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    n, t = int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]

    left = 0
    current_sum = 0
    max_books = 0

    for right in range(n):
        current_sum += a[right]
        while current_sum > t:
            current_sum -= a[left]
            left += 1
        max_books = max(max_books, right - left + 1)

    print(max_books)


if __name__ == "__main__":
    solution()