# Palindrome means, word reading from right to left or from left to right equals same value. EX: noon

a = 'anna'


def Palindrome(value):
    # If length of value equals to 0 or 1, this is anyway Palindrome
    # Base case of Recursion
    if len(value) <= 1:
        return True

    # Here is recursion happens: Palindrome(value[1:-1]).
    # Everytime check next value from left and right side of the word, and return the Bool value
    else:
        return value[0] == value[-1] and Palindrome(value[1:-1])


print(Palindrome(a))
