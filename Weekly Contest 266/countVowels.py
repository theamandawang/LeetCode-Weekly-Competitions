class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        #this solution exceeded the time limit, but gave correct results.
        #attempt at dynamic programming
        total = 0
        temp = 0
        numvows = 0
        for i in range(len(word)):
            numvows = 0
            temp = 0
            for j in range(i, len(word)):
                if(word[j] in 'aeiou'):
                    numvows += 1
                    temp += numvows
                    
                else:
                    temp += numvows
            total+=temp
        return total
      
      #this solution is O(n^2), and there is an obvious solution that can be done by
      #iterating through the loop once and storing each of the individual vowel counts for each substring (that always includes the '0' index
      #then, it should be easy to see that for following substrings that start at '1', for instance have a sum of vowels equal to
      
      ### I HAVE NOT TESTED THIS YET
      #   (total sum for '0' index) - (length of word) * (individual sum for very first substring)
      
      #   generalized, this should be (total sum for '0' index) - (length of word) * (individual sum for substring prior to the current index)
      
      # the sum of these sums should be at the end, 
      #(length of word) * (total sum for '0' index) - (length of word) * (total sum for '0' index - subsum for 'n-1' index)
