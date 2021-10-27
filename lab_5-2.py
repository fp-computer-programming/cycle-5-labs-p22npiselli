# Author: Nolan (AMDG) 10/27/2021

word1 = str(input("Enter any word in lowercase: "))
word2 = str(input("Enter another word in lowercase: "))
 
if word1 < word2:
    print(word1 + " comes before " + word2)
elif word1 > word2:
    print(word1 + " comes after " + word2)
else: 
    print(word1 + " is the same as " + word2)