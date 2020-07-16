'''
Input: a List of integers
Returns: a List of integers
'''

"""
U - Input is a list of integers. The list of integers will have some 0s included in it.
    The 0s need to be pushed to the tail end of the list. The rest of the list needs to remain in order.
    
P1 (in-place swap plan) - 
    
    1) We need a way of keeping track of where we are in the array.
    2) We need to know the total length of the array.
    3) We need to determine if an object at a certain index is equal to 0.
    4) If the integer at the next looping index is NOT equal to 0, we can insert at that index.
    5) We don't actually need to touch the 0s.
    
P2 (ugly-stepchild recombinant lists plan) -
    
    1) - Count the number of zeroes in the array.
    2) - Remove all zeroes from the array.
    3) - Create a new array with the correct number of zeroes.
    4) - Squash the old array (minus zeroes) together with the new array (with the right number of zeroes)
    5) - Profit.
    
E - We'll need a counter, a list comprehension, 
    a new array for the correct number of zeroes, 
    and then to put things together.
    
R - Look for a way of cleaning these functions up. 
    Ideally, we'd want to use the in-place swap because it wouldn't require more space.

"""


def moving_zeroes(arr):
    item_count = arr.count(0)

    minus_zero = [item for item in arr if item != 0]
    add_zero = [0] * item_count

    final_array = minus_zero + add_zero
    return final_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
