
text = input("Enter a string : ")


def rev(text, i):
    if i < 0:
        return ""
    
    return text[i] + rev(text, i-1)

res = rev(text, len(text))

if text == res:
    print("Palindrome")
else:
    print("It is not palindrome")
