"""
Q3.Write a Python code to remove all characters except a            
Sample String : 'exercises' 
Expected Result : 'eee' (Removed all characters except special character : e) """

user_input=input("Enter the string")
character=input("character")
result=[]

for char in user_input:
    if char==character:
        result.append(char)
output = "".join(result)
print(output)



