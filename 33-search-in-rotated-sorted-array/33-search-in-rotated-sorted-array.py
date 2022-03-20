class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right, target):
            while left <= right:
                mid = (left+right)>>1
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def search_in_rotated(left, right, target):
            if left == right:
                return left if nums[left] == target else -1
                
            mid = (left+right)>>1
            ret = -1
            if nums[left] < nums[mid]:
                ret = binary_search(left, mid, target)
                if ret != -1: return ret
            else:
                ret = search_in_rotated(left, mid, target)
                if ret != -1: return ret
            if nums[mid+1] < nums[right]:
                ret = binary_search(mid+1, right, target)
                if ret != -1: return ret
            else:
                ret = search_in_rotated(mid+1, right, target)
                if ret != -1: return ret
            return -1
        
        left, right = 0, len(nums)-1
        return search_in_rotated(left, right, target) 