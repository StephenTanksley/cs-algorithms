from functools import reduce

'''
Input: a List of integers
Returns: a List of integers
'''

"""
U - We're given a list of integers.  We're required to 
    return the product of each number by every OTHER number 
    in the list. We're required to do this in O(n) time
    AND O(n) space without using division. 
    
    To do this with division, you could just get the product 
    of the entire array and divide it by the index that should 
    be skipped. For our solution, we're going to remove that 
    value entirely.
    
P - Naive solution: 
    
    1) create a temporary array and a solutions array
    2) create a loop and copy the array into the temporary array
        3) for an item at i, remove it from the temporary array
        4) using a lambda function, get the product of the entire array minus the item
        5) push that value into the solutions array
    6) return solutions array
    
P - Optimized(?) solution
    
    1) Pretty much do the same thing as on the Naive solution.
    2) Cache the results of the first function call and the popped value 
       using enumerate.
    3) Compare the popped value to value at the loop index.
        4) if the cache has the results of a number that's the same at i, 
           push the results of that prior function call into solutions array 
           and keep the popped value the same.
        5) if they're different, perform caching of the new value and add 
           to solutions array.
        6) return the solutions array at the end of the function.

E - Need to provide a cache as an argument to the function as well as the
    requirements for the normal algorithm's requirements.

"""


def product_of_all_other_numbers(arr, cache):

    # We create a solutions array to store our final solutions.
    solutions = []
    temp = []

    # We create a temporary copy of the original array. We only want to do operations on this temporary copy.
    # We want to create the temporary copy of the array inside the loop because we don't want the copy of the array to persist beyond one cycle.
    for i, num in enumerate(arr):

        if i in cache:
            solutions.append(cache[i])
            return

        temp = arr[:]
        # we pop off the value at the index of i
        popped = temp.pop(i)

        # we reduce the temporary array down to a single product
        product = reduce((lambda x, y: x * y), temp)
        cache[i] = product

        # we add that product to our solutions accumulator array and repeat the loop
        solutions.append(product)

    return solutions


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr, {})}")
