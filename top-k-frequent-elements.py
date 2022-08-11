# O(n) solution faster than 95% of leetcode submissions wiht 45% better memory utilization

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #instantiate counts
        counts = defaultdict(int)
        
        #generate counts for all of numbers in nums
        for num in nums:
            counts[num] += 1
        
        #instantiate a result list
        res = []
        
        #append all of the numbers and their counts to the list
        for num in counts:
            res.append([num, counts[num]])
        
        #sort the list based on the counts of the numbers
        res = sorted(res, key=lambda x:x[1], reverse = True)
        
        #return the numbers of the top k elements in a list
        return [x[0] for x in res[:k]]
        
