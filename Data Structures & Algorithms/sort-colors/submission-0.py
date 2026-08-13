class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums) - 1)
    def quicksort(self, arr, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        pivot = arr[mid]
        l = left
        r = right - 1

        arr[mid], arr[right] = arr[right], arr[mid]

        while l <= r:
            while l <= r and arr[l] < pivot:
                l += 1
            
            while l <=r and arr[r] > pivot:
                r -= 1
            
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        arr[l], arr[right] = arr[right], arr[l]

        self.quicksort(arr, left, l - 1)
        self.quicksort(arr, l + 1, right)

        return arr