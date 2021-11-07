class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = 'aeiou'
        vowelbools = [0, 0, 0, 0, 0]
        tot = 0
        c = 0
        while(c < len(word)):
            if(word[c] in vowels):
                vowelbools[vowels.find(word[c])] = 1;
                for d in range(c, len(word)):
                    if(not(word[d] == 'a' or word[d] == 'e' or word[d] == 'i' or word[d] == 'o' or word[d] == 'u')):
                        break
                    else:
                        vowelbools[vowels.find(word[d])] = 1;
                    print(str(vowelbools) + ', ' + word[d] + ', ' + str(tot))
                    if(vowelbools[0] == 1 and vowelbools[1] == 1 and vowelbools[2] == 1 and vowelbools[3] == 1 and vowelbools[4] == 1 ):
                        tot+=1
            vowelbools = [0, 0, 0, 0, 0]
            c+=1
        return tot
