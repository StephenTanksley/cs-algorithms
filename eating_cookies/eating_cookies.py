from itertools import permutations

'''
Input: an integer
Returns: an integer
'''

"""
U - Cookie Monster can eat up to 3 cookies at a time. We need to determine 
    how many permutations are possible for (n) cookies if he eats:
    
        1) 1 cookie, then 1 cookie, then 1 cookie.
        2) 2 cookies, then 1 cookie
        3) 1 cookie, then 2 cookies
        4) 3 cookies all at once.
        
    Therefore, the function `eating_cookies(3)` should return 4, which is
    the sum of all the different ways he could eat all the cookies in the jar.
    
P - The function is essentially recursive. We want to narrow down the field of 
    possible choices by calling the function and dividing it into simpler sub-problems.
    To accomplish this, we can set up a base case based on some of the inputs in the 
    test files.

"""


def eating_cookies(n, cache=None):

    if cache is None:
        cache = {}

    cache[0] = 1
    cache[1] = 1
    cache[2] = 2

    # base cases for recursion
    if n < 0:
        return 0
    if n == 0:
        return 1

    # Let's see if the answer is already stored in the cache.
    if n in cache:
        return cache[n]

    number_of_ways = eating_cookies(
        n-1, cache=cache) + eating_cookies(n-2, cache=cache) + eating_cookies(n-3, cache=cache)

    cache[n] = number_of_ways

    return number_of_ways


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
