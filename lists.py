"""
The function 'median' returns the median value of an input list. It should work with lists that have an odd/even number of elements.
For lists with an even number of elements it should return the mean of the two central elements.
"""

def median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        # if the list has an odd number of elements,
        # the median is the middle element
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        # if the list has an even number of elements,
        # the median is the average of the middle two elements
        right_of_middle = len(numbers)//2
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle])/2

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))
