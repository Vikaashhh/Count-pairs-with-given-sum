class Solution:
    # Function to count pairs with given sum
    def countPairs(self, arr, target):
        freq = {}  # Dictionary to store frequencies
        count = 0  # Pair count ka counter

        for num in arr:
            # Check karo kya (target - num) pehle aaya tha
            complement = target - num
            if complement in freq:
                count += freq[complement]  # Kitni baar complement aaya hai, utne pairs banenge
            
            # Ab is number ko frequency map me daal do
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        return count
