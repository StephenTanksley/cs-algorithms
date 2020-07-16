'''
Input: a List of integers
Returns: a List of integers
'''

"""
U - We're given a list of integers. 
    We're required to return the product
    of each number by every OTHER number 
    in the list. We're required to do this on O(n) time
    AND O(n) space without using division.
    
P - Naive solution: 
    
    1) create a temporary array and a solutions array
    2) create a loop
        2a) Copy the array into the temporary array
        3) for an item at i, remove it from the temporary array
        4) using a lambda function, get the product of the entire array minus the item
        5) push that value into the solutions array
    6) return solutions array

"""


def product_of_all_other_numbers(arr):

    solutions = []
    temp = arr[:]
    for i in temp:
        popped = temp.pop(i)
        print('popped', popped)


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
