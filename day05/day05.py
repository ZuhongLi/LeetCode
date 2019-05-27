
num1
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        list1 = [".-","-...","-.-.","-..",".",
                "..-.","--.","....","..",".---","-.-",".-..",
                "--","-.","---",".--.","--.-",".-.","...","-",
                "..-","...-",".--","-..-","-.--","--.."]
        method 1
        list2 = [chr(x) for x in range(ord('a'),ord('z')+1)]
        morse_list = []
        for str in words:
            word = ''
            for ch in str:
                index = list2.index(ch)
                word = word+list1[index]
            morse_list.append(word)
        return len(set(morse_list))

        method 2
        res = set()
        for word in words:
            val = ''
            for ch in word:
               val= val + list1[ord(ch)-ord('a')]
            res.add(val)
        return len(res)
s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

num2
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #method 1
        # if target not in nums:
        #     if nums[0]>target:
        #         return 0
        #     if nums[-1]<target:
        #         return len(nums)
        #     for num in nums:
        #         if num>target:
        #             return nums.index(num)
        # else: return nums.index(target)
        # method 2
        print(len([x for x in nums if x <target]))
        # return len([x for x in nums if x<target])
s = Solution()
print(s.searchInsert([1,3,5,6], 5))

num3
class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res

num 4
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
s = Solution()
print(s.deleteDuplicates([1,2,3,4,5]))

'''
@author:Lee
@file:test08.py
@Time: 2019/4/1 20:18
'''
#num1
# class Solution(object):
#     def flipAndInvertImage(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         for el in A:
#             j = -1
#             for i in range(len(el)):
#                 if i <= len(el) // 2 - 1:
#                     el[i], el[j] = el[j], el[i]
#                 i = i + 1
#                 j = j - 1
#             for i  in range(len(el)):
#                 if el[i] ==0:
#                     el[i]=1
#                 else: el[i] =0
#         return A
# s = Solution()
# print(s.flipAndInvertImage([[1,0,0],[0,1,1,0,1]]))

# num2
# class Solution(object):
#     def trailingZeroes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        # 暴力搜索
        # a = 1
        # if n ==0:
        #     return 1
        # for i in range(1,n+1):
        #     a = a * i
        # s = str(a)
        # i = -1
        # count = 0
        # for j in range(len(s)):
        #     if s[i]=='0':
        #         count = count + 1
        #         i = i - 1
        #     else:
        #         return count

    #所有的0都可以看做是5*2的结果，所以n有几个5，就有几个0
        # return 0 if n ==0 else n/5 +trailingZeroes(n/5)
#         return 0 if n == 0 else n // 5 + self.trailingZeroes(n //5)
# s = Solution()
# print(s.trailingZeroes(5))

#num 3
# class Solution(object):
#     def titleToNumber(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         sum = 0
#         i = 0
#         for el in s[::-1]:
#             sum += (ord(el)-ord('A')+1)*(26**i)
#             i=i+1
#         return sum
# s = Solution()
# print(s.titleToNumber('ZY'))


#num 4
# class Solution(object):
#     def diStringMatch(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """
#         n = len(S)
#         l = sorted([i for i in range(n + 1)])
#
#         l1 = []
#         for i in S:
#             if i == 'I':
#                 l1.append(l.pop(0))
#             else:
#                 l1.append(l.pop(-1))
#         return l1 +l
# s = Solution()
# print(s.diStringMatch('IDID'))

#num 5
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums1 = nums[0:len(nums)-k]
        nums2 = nums[len(nums)-k:len(nums)]
        return nums2+nums1
s = Solution()
print(s.rotate([1,2,3,4,5,6,7],3))
