class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        # prefix = [1] * size
        # postfix = [1] * size

        # for i in range(1, size): 
        #     prefix[i] = prefix[i-1] * nums[i-1]
            
        # for j in range(size - 2, -1, -1): 
        #     postfix[j] = postfix[j+1] * nums[j+1]

        # res = []
        # for x in range(size): 
        #     res.append(prefix[x] * postfix[x])

        # return res

        res = [1] * size
        prefix = 1
        for i in range(size):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(size - 1, -1, -1): 
            res[j] *= postfix
            postfix *= nums[j]

        return res
        