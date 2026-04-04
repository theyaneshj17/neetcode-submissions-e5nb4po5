class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        '''    
        Say given 234

        2-abc
        3-def
        4-ghi

        it will be adg, adh, adi, bdg, dbh

        itis same as wearing top, bottom shoe problem

        top =['a', 'b', 'c']
        bottom =['d', 'e', 'f']
        shoes =['g','h', 'i']

        so, 
        #Lets built hashmap from 2 to 9, 
        which gives choices as ['abc', 'def', 'ghi']


        Now the questions, is how do we know which layer we're at
        like current =top like we alreayd wore top, now bottom, next shoe

        current="", nothing

        current="a", which means we wore top
        current ="ad", top+bottom

        len(current), will tell you which layer you're in


        wearing []        → len=0 → picking top
        wearing ["T1"]    → len=1 → picking bottom
        wearing ["T1","B1"] → len=2 → picking shoe


        current=""   → picked 0 letters so far → I'm on layer 0
        current="a"  → picked 1 letter so far  → I'm on layer 1
        current="ad" → picked 2 letters so far → I'm on layer 2
       
       
       
        choices 2--abc, 

        The thing is la

        ##Base case, 
        if len(current) ==len(digits): result.append(current) return



     


        '''


        hashmap={}

        hashmap[2]="abc"
        hashmap[3]="def"
        hashmap[4]="ghi"
        hashmap[5]="jkl"
        hashmap[6]="mno"
        hashmap[7]="pqrs"
        hashmap[8]="tuv"
        hashmap[9]="wxyz"

        choices=[]

        for digit in digits:

            choices.append(hashmap[int(digit)])

        print(choices)




        ##Now i've ['def', 'ghi'], The thing is i just need to form dg, dh, di

        result=[]

        if not digits:
            return result

        def backtrack(current):

            if len(current)== len(digits):
                result.append(current)
                return



            layer = len(current)
            choices_at_this_layer = choices[layer]

            for letter in choices_at_this_layer:

                
                backtrack(current+letter)
                #current = current[0:len(current)]



        

        backtrack("")



        return result

