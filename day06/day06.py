'''
@author:Lee
@file:test09.py
@Time: 2019/4/2 20:13
'''
# num1
# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         count = 0
#         m = bin(x).split('b')[1]
#         n = bin(y).split('b')[1]
#         l = abs(len(m)-len(n))
#         if x < y:
#             for i in range(l):
#                 m = '0'+m
#         else :
#             for i in range(l):
#                 n = '0'+n
#         for j in range(len(m)):
#             if m[j]!=n[j]:
#                 count = count+1
#         return count
# s = Solution()
# print(s.hammingDistance(1,8))

#num 2
# class Solution(object):
#     def selfDividingNumbers(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: List[int]
#         """
#         Is = True
#         res = []
#         for i in range(left,right+1):
#             s = str(i)
#             if '0' in s:
#                 continue
#             for el in s:
#                 if i%int(el)!=0:
#                     Is =False
#             if Is == True:
#                 res.append(i)
#             Is = True
#         return res
# s = Solution()
# print(s.selfDividingNumbers(47,85))


#num 3
# class Solution(object):
#     def peakIndexInMountainArray(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         return A.index(max(A))
# s =Solution()
# print(s.peakIndexInMountainArray([0,2,1,0]))

#num 4
# class Solution(object):
#     def arrayPairSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sum = 0
#         l = sorted(nums)
#         for i in range(len(nums)):
#             if i % 2==0:
#                 sum = sum + l[i]
#         return sum
#
#     #method 2
#         return sum(sorted(nums)[::2])
# s =Solution()
# print(s.arrayPairSum([1,2,3,4]))
