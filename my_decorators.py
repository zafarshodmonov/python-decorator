
def cache(func):
    memo = {}

    def wrapper(*args, **kwargs):
        # Create a unique key based on the function name and arguments
        key = (func.__name__, args, frozenset(kwargs.items()))

        # Check if the result is already in the cache
        if key in memo:
            # print("Cache hit!")
            return memo[key]

        # If not in the cache, compute the result and store it
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper

@cache
def F(x):
    return x ** 2

print(F(5))
print(F(6))
print(F(5))
