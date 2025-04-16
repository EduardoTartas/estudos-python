class Solution(object):
    def twoSum(self, nums, target):   
        for i in range(len(nums)):
            for x in range(len(nums)):
                if i == x:
                    continue
                if nums[i] + nums[x] == target:
                    return [i, x]  
                


    #print(twoSum(0,[3,2,3], 6))

#---------
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

    #print(isPalindrome(0, 121))

#---------
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        
        return total

  
    print(romanToInt(0,"III"))
