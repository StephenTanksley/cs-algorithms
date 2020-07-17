'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

"""
U - The sliding window effectively creates a sub-list from a larger array of numbers.
    The input will be an array of numbers as well as a value 'k' which describes the size of the window.
    The objective is to search within the sub array to determine the maximum value.
    
P - Naive implementation

    1) Create a loop to iterate on the list of numbers.
    2) Within the loop, create the window. This can be done by using slicing.
        ex. - window = arr[i:i+3]
        if arr[i+3] == None, return.
    3) check max for window on each iteration. 
        ex. - return max(window)
    4) The expected return is an array featuring the max of each iteration.
    
"""


def sliding_window_max(nums, k):
    output_array = []

    # NAIVE SOLUTION
    for i, item in enumerate(nums):

        opened = i
        closed = i + k

        # Creating the window - create a slice using i as the start, and i + k as the end.
        window = nums[opened:closed]
        # if the length of window is the same as the value passed in via k
        if k == len(window):
            # append the max item inside that window
            output_array.append(max(window))

    # # Artem's Solution
    # for i in range(len(nums) - k + 1):
    #     current_window = nums[i:i + k]
    #     current_max = max(current_window)
    #     output_array.append(current_max)

    # return the output_array
    return output_array


def sliding_window_max_queue(nums, k):
    # create a queue that stores 'useful numbers'
    # insert the first k elements.
    # for each element we add
    # all smaller numbers in the queue, remove them.
    # process the remaining elements in nums.
    # from k to n-1
    # the element at the front of the queue
    # is the largest number of the current window
    # so save that number into our output.


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
