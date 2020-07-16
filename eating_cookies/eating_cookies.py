import itertools

'''
Input: an integer
Returns: an integer
'''

"""
U - Cookie Monster can eat up to 3 cookies at a time. 

"""

my_list = [1, 2, 3, 4, 5]
my_second_list = my_list[:]
my_list.append(6)
print('my_list: ', my_list)
print('second list: ', my_second_list)


# combine = itertools.combinations(range(51), 3)
# combine2 = itertools.combinations(range(51), 2)
# combine3 = itertools.combinations(range(51), 1)

total = 124950 * 2550 * 51
print(total)

permute = itertools.permutations(range(51), 3)
permute2 = itertools.permutations(range(51), 2)
permute3 = itertools.permutations(range(51), 1)

full_list = [permute, permute2, permute3]

full_permute = itertools.permutations(full_list, 3)
counter = 0

for c in full_permute:
    counter += 1
    print(counter)

# for p in permute3:
#     counter += 1
#     print(counter)


def eating_cookies(n):
    # Your code here

    pass


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
