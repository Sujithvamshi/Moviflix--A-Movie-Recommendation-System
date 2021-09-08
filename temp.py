s1=input()
s2=input()
if sorted(set(s1)) == sorted(set(s2)):
    print("Anagram")
else :
    print("Not Anagram")
