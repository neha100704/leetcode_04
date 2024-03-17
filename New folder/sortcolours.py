def sortColors(nums):
    n = len(nums)
    for i in range(n):
        m = i
        for j in range(i, n):
            if nums[m] > nums[j]:
                m = j
        nums[i], nums[m] = nums[m], nums[i]

if __name__ == "__main__":
    nums = [int(num) for num in input("Enter numbers separated by commas: ").split(',')]
    sortColors(nums)
    print("Sorted colors:", nums)


