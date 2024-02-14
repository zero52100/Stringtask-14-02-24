"""
Q2.Print even length words in a string. 
Sample String : ''I love coding" 
Expected Result : “love, coding” """


input_string = input("Enter a string: ")
words = input_string.split()
even = []

for i in words:
    if len(i) % 2 == 0:
        even.append(i)
result = ", ".join(even)
print("Even length word:", result)
