class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        result=[]

        def backtrack(remaining, current):

            
            result.append(list(current))


            for end in range(0, len(remaining)):

                current.append(remaining[end])
                backtrack(remaining[end+1:], current)
                current.pop()


        backtrack(nums, [])

        return result