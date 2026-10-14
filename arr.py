# ============================================================
# LEETCODE: 60 ARRAY & MATRIX PROBLEMS
# Python solutions + one-line explanation
# ============================================================

# ======================== EASY ==============================

# 1. Two Sum
# Use a dictionary to find the complement in O(n) time.
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i


# 2. Contains Duplicate
# A set removes duplicates, so compare the lengths.
def containsDuplicate(nums):
    return len(nums) != len(set(nums))


# 3. Best Time to Buy and Sell Stock
# Track the minimum price and maximum possible profit.
def maxProfit(prices):
    minimum = float("inf")
    profit = 0
    for price in prices:
        minimum = min(minimum, price)
        profit = max(profit, price - minimum)
    return profit


# 4. Binary Search
# Repeatedly discard half of the sorted search range.
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 5. Move Zeroes
# Move nonzero values forward and fill remaining positions with zero.
def moveZeroes(nums):
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    while pos < len(nums):
        nums[pos] = 0
        pos += 1


# 6. Remove Duplicates from Sorted Array
# Keep only distinct values at the beginning of the array.
def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k


# 7. Merge Sorted Array
# Merge backwards so existing values in nums1 are not overwritten.
def mergeSortedArray(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


# 8. Single Number
# XOR cancels matching pairs and leaves the unpaired number.
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# 9. Missing Number
# Subtract the array sum from the expected sum of 0 through n.
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


# 10. Majority Element
# Boyer-Moore voting finds the element appearing more than n/2 times.
def majorityElement(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


# 11. Plus One
# Add one from the last digit and propagate any carry.
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


# 12. Pascal's Triangle
# Each inner element is the sum of two elements in the previous row.
def pascalTriangle(numRows):
    result = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


# 13. Squares of a Sorted Array
# Compare absolute values from both ends and fill the result backwards.
def sortedSquares(nums):
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for k in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[k] = nums[left] ** 2
            left += 1
        else:
            result[k] = nums[right] ** 2
            right -= 1
    return result


# 14. Intersection of Two Arrays
# Set intersection returns distinct elements present in both arrays.
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


# 15. Third Maximum Number
# Sort distinct values descending and return the third or the maximum.
def thirdMax(nums):
    values = sorted(set(nums), reverse=True)
    return values[2] if len(values) >= 3 else values[0]


# 16. Maximum Average Subarray I
# Maintain a fixed-size sliding window and track its largest sum.
def findMaxAverage(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k


# 17. Find All Numbers Disappeared in an Array
# Check which values from 1 through n are absent from the set.
def findDisappearedNumbers(nums):
    present = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in present]


# 18. Rotate Array
# Slice the array at n-k to rotate its elements to the right.
def rotateArray(nums, k):
    if not nums:
        return
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k] if k else nums


# 19. Check if Array Is Sorted and Rotated
# A valid sorted rotation has at most one descending adjacent pair.
def checkSortedRotated(nums):
    n = len(nums)
    drops = sum(nums[i] > nums[(i + 1) % n] for i in range(n))
    return drops <= 1


# 20. Find Pivot Index
# Compare the left sum with the remaining right sum at each index.
def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i, num in enumerate(nums):
        if left == total - left - num:
            return i
        left += num
    return -1


# 21. Running Sum of 1D Array
# Add each previous cumulative sum to the current element.
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


# 22. Remove Element
# Overwrite the array with values that are not equal to val.
def removeElement(nums, val):
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k


# 23. Search Insert Position
# Binary search finds the first index whose value is at least target.
def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


# 24. Valid Mountain Array
# Require a nonempty uphill section followed by a downhill section.
def validMountainArray(arr):
    n = len(arr)
    i = 0
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    return i == n - 1


# 25. Height Checker
# Compare the original heights with their sorted order.
def heightChecker(heights):
    expected = sorted(heights)
    return sum(a != b for a, b in zip(heights, expected))


# 26. Max Consecutive Ones
# Count consecutive ones and reset the count whenever zero appears.
def findMaxConsecutiveOnes(nums):
    current = best = 0
    for num in nums:
        if num == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


# 27. Degree of an Array
# Find the shortest span covering all occurrences of a most-frequent value.
def findShortestSubArray(nums):
    count, first, last = {}, {}, {}
    for i, num in enumerate(nums):
        count[num] = count.get(num, 0) + 1
        first.setdefault(num, i)
        last[num] = i
    degree = max(count.values())
    return min(last[x] - first[x] + 1
               for x in count if count[x] == degree)


# 28. Fair Candy Swap
# Use the difference between sums to find an equalizing exchange.
def fairCandySwap(aliceSizes, bobSizes):
    difference = (sum(aliceSizes) - sum(bobSizes)) // 2
    bob = set(bobSizes)
    for a in aliceSizes:
        b = a - difference
        if b in bob:
            return [a, b]


# 29. Monotonic Array
# Check whether all adjacent pairs are nondecreasing or nonincreasing.
def isMonotonic(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
            or all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


# 30. Richest Customer Wealth
# Sum each customer's account balances and return the largest total.
def maximumWealth(accounts):
    return max(map(sum, accounts))


# ======================= MEDIUM =============================

# 31. Maximum Subarray
# Kadane's algorithm chooses whether to extend or restart the subarray.
def maxSubArray(nums):
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


# 32. Product of Array Except Self
# Multiply prefix and suffix products without using division.
def productExceptSelf(nums):
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


# 33. Container With Most Water
# Move the shorter boundary inward to search for a larger area.
def maxArea(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


# 34. Merge Intervals
# Sort intervals and merge each interval that overlaps the previous one.
def mergeIntervals(intervals):
    intervals.sort()
    result = []
    for start, end in intervals:
        if not result or start > result[-1][1]:
            result.append([start, end])
        else:
            result[-1][1] = max(result[-1][1], end)
    return result


# 35. 3Sum
# Fix one number and use two pointers to find pairs summing to its negative.
def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


# 36. Next Permutation
# Find the pivot, swap it with its successor, and reverse the suffix.
def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])


# 37. Search in Rotated Sorted Array
# Binary search identifies the sorted half and discards the other half.
def searchRotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# 38. Find First and Last Position of Element
# Two binary searches find the leftmost and rightmost target positions.
def searchRange(nums, target):
    def bound(first):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target or (first and nums[mid] == target):
                right = mid
            else:
                left = mid + 1
        return left

    start = bound(True)
    if start == len(nums) or nums[start] != target:
        return [-1, -1]
    return [start, bound(False) - 1]


# 39. Sort Colors
# Dutch National Flag partitions zeroes, ones, and twos in one pass.
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# 40. Jump Game
# Track the farthest reachable index and fail if an index is unreachable.
def canJump(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True


# 41. Jump Game II
# Greedily expand the current reachable range to minimize jumps.
def jumpGameII(nums):
    jumps = current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


# 42. Rotate Image
# Transpose the square matrix and reverse each row.
def rotateImage(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


# 43. Spiral Matrix
# Traverse the outer boundaries inward while collecting matrix elements.
def spiralOrder(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result


# 44. Set Matrix Zeroes
# Use the first row and column as markers to achieve O(1) extra space.
def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row = any(matrix[0][j] == 0 for j in range(cols))
    first_col = any(matrix[i][0] == 0 for i in range(rows))

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row:
        matrix[0] = [0] * cols
    if first_col:
        for i in range(rows):
            matrix[i][0] = 0


# 45. Subarray Product Less Than K
# A sliding window counts all valid subarrays ending at each right index.
def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    product, left, count = 1, 0, 0
    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count


# 46. Insert Interval
# Add earlier intervals, merge overlaps, and append the remaining intervals.
def insertInterval(intervals, newInterval):
    result = []
    i = 0
    start, end = newInterval

    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    result.append([start, end])
    result.extend(intervals[i:])
    return result


# 47. Find Minimum in Rotated Sorted Array
# Binary search narrows the range containing the minimum element.
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# 48. Maximum Product Subarray
# Track both maximum and minimum products because negative values can flip signs.
def maxProduct(nums):
    maximum = minimum = answer = nums[0]
    for num in nums[1:]:
        if num < 0:
            maximum, minimum = minimum, maximum
        maximum = max(num, maximum * num)
        minimum = min(num, minimum * num)
        answer = max(answer, maximum)
    return answer


# 49. Find the Duplicate Number
# Floyd's cycle detection finds the duplicate without modifying the array.
def findDuplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


# 50. Search a 2D Matrix
# Treat the sorted matrix as a flattened sorted array for binary search.
def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        if value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# ======================== HARD ==============================

# 51. Trapping Rain Water
# Two pointers accumulate water using the maximum height seen on each side.
def trapRainWater(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


# 52. Median of Two Sorted Arrays
# Binary search partitions the smaller array to find the combined median.
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        al = float("-inf") if i == 0 else nums1[i - 1]
        ar = float("inf") if i == m else nums1[i]
        bl = float("-inf") if j == 0 else nums2[j - 1]
        br = float("inf") if j == n else nums2[j]

        if al <= br and bl <= ar:
            if (m + n) % 2:
                return max(al, bl)
            return (max(al, bl) + min(ar, br)) / 2

        if al > br:
            right = i - 1
        else:
            left = i + 1


# 53. First Missing Positive
# Place each positive value x at index x-1 and find the first mismatch.
def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n:
            correct = nums[i] - 1
            if nums[correct] == nums[i]:
                break
            nums[i], nums[correct] = nums[correct], nums[i]

    for i, num in enumerate(nums):
        if num != i + 1:
            return i + 1
    return n + 1


# 54. Sliding Window Maximum
# A decreasing deque maintains candidate indices for each window maximum.
from collections import deque

def maxSlidingWindow(nums, k):
    dq, result = deque(), []
    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


# 55. Candy
# Two passes ensure every child with a higher rating gets more candy.
def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


# 56. Count of Smaller Numbers After Self
# Merge sort counts right-half elements moved before each left-half element.
def countSmaller(nums):
    n = len(nums)
    result = [0] * n
    indexes = list(range(n))

    def sort(left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)

        merged = []
        i, j = left, mid
        smaller = 0

        while i < mid and j < right:
            if nums[indexes[j]] < nums[indexes[i]]:
                merged.append(indexes[j])
                smaller += 1
                j += 1
            else:
                result[indexes[i]] += smaller
                merged.append(indexes[i])
                i += 1

        while i < mid:
            result[indexes[i]] += smaller
            merged.append(indexes[i])
            i += 1

        while j < right:
            merged.append(indexes[j])
            j += 1

        indexes[left:right] = merged

    sort(0, n)
    return result


# 57. Split Array Largest Sum
# Binary search the minimum possible largest subarray sum.
def splitArray(nums, k):
    left, right = max(nums), sum(nums)

    while left < right:
        mid = (left + right) // 2
        groups, current = 1, 0

        for num in nums:
            if current + num > mid:
                groups += 1
                current = num
            else:
                current += num

        if groups <= k:
            right = mid
        else:
            left = mid + 1

    return left


# 58. Maximum Gap
# Bucket minimums and maximums reveal the largest gap between buckets.
def maximumGap(nums):
    n = len(nums)
    if n < 2:
        return 0

    minimum, maximum = min(nums), max(nums)
    if minimum == maximum:
        return 0

    size = max(1, (maximum - minimum + n - 2) // (n - 1))
    count = (maximum - minimum) // size + 1
    bucket_min = [float("inf")] * count
    bucket_max = [float("-inf")] * count

    for num in nums:
        i = (num - minimum) // size
        bucket_min[i] = min(bucket_min[i], num)
        bucket_max[i] = max(bucket_max[i], num)

    answer, previous = 0, minimum
    for bmin, bmax in zip(bucket_min, bucket_max):
        if bmin == float("inf"):
            continue
        answer = max(answer, bmin - previous)
        previous = bmax

    return answer


# 59. Minimum Number of Refueling Stops
# Use a max heap to refuel from the largest previously passed station.
import heapq

def minRefuelStops(target, startFuel, stations):
    fuel, position, stops = startFuel, 0, 0
    heap = []

    for location, capacity in stations + [[target, 0]]:
        fuel -= location - position

        while fuel < 0 and heap:
            fuel += -heapq.heappop(heap)
            stops += 1

        if fuel < 0:
            return -1

        heapq.heappush(heap, -capacity)
        position = location

    return stops


# 60. Find Median from Data Stream
# Two heaps keep the lower and upper halves balanced for fast median lookup.
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap, stored as negative values
        self.large = []  # Min heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        if self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2