class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 , count1 = num , 1
            elif count2 == 0:
                cand2 , count2 = num , 1
            else :
                count1 -= 1
                count2 -= 1
        result = []
        n  = len(nums)
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > n //3:
                result.append(cand)
        return result
