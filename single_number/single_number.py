
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

"""
U - Input will be in the form of an array that contains integers. 
    Most of those integers will be present in the array twice. 
    One of those numbers will only appear once. 
    For the solution to this problem, we want to retrieve the number that only appears once.

P - 1) Cycle through the array to count items.
    2) Check to see what items have counts == 1
    3) Return that item.

E - Will require the count function, and a for loop.

R - Look for an opportunity to fix this using dicts. 
    Using a Counter dict, we may be able to just populate a dict 
    and then use a simple conditional to return our answer 
    instead of requiring a for loop.
"""


def single_number(arr):
    original = None

    for item in arr:
        clone = arr.count(item)
        if clone == 1:
            original = item
    return original


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
