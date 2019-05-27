'''
@author:Lee
@file:test11.py
@Time: 2019/4/4 20:59
'''

import collections
# class Solution(object):
#     def sumEvenAfterQueries(self, A, queries):
#         """
#         :type A: List[int]
#         :type queries: List[List[int]]
#         :rtype: List[int]
#         """
        # method1
        # l1 = []
        # l2 = []
        # for ch in queries:
        #     A[ch[1]] = A[ch[1]]+ch[0]
        #     for i in A:
        #         if i%2==0:
        #             l2.append(i)
        #     l1.append(sum(l2))
        #     l2 = []
        # return l1


#         # method2
#         cur = sum(a for a in A if a%2==0)
#         for ch in queries:
#             if (A[ch[1]] +ch[0])%2==0:
#                 A[ch[1]] = A[ch[1]] +ch[0]
#                 cur+=(A[ch[1]] +ch[0])
#             else:
#                 A[ch[1]] = A[ch[1]] + ch[0]
#                 cur-=A[ch[1]]
# s = Solution()
# print(s.sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))

#num 2
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        s = collections.Counter(deck)
        print(s.values())
        for key in s.keys():
            if s[key]%2!=0:
                return False
        return True
s =Solution()
print(s.hasGroupsSizeX([1,2,1,2]))

