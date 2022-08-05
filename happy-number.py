#Solution faster than 50% and better memory usage than 95% of all leetcode solutions.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #create a hashmap to track numbers we have already seen
        seen = defaultdict(int)
        
        #loop until n = 1
        while n > 1:
            
            #cast n as a string
            temp = n
            #reset n to 0
            n = 0
            
            #loop through the digits in n
            for digit in temp:
                #sum the squares of the digits
                n += int(digit) ** 2
            
            #if we have already seen n, we are in a loop and return false
            if seen[n] > 0:
                return False
            
            #if not, then we update the hashmap
            else:
                seen[n] = 1
        
        #if we break out of the loop, no cycle so return true
        return True
                
        
