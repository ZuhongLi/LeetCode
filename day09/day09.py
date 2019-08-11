'''
@author:Lee
@file:test13.py
@Time: 2019/4/9 20:06
@Description:
'''

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


# num821
# class Solution(object):
#     def shortestToChar(self, S, C):
#         """
#         :type S: str
#         :type C: str
#         :rtype: List[int]
#         """
#         res = []
#         index = [i for (i,v) in enumerate(S) if v==C]
#         for i in range(len(S)):
#             res.append(min([abs((t-i)) for t in index]))
#         return res
# s =Solution()
# print(s.shortestToChar("loveleetcode",'e'))

#num 701
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from collections import deque
# class Solution(object):
#     def insertIntoBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
        # queue = deque()
        # queue.append(root)
        # res = root
        # while queue:
        #     root = queue.popleft()
        #     if root.val > val and root.left is None:
        #         root.left = TreeNode(val)
        #         return res
        #     if root.val < val and root.right is None:
        #         root.right=TreeNode(val)
        #         return res
        #     if root.val > val:
        #         queue.append(root.left)
        #     if root.val<val:
        #         queue.append(root.right)
        # return res
#num 950
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
#         deck = sorted(deck, reverse = True)
#         stack = []
#         stack.append(deck[0])
#         deck = deck[1:]
#         for i in deck:
#             stack = stack[-1:]+stack[:-1]
#             stack = [i] + stack
#         return stack
#         deck  =  sorted(deck,reverse=True)
#         l = []
#         l.append(deck[0])
#         deck = deck[1:]
#         for i in deck:
#             l.insert(0,i)
#             temp = l[-1]
#             l = l[:-1]
#             l.insert(0,temp)
#         temp = l[0]
#         l = l[1:]
#         l.append(temp)
#         return l
# s = Solution()
# print(s.deckRevealedIncreasing([7,13,1,2,3,5,27]))

#num 476
# class Solution(object):
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         s = bin(num).split('0b')[-1]
#         res = ''
#         for i in s:
#             if i =='1':
#                 res+='0'
#             elif i=='0':
#                 res+='1'
#         return int(res,2)
#
# s =Solution()
# print(s.findComplement(1))
