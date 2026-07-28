# Q1. Write a program to calculate the sum of all keys in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4}.
# d = {1: 1, 2: 2, 3: 3, 4: 4}
# res=sum(d.keys())
# print(f"sum of all keys are {res}")
#--------------------------------------------------------------------------------------------------------------------------------
# Q2. Write a program to calculate the sum of all values in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4}
# d = {1: 1, 2: 2, 3: 3, 4: 4}
# res=sum(d.values())
# print(f"sum of all Values are {res}")

#--------------------------------------------------------------------------------------------------------------------------------
# Q3. Write a program to calculate the sum of both keys and values in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4}

# d = {1: 1, 2: 2, 3: 3, 4: 4}
# total = 0
# for key, value in d.items():
#     total += key + value

# print("Total sum of keys and values:", total)

#--------------------------------------------------------------------------------------------------------------------------------

# Q4. Create an empty dictionary called user_data. Allow the user to enter key-value pairs until they choose to stop. Print the final dictionary.
# user_data = {}

# while True:
#     key = input("Enter key: ")
#     value = input("Enter value: ")

#     user_data[key] = value

#     choice = input("Do you want to add another key-value pair? (yes/no): ")

#     if choice.lower() == "no":
#         break

# print("\nFinal Dictionary:")
# print(user_data)

#--------------------------------------------------------------------------------------------------------------------------------

# Q5. Write a program to calculate the total score of all students student_score = {1: 44, 2: 45, 3: 55}

# student_score = {1: 44, 2: 45, 3: 55}
# score=sum(student_score.values())
# print(f"the Score of all students : {score}")

#--------------------------------------------------------------------------------------------------------------------------------

# 6. Write a program to separate odd and even keys from a dictionary. Also count the total number of odd keys and even keys.

# d = {1: 1, 2: 2, 3: 3, 4: 4}

# even={}
# odd={}
# for key,values in d.items():
#     if values%2==0:
#         even[key]=values
#     else:
#         odd[key]=values
# print(f"even: {even},\nodd: {odd}")

#--------------------------------------------------------------------------------------------------------------------------------

# Q7. Write a program to find the greatest key in the dictionary player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}

# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
# greatest=max(player.keys())
# print(f"Greatest key : {greatest}")
# print(f"Player Name : {player[greatest]}")

#--------------------------------------------------------------------------------------------------------------------------------

# Q8. Write a program to extract alternate key-value pairs from the dictionary player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}

# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
# alternate=dict(list(player.items())[::2])
# print(f"Alternate key-value pairs : {alternate}")
#--------------------------------------------------------------------------------------------------------------------------------

# Q9. Write a program to fi nd all values that start with the letter ‘K’ player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
# k_values = [value for value in player.values() if value.startswith('K')]
# print(f"Values starting with 'K': {k_values}")
#--------------------------------------------------------------------------------------------------------------------------------
# Q10. Write a program to merge two dictionaries d1 = {1: "a", 2: "b"} d2 = {3: "c", 4: "d"}
# d1 = {1: "a", 2: "b"}
# d2 = {3: "c", 4: "d"}
# d1.update(d2)
# print(d1)
#--------------------------------------------------------------------------------------------------------------------------------
# Q11. Write a program to check whether a given key exists in the dictionary d = {1: 100, 2: 200, 3: 300}
# d = {1: 100, 2: 200, 3: 300}
# user_input=int(input("enter key to check : "))
# if user_input in d.keys():
#     print("yes")
# else:
#     print("No")
#--------------------------------------------------------------------------------------------------------------------------------
# Q12. Write a program to find the minimum value in the dictionary marks = {"A": 85, "B": 90, "C": 75, "D": 95}
# marks = {"A": 85, "B": 90, "C": 75, "D": 95}

