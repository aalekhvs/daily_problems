class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        pivot = arr[mid]

        arr[mid], arr[right] = arr[right], arr[mid]

        l = left
        r = right - 1

        while l <= r:
            while l <= r and arr[l] < pivot:
                l += 1
            
            while l <= r and arr[r] > pivot:
                r -= 1
            
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        arr[l], arr[right] = arr[right], arr[l]

        self.quicksort(arr, left, l - 1)
        self.quicksort(arr, l + 1, right)

        return arr

    



        



