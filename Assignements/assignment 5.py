#Q1. Filter vowels and consonants from the string "How are you sir".

# str1= "How are you sir"
# vowels=""
# consonents=""
# for i in str1:
#     if i in "aeiouAEIOU":
#         vowels+=i
#     else:
#         consonents+=i
# print(f"volwels from string :  {vowels}")
# print(f"consonents from string :  {consonents}")

# Q2. Count vowels and consonants in the string "How are you sir".

# str1= "How are you sir"
# vowels=0
# consonents=0
# for i in str1:
#     if i in "aeiouAEIOU":
#         vowels+=1
#     else:
#         consonents+=1
# print(f"volwels count from string : {vowels}")
# print(f"consonents count from string : {consonents}")

# Q3. Reverse the string "How are you sir".

# str1= "How are you sir"
# print(str1[::-1])

# Q4. Convert lowercase letters to uppercase in the string "How are you sir".

# str1= "How are you sir"
# new_str=""
# for i in str1:
#     if i.islower():
#         new_str+=i.upper()
#     else:
#         new_str+=i
# print(new_str)

# Q5. Remove duplicate letters from the string "this is python programming place".

# string = "this is python programming place"
# new_str=""
# for i in string:
#     if string.count(i)>1:
#         i+=i
#     else:
#         new_str+=i
# print(new_str)
        
# Q6. Search for a specific character in the string "this is pyth@n programm!ng place".

# string = "this is pyth@n programm!ng place"
# new_str=input("enter text to find = ")
# if new_str in string:
#     print(f"{new_str} is present in string {string}")
# else:
#     print(f"{new_str} is not present in string {string}")



# Q7. Find the greatest and smallest characters from the string "venugopaliyer"
# string = "VeNuGoPaLiYeR"
# low_str=""
# upper_str=""
# for i in string:
#     if "A"<i<="Z" or i.isupper():
#         upper_str+=i
#     else:
#         low_str+=i
# print(f"lower string from {string} is : {low_str}")
# print(f"upper string from {string} is : {upper_str}")
        

# Q8. Count the total occurrences of a specific letter in the string "this is python programming place".

# string = "this is python programming place"
# letter= input(f"enter text to find in the string {string} = ")
# count=string.count(letter)
# print(f"count of {letter} in the string {string} is {count}")

#Q9. Replace "python" with "javascript" in the string "python developer python engineer python holder".

# string ="python developer python engineer python holder"
# new_str=string.replace("python","javascript")
# print(new_str)

# Q10. Print alternate letters from the string "How are you sir".

# string = "How are you sir"
# new_str=""
# for i in range(0,len(string),2):
#     new_str+=string[i]
# print(new_str)

# Q11. Convert the string "qwertyuiopasdfghjklzxcvbnm" to "abcdefghijklmnopqrstuvwxyz".

# string = "qwertyuiopasdfghjklzxcvbnm"
# new_str="".join(sorted(string))
# print(new_str)

# Q12. Check if the string is a palindrome (e.g., "madam" → Palindrome, "hello" → Not palindrome).

# str1=input("enter text = ")
# rev_str=str1[::-1]
# if str1==rev_str:
#     print(f"{str1} is a palindrome")
# else:
#     print(f"{str1} is not a palindrome")

# Q13. Count spaces, digits, alphabets, and special characters in "Python 3.9 is awesome!!"

# str1 = "Python 3.9 is awesome!!"
# space_count=0
# digit_count=0
# alphabets_count=0
# special_char_count=0
# for i in str1:
#     if i.isalpha():
#         alphabets_count+=1
#     if i.isdigit():
#         digit_count+=1
#     if i==" ":
#         space_count+=1
#     else:
#         special_char_count+=1
# print(f"count of special char in string {str1} is {special_char_count}")
# print(f"count of alphabets char in string {str1} is {alphabets_count}")
# print(f"count of digits in string {str1} is {digit_count}")
# print(f"count of spaces char in string {str1} is {space_count}")

# Q14. Find the longest word in the string "Python programming is interesting".

# string = "Python programming is interesting"
# new_lis=string.split()
# new_str=""

# for i in new_lis:
#     if len(i) > len(new_str):
#         new_str =i
#     else:
#         i+=i
# print(new_str)

# Q15. Capitalize the first letter of each word in "welcome to python world".

# string="welcome to python world"
# new_lis=string.split()
# new_str=""
# for i in new_lis:
#    new_str+=i.capitalize()+" "
# print(new_str)

# Q16. Remove all spaces from "How are you sir".

# string = "How are you sir"
# new_str=string.replace(" ","")
# print(new_str)

# Q17. Check if all characters in the string are unique (e.g., "abcde" → True, "hello" → False).

# string=input("enter string to check = ")
# is_unique=True

# for i in string:
#     if string.count(i)>1:
#         is_unique=False
#         break
# print(is_unique)

# Q18. Sort characters alphabetically in "programming" → "aggimmnoprr".

# string="programming"
# new_str="".join(sorted(string))
# print(new_str)

# Q19. Swap cases of all letters in "Python Is Fun" → "pYTHON iS fUN".

# string="Python Is Fun"
# name_str=""
# for i in string:
#     if i.islower():
#         name_str+=i.upper()
#     elif i.isupper():
#         name_str+=i.lower()
#     else:
#         name_str+=i
# print(name_str)

# Q20. Find frequency of each character in "banana" → { 'b':1, 'a':3, 'n':2 }.

# string=input("enter string : ")
# freq = {}

# for i in string:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)

# Q21. Remove vowels from "How are you sir" → "Hw r y sr".

