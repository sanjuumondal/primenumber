def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_smallest_prime(arr):
    q = min(arr)
    for p in range(q, 10**10):
        if all(p % num == q for num in arr if num != q) and is_prime(p):
            return p

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the distinct natural numbers separated by spaces: ").split()))

result = find_smallest_prime(arr)
print(f"The smallest prime number that satisfies the conditions is {result}")
