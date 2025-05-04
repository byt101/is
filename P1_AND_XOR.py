# Write a Java/C/C++/Python program that contains a string (char pointer) with a value HelloWorld9. The program should AND or and XOR each character in this string with 127 and display the result.

s = "HelloWorld9"

print("Original String:", s)
print("\nChar|AND-127|XOR-127")

and_str = ''
xor_str = ''

for c in s:
    a = ord(c) & 127
    x = ord(c) ^ 127
    and_str += chr(a)
    xor_str += chr(x)
    print(c,"  |",a,"  |",x)

print("\nString after AND with 127:", and_str)
print("String after XOR with 127:", xor_str)