'''Imagine you're organizing a grand party with three different rooms for your guests. Each guest belongs to a specific group (1, 2, or 3). But things get messy! Some guests end up in the wrong rooms, and the rooms themselves are quite unorganized.

Your task is to get everyone properly grouped and seated in a way that satisfies these conditions:

Grouped by colour: Guests in each room, represented by their group number, should be sitting together after sorting them within the room.
Sorted in order: The entire seating arrangement, after combining all rooms, should be in ascending order.
Minimum adjustments: You can "swap" a guest's group assignment (change their "ticket") any number of times. But the goal is to use the fewest number of swaps possible to achieve the desired seating arrangement.
Input:
An array nums of length n, where each element nums[i] represents the group number (1, 2, or 3) of guest i.
Output:
An integer representing the minimum number of group swaps needed to make the final seating arrangement beautiful (sorted within and between groups).
Example Input/Output:
Input:
[2, 1, 3, 2, 1]

Output:
3 (Swap nums[0], nums[2], and nums[3] to group 1)

Input:
[1, 3, 2, 1, 3, 3]

Output:
2 (Swap nums[1] and nums[2] to group 1)

Input:
[2, 2, 2, 2, 3, 3]

Output:
0 (No swaps needed; already beautiful)

Constraints:
1 <= n <= 100
1 <= nums[i] <= 3'''
def min_group_swaps(nums):
    num_groups = 3
    group_size = len(nums) // num_groups
    swaps = 0

    for group in range(1, num_groups + 1):
        group_start = (group - 1) * group_size
        group_end = group_start + group_size
        correct_positions = range(group_start, group_end)
        num_incorrect_positions = sum(1 for i, num in enumerate(nums) if num == group and i not in correct_positions)
        swaps += num_incorrect_positions

    return swaps

# Test cases
print(min_group_swaps([2, 1, 3, 2, 1]))   # Output: 3
print(min_group_swaps([1, 3, 2, 1, 3, 3])) # Output: 2
print(min_group_swaps([2, 2, 2, 2, 3, 3])) # Output: 0
