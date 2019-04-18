'''
@author:Lee
@file:test2.py
@Time: 2019/3/26 20:59
'''
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
        # method1
#         num = 0
#         if x ==0:
#             num=0
#         if x > 0:
#             s = str(x)
#             num = int(s[::-1])
#         if x < 0:
#             x = -x
#             s = str(x)
#             num = -int(s[::-1])
#         if num > pow(2,31) or num < pow(-2,31):
#             return 0
#         return num
# s = Solution()
# print(s.reverse(-123))
        #method2
        # num = 0
        # if x == 0:
        #     num = 0
        # if x < 0:
        #     x = -x
        #     while x > 0:
        #         num = num*10 + x%10
        #         x = x/10
        # if x > 0:
        #     while x>0:
        #         num = num*10+ x%10
        #         x = x/10
        # if num > pow(2,31) or num < pow(-2,31):
        #     return 0
        # return num

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#          """
        #method 1
#         s = str(x)
#         if s == s[::-1]:
#             return True
#         else:
#             return  False
# s = Solution()
# print(s.isPalindrome(-121))

class Solution(object):
    #Amazing method
#     def romanToInt(self, s):
#         d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#         """
#         :type s: str
#         :rtype: int
#       """
#         res, p = 0, 'I'
#         for c in s[::-1]:
#             res, p = res - d[c] if d[c] < d[p] else res + d[c], c
#             print(res)
#         return res
# s = Solution()
# print(s.romanToInt('IV'))


    def romanToInt(self, s):
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        """
        :type s: str
        :rtype: int
      """
        sum = 0
        for i in range(0,len(s)-1):
            if d[s[i]]<d[s[i+1]]:
                sum = sum-d[s[i]]
            else:
                sum = sum+d[s[i]]
        return sum+d[s[len(s)-1]]
s = Solution()
print(s.romanToInt('IX'))
