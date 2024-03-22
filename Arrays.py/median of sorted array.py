def findMedianSortedArrays(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    # Let's perform the binary search on the smaller array. Ensure that nums1 is smaller.
    if m > n:
        return findMedianSortedArrays(nums2, nums1)
    total_length = m + n
    half_length = (total_length + 1) // 2
    left, right = 0, m
    while left <= right:
        p_a = (left + right) // 2
        p_b = half_length - p_a
        max_left_a = float('-inf') if p_a == 0 else nums1[p_a - 1]
        max_left_b = float('-inf') if p_b == 0 else nums2[p_b - 1]
        min_right_a = float('inf') if p_a == m else nums1[p_a] 
        min_right_b = float('inf') if p_b == n else nums2[p_b]            
        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if total_length % 2 == 0:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
            else:
                return max(max_left_a, max_left_b)
        elif max_left_a > min_right_b:
            right = p_a - 1
        else:
            left = p_a + 1
    # Code should never reach here
    return -1
ans=findMedianSortedArrays([1,3,5],[2,4,6])
print(ans)
