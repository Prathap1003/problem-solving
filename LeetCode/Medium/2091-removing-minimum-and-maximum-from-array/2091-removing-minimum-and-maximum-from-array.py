class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        count=0
        count1=0
        nums1=nums.copy()
        if len(nums)<=2:
            return len(nums)
        print(max(nums),min(nums))
        min_index=nums.index(min(nums))
        if len(nums[:min_index+1])<len(nums[min_index:]):
            count+=len(nums[:min_index+1])
            del nums[:min_index+1]
        else:
            count+=len(nums[min_index:])
            del nums[min_index:]
        max_index=nums.index(max(nums))
        if len(nums[:max_index+1])<len(nums[max_index:]):
            count+=len(nums[:max_index+1])
            del nums[:max_index+1]
        else:
            count+=len(nums[max_index:])
            del nums[max_index:]
        max_index=nums1.index(max(nums1))
        if len(nums1[:max_index+1])<len(nums1[max_index:]):
            count1+=len(nums1[:max_index+1])
            del nums1[:max_index+1]
        else:
            count1+=len(nums1[max_index:])
            del nums1[max_index:]
        min_index=nums1.index(min(nums1))
        if len(nums1[:min_index+1])<len(nums1[min_index:]):
            count1+=len(nums1[:min_index+1])
            del nums1[:min_index+1]
        else:
            count1+=len(nums1[min_index:])
            del nums1[min_index:]
        #max_index=nums.index(max(nums))
        #print(max_index,min_index,len(nums))
        #n=len(nums)
        #count+=min(n-(min_index),min_index+1)
        #print(count)
        #count+=min(n-(max_index),max_index+1)
        return min(count1,count)

        