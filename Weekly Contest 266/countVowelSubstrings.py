class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        ###solution! this is not the prettiest code i've ever made.
        
        
        #this is made much simpler because there are only 5 vowels to consider. the indices in vowelbools corresponds to the index of each vowel character 
        #in the vowels string.
        vowels = 'aeiou'
        vowelbools = [0, 0, 0, 0, 0]
        tot = 0
        c = 0
        while(c < len(word)):
            #if a character is a vowel
            if(word[c] in vowels):
                #we set the corresponding index in vowelbools to 1
                vowelbools[vowels.find(word[c])] = 1;
                for d in range(c, len(word)):
                    #break when the substring is interrupted by a consonant
                    if(not(word[d] == 'a' or word[d] == 'e' or word[d] == 'i' or word[d] == 'o' or word[d] == 'u')):
                        break
                    else:
                        vowelbools[vowels.find(word[d])] = 1;
                        
                    #kept for testing!
                    print(str(vowelbools) + ', ' + word[d] + ', ' + str(tot))
                    
                    #if everything in vowelbools is 1, that means all the vowels are now present
                    #any following substring in this run will also have all vowels present, so we can just keep adding one to total.
                    if(vowelbools[0] == 1 and vowelbools[1] == 1 and vowelbools[2] == 1 and vowelbools[3] == 1 and vowelbools[4] == 1 ):
                        tot+=1
            vowelbools = [0, 0, 0, 0, 0]
            c+=1
        return tot
