
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

"""
U - Input will be in the form of an array that contains integers. Most of those integers will be present in the array twice. One of those numbers will only appear once. For the solution to this problem, we want to retrieve the number that only appears once.

P - 1) Cycle through the array to populate a dictionary.
    2) Check to see what items have counts == 1 in the dictionary
    3) Return that items.

E - Will require a dictionary (Counter), and a for loop.
"""


def single_number(arr):
    # My Code Here
    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
