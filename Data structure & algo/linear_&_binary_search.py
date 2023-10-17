""" Big 'O' Notation """

nums_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
target = 17


def linearSearch(nums_list, target):
    """ linear search works on Order of n 0(n) """
    take_steps = 0
    for i in range(len(nums_list)-1):
        take_steps += 1
        if nums_list[i] == target:
            print(f"Found at index by using linearSearch : {i}")
            print(f"Steps taken to found element : {take_steps}")
            return i
    return -1


def binarySearch(nums_list, target):
    """ binary search works on Order of n 0(log n) """
    take_left = 0
    take_right = len(nums_list) - 1
    take_steps = 0
    while (take_left <= take_right):
        take_steps += 1
        take_mid = (take_left + take_right)//2
        if nums_list[take_mid] == target:
            print(f"Found at index by using binarySearch : {take_mid}")
            print(f"Steps taken to found element : {take_steps}")
            return take_mid
        elif nums_list[take_mid] < target:
            take_left = take_mid + 1
        else:
            take_right = take_mid - 1

    return -1


def recursionBinarySearch(nums_list, target, take_left=0, take_right=len(nums_list), take_steps=0):
    if take_left <= take_right:
        take_mid = (take_left + take_right)//2
        if nums_list[take_mid] == target:
            print(
                f"Found at index by using recursionBinarySearch : {take_mid}")
            print(f"Steps taken to found element : {take_steps}")
            return take_mid
        elif nums_list[take_mid] < target:
            return recursionBinarySearch(nums_list, target, take_left=take_mid + 1, take_right=take_right, take_steps=take_steps+1)
        else:
            return recursionBinarySearch(nums_list, target, take_left, take_right=take_mid - 1,take_steps=take_steps+1)


linearSearch(nums_list, target)
binarySearch(nums_list, target)
recursionBinarySearch(nums_list, target, 0, take_right=len(nums_list))
