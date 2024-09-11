answer = input("Enter two space-separated characters: ")
char1, char2 = answer.split()

ascii_1 = ord(char1)
ascii_2 = ord(char2)

larger_char = max(char1, char2, key=ord)

print("-------------------------")
print(f"The character with greater value is: {larger_char}")
print("Showing ASCII Values: ")
print(f"{char1} : {ascii_1}")
print(f"{char2} : {ascii_2}")