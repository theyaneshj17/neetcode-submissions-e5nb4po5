class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def is_palindrome(s):
            l,r=0, len(s)-1

            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        result=[]

        def backtrack(remaining, current):

            if remaining =="":
                result.append(list(current))
                return

            for end in range(len(remaining)):

                slice = remaining[0:end+1]
                if not is_palindrome(slice):
                    continue

                current.append(slice)
                backtrack(remaining[end+1:], current)
                current.pop()

        backtrack(s, [])

        return result