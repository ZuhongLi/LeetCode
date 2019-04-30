'''
@author:Lee
@file:test04.py
@Time: 2019/3/28 19:38
'''

# num1
# class Solution(object):
#     def toLowerCase(self, str):
#         """
#         :type str: str
#         :rtype: str
#         """
#         return str.lower()
# s = Solution()
# print(s.toLowerCase('hssada'))

#num2
# class Solution(object):
#     def numUniqueEmails(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: int
#         """
#         list = set()
#         for i in range(len(emails)):
#             domain = emails[i].split('@')[-1]
#             local = emails[i].split('@')[0].split('+')[0].replace('.','')
#             email = local+domain
#             list.add(email)
#         return len(list)
# s = Solution()
# print(s.numUniqueEmails(['abcd@com','ab.cd@com','abcdwe@com']))

#num3
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         dict = {'}':'{',']':'[',')':'('}
#         stack = []
#         for i in s:
#             if i in dict.values():
#                 stack.append(i)
#             elif stack==[] or dict[i]!=stack.pop():
#                 return False
#         return stack==[]
# s = Solution()
# print(s.isValid('{'))

#num4
# class Solution(object):
#     def removeDuplicates(self,nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         s = set(nums)
#         return len(s)
#         # if not A:
#         #     return 0
#         #
#         # newTail = 0
#         #
#         # for i in range(1, len(A)):
#         #     if A[i] != A[newTail]:
#         #         newTail += 1
#         #         A[newTail] = A[i]
#         #
#         # return newTail + 1
# s = Solution()
# print(s.removeDuplicates([2,2,2,3,3,1,1]))

#num5
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         dummy = cur = ListNode(0)

#num6
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # count = nums.count(val)
        # for i in range(count):
        #     nums.remove(val)
        # return len(nums)

        #method 2
        # i = 0
        # for x in nums:
        #     if x != val:
        #         nums[i] = x
        #         i += 1
        # return i
# s = Solution()
# print(s.removeElement([1,1,2,2,4,5],2))

#num7
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s
s =Solution()
print(s.countAndSay(5))