# res=min(marks.values())
# print(res)
#--------------------------------------------------------------------------------------------------------------------------------
#  Q13. Write a program to find the minimum value in the dictionary marks = {"A": 85, "B": 90, "C": 75, "D": 95}
# marks = {"A": 85, "B": 90, "C": 75, "D": 95}

# res=max(marks.values())
# print(res)
#--------------------------------------------------------------------------------------------------------------------------------
# Q14. Write a program to swap keys and values in the dictionary

# d = {1: "one", 2: "two", 3: "three"}
# new_dic={}
# for key,values in d.items():
#     new_dic[values]=key
# print(new_dic)
#--------------------------------------------------------------------------------------------------------------------------------
# Q15. Write a program to remove a specific key (for example, key = 2) from the dictionary
# d = {1: 10, 2: 20, 3: 30}
# key=int(input("enter key to remove : "))
# res=d.pop(key)
# print(res)
# print(d)
#--------------------------------------------------------------------------------------------------------------------------------
# Q16. Write a program to count the frequency of each character in a string using a dictionary. Example: "banana"
# string = "banana"
# freq = {}
# for key in string:
#     freq[key] = freq.get(key, 0) + 1

# print(freq)
#--------------------------------------------------------------------------------------------------------------------------------
# 17. Write a program to create a dictionary where keys are numbers from 1 to 5 and values are their squares.

# dic={}

# for key in range(1,6):
#     dic[key]=key**2
# print(dic)
#--------------------------------------------------------------------------------------------------------------------------------
# Q18. Write a program to find the total number of items in the dictionary

# d = {"apple": 5, "banana": 7, "cherry": 3}
# res=len(d)
# print(res)
#--------------------------------------------------------------------------------------------------------------------------------
# 19. Write a program to sort a dictionary by its keys
# d = {3: "three", 1: "one", 2: "two"}
# new_dic={}
# for key in sorted(d):
#     new_dic[key]=d[key]

# print(new_dic)
#--------------------------------------------------------------------------------------------------------------------------------
# Q20. Write a program to count how many values are greater than 50 in a dictionary.
# dict = {"A": 45, "B": 60, "C": 75, "D": 80}
# count=0
# for i in dict.values():
#     if i >50:
#         count+=1
# print(count)
#--------------------------------------------------------------------------------------------------------------------------------
# Q21. Write a program to find the key with the highest value in a dictionary.

# student = {"A": 45, "B": 60, "C": 75, "D": 80}

# highest_key = max(student, key=student.get)

# print(f"Highest key is {highest_key} : {student[highest_key]}")
#--------------------------------------------------------------------------------------------------------------------------------
# 22. Write a program to update a value in a dictionary if the key exists; otherwise,add the key.

# student = {"A": 45, "B": 60, "C": 75, "D": 80}
# key=input("enter key to insert/update: ")
# value=int(input("enter key to insert/update: "))

# if key in student:
#     student[key]=value
#     print("key already in dictonary hence key updated")
#     print(student)
# else:
#     student[key]=value
#     print("key not in dictonary hence key added")
#     print(student)
#--------------------------------------------------------------------------------------------------------------------------------
# 23. Write a program to convert two lists into a dictionary
# keys = [1, 2, 3] 
# values = ["a", "b", "c"]
# dict1=dict(zip(values,keys))
# print(dict1)
#--------------------------------------------------------------------------------------------------------------------------------
# Q24. Write a program to remove duplicate values from a dictionary.

# student = {"A": 45,"B": 60,"C": 45,"D": 80,"E": 60}

# result = {}
# seen = set()

# for key, value in student.items():
#     if value not in seen:
#         result[key] = value
#         seen.add(value)

# print(result)
#--------------------------------------------------------------------------------------------------------------------------------

# Q25. Write a program to check whether all values in a dictionary are unique.
# student = {"A": 45,"B": 60,"C": 45,"D": 80,"E": 60}
# if len(student.values())==len(set(student.values())):
#     print("unique")
# else:
#     print("not unique")
#--------------------------------------------------------------------------------------------------------------------------------