# string="How are you sir"
# vowels="aeiouAeiou"
# for i in vowels:
#     string=string.replace(i,"")
# print(string)

# Q22. Check if a substring exists in "Python programming" (e.g., "thon" → Found).
# string="Python programming"
# sub_str=input("enter substring to find : ")
# if sub_str in string:
#     print(f"{sub_str} is present in {string}")
# else:
#     print(f"{sub_str} is not present in {string}")

# Q23. Print words in reverse order in "How are you sir" → "sir you are How".

# string="How are you sir"
# new_lis=" ".join(string.split()[::-1])
# print(new_lis)

# Q24. Count words in the string "This is a python assignment".

# string = "This is a python assignment"
# lis=string.split()
# print(len(lis))

# Q25. Find the ASCII value of each character in "ABcd".

# str1="ABcd"
# for i in str1:
#     print(i,":",ord(i))

# Q26. Convert a string into a list of words using "split()" (e.g., "Python is fun" → ["Python", "is", "fun"]).

# string="Python is fun"
# lis=string.split()
# print(lis)

# Q27. Join a list of words into a string using "join()" (e.g., ["Python", "is", "fun"] → "Python is fun").

# lis=["Python", "is", "fun"]
# string=" ".join(lis)
# print(f'"{string}"')

# Q28. Find the first non-repeating character in "swiss" → "w".

# string="swiss"
# for i in string:
#     if string.count(i)==1:
#         break
# print(i)


# Q29. Check if two strings are anagrams (e.g., "listen" and "silent" → Anagrams).
# string1="listen"
# string2="silent"
# if sorted(string1)==sorted(string2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

# Q30. Replace all spaces with hyphens (-) in "Python is easy to learn" → "Python-is-easy-to-learn".

# string="Python is easy to learn"
# new_str=string.replace(" ","-")
# print(new_str)

# Q31. Extract a substring from "Python Programming" → from index 0 to 6 should give "Python".
# string="Python Programming"
# sub_str=string[0:6]
# print(sub_str)

# Q32. Check if one string is a substring of another (e.g., "gram" is a substring of "Programming").
# string="python programming"
# sub_str=input("enter substring to check = ")
# if sub_str in string:
#     print("It is present")
# else:
#     print("It is not present")

# Q33. Find all occurrences of a substring in "This is Python and Python is fun" → Substring "Python".
# string="This is Python and Python is fun"
# lis=string.split()
# sub_str=input("enter text to search : ")
# for i in range(len(lis)):
#     if lis[i]==sub_str:
#         print(f"index of {sub_str} is {i}")

# Q34. Replace a substring in "I like Python" → Replace "Python" with "Java".

# string="I like Python"
# res=string.replace("python","java")
# print(res)

# Q35. Remove a substring from "HelloWorld" → Remove "World" → "Hello".

# string="HelloWorld"
# sub_str=input("enter substring : ")
# res=string.replace(sub_str.lower()),"")
# print(res)

# Q36. Count occurrences of a substring in "banana" → Substring "ana" appears 2 times.
# string="banana"
# sub_str=input("enter substring to find : ")
# res=string.count(sub_str)
# print(res)

# Q37. Check if a string starts with a substring (e.g., "Python is easy" starts with "Python").
# string="Python is easy"
# sub_str=input("enter text to find : ")
# if string.lower().startswith(sub_str.lower()):
#     print("Yes")
# else:
#     print("No")

# Q38. Check if a string ends with a substring (e.g., "Learn coding" ends with "coding").

# string="Learn coding"
# sub_str=input("enter text: ")
# if string.lower().endswith(sub_str.lower()):
#     print("Yes")
# else:
#     print("No")

# Q39. Split a string based on a substring (e.g., "apple,banana,grapes" → Split by "," → ["apple", "banana", "grapes"]).

# string="apple,banana,grapes"
# res=string.split(",")
# print(res)

# Q40. Find the index of the first occurrence of a substring in "Programming is great" → Substring "is" → Index 12.

# string="Programming is great"
# sub_str=input("enter text to find : ")
# index=string.find(sub_str)
# if index != -1:
#     print(f"{sub_str} found at index {index}")
# else:
#     print("Substring not found")

# Q41. Find the index of the last occurrence of a substring in "Programming in Python Programming" → Substring "Programming".
# string="Programming in Python Programming"
# sub_str="Programming"
# index=string.rfind(sub_str)
# print(index)

# Q42. Extract substring after a specific word (e.g., "Welcome to Python World" → substring after "to" → "Python World").

# string = "Welcome to Python World"
# sub_str = "to"

# index = string.find(sub_str)

# new_str = string[index + len(sub_str) + 1:]

# print(new_str)

# Q43. Extract substring before a specific word (e.g., "Welcome to Python World" → substring before "Python" → "Welcome to").

# string = "Welcome to Python World"
# sub_str = "to"

# index = string.find(sub_str)

# new_str = string[:index]

# print(new_str)

# Q44. Check if two strings are rotations (cyclic substrings) of each other (e.g., "abcd" and "cdab" → Rotations).

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if len(str1) == len(str2) and str2 in (str1 + str1):
#     print("Rotations")
# else:
#     print("Not Rotations")

# Q45. Find the longest common substring between two strings (e.g., "abcdxyz" and "xyzabcd" → Longest common substring = "abcd").

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# longest = ""

# for i in range(len(str1)):
#     for j in range(i + 1, len(str1) + 1):
#         sub = str1[i:j]

#         if sub in str2 and len(sub) > len(longest):
#             longest = sub

# print("Longest Common Substring:", longest)