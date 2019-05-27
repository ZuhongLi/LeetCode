'''
@author:Lee
@file:test12.py
@Time: 2019/4/8 20:23
@Description:
'''
import numpy as np
#num 1

# class Solution(object):
#     def maxIncreaseKeepingSkyline(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         row= np.max(grid,axis=1)
#         column = np.max(grid,axis=0)
#         total = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 total+=(min(row[i],column[j])-grid[i][j])
#         return total
# s= Solution()
# print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

#num 2
# class Codec:
#     def __init__(self):
#         self.urls = []
#
#
#     def encode(self, longUrl):
#         """Encodes a URL to a shortened URL.
#
#         :type longUrl: str
#         :rtype: str
#         """
#         self.urls.append(longUrl)
#         return 'http://tinyurl.com/'+str(len(self.urls)-1)
#
#     def decode(self, shortUrl):
#         """Decodes a shortened URL to its original URL.
#
#         :type shortUrl: str
#         :rtype: str
#         """
#         return self.urls[int(shortUrl.split('/')[-1])]
#
# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(url))
# s = Codec()
# print(s.encode('adawdada'))
# print(s.decode('http://tinyurl.com/0'))

#num 3
# class Solution(object):
#     def transpose(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         return np.transpose(A)
# s =Solution()
# print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))

#num 4
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(' ')
        res = []
        for ch in l:
            res.append(ch[::-1])
        s =''
        for ch in res:
            s+=ch+' '
        return s.rstrip()
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
