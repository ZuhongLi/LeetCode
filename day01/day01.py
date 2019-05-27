'''
@author:Lee
@file:test01.py
@Time: 2019/3/25 19:53
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         res = [];
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == target - nums[j]:
#                     res.append(i);
#                     res.append(j);
#         return res;
# s = Solution().twoSum([2,3,5],7)
# print(s)
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                print(buff_dict)
s = Solution().twoSum([2,3,5,7,9,11,13,15,17],19)
print(s)

#         if len(nums)<= 1:
#             return None
#         buff_dict = {};
#         for i in range(len(nums)):
#             if nums[i] in buff_dict:
#                 return [buff_dict[nums[i]],i]
#             else:
#                 buff_dict[target-nums[i]] = i;
# s= Solution().twoSum([2,3,5,7,9,11,13,15,17],20)
# print(s)


#num 334
# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         # return s[::-1]
#         left ,right = 0,len(s)-1
#         while left<right:
#             s[left],s[right] = s[right],s[left]
#             left+=1
#             right-=1
#         return s
# s = Solution()
# print(s.reverseString(["H","a","n","n","a","h"]))
