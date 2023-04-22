class PairFinder:
    def __init__(self):
        pass
    
    def find_pair(self, nums, target):
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return [num_indices[complement], i]
            
            num_indices[num] = i
        
        return None