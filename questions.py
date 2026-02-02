'''
Docstring for Datas.py.Opertaors.questions

STRING
1. Case Conversion + Membership  
   - Take a string(sentence) from the user.  
   - Convert it to lowercase using .lower().  
   - Check whether the word "python" exists in the string (membership operator in).  
2. Uppercase Conversion + Check  
   - Input a string(sentence) from the user.  
   - Convert it to uppercase using .upper().  
   - Check if the converted string contains "HELLO".   
3. Strip + Membership  
   - Take a string input from the user with extra spaces at the beginning and end.  
   - Remove spaces using .strip().  
   - Check if it starts with "Hi" using .startswith().  
4. Replace + Membership  
   - Input a string from the user.  
   - Replace all spaces with "-" using .replace().  
   - Check whether "-" is present in the modified string.  
   
5. Take a sentence as input from the user.  
   - Convert it into a list of words using .split().  
   - Access and print the first and last word from the list.

'''

# 1 Case Conversion + Membership  
#    - Take a string(sentence) from the user.  
#    - Convert it to lowercase using .lower().  
#    - Check whether the word "python" exists in the string (membership operator in).  

s = input("Enter a sentence : ").lower()
w = "python"

# print(w in s)

'''
2. Uppercase Conversion + Check  
   - Input a string(sentence) from the user.  
   - Convert it to uppercase using .upper().  
   - Check if the converted string contains "HELLO". 

'''

s = input("Enter the String :").upper()
w = "HELLO"
# print(w in s)

'''
3. Strip + Membership  
   - Take a string input from the user with extra spaces at the beginning and end.  
   - Remove spaces using .strip().  
   - Check if it starts with "Hi" using .startswith(). 

'''

user = input("   Enter the  Sentence.").strip()
remove = user.startswith("Hi")
print(remove in user)