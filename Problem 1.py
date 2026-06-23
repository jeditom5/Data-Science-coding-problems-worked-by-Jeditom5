# this problem is about finding anagrams
import re
def anagramchecker(s1,s2):
    return sorted(list(re.sub(r'\W','',s1))) == sorted(list(re.sub(r'\W','',s2)))
# now that we have a solution lets test it
print(anagramchecker("public relations","crap built on lies."))# true
print(anagramchecker("aa", "cc"))# false
print(anagramchecker("aba", "baa"))# true
print(anagramchecker("aba", "baaa"))# false
print(anagramchecker("",""))# true
print(anagramchecker('.....::@!##@#$#',"#!@$%$%^&&&"))# true since there are no letters in these strings


