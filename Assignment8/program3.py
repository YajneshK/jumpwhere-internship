class SubsetGenerator:
    def __init__(self):
        pass
    
    def get_subsets(self, nums):
        if not nums:
            return [[]]
        
        subsets = []
        self._generate_subsets(nums, [], subsets)
        return subsets
    
    def _generate_subsets(self, nums, current, subsets):
        subsets.append(current)
        
        for i in range(len(nums)):
            self._generate_subsets(nums[i+1:], current + [nums[i]], subsets)