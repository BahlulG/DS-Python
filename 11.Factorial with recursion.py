# When should we use recursion?
# 1. When the problem has a tree-like structure
# 2. When the problem needs backtracking


def factorial(num):
    if num == 1:  # This is base case of Recursion, because it doesn't call itself here
        return 1
    else:
        return num * factorial(num - 1)  # Calling the 'factorial' itself until 'num' equals to 1


print(factorial(5))
