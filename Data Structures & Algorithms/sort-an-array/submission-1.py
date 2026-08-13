class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums
    def merge(self, arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        temp.extend(arr[i : mid + 1])
        temp.extend(arr[j : right + 1])

        for k in range(len(temp)):
            arr[left + k] = temp[k]
    

    def merge_sort(self, arr, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2

        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid + 1, right)

        self.merge(arr, left, mid, right)
