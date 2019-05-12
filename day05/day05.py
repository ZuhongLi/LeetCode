
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
