def get_str(text):
    if len(text)<2:
        return ""
    return text[:2]+text[-2:]

my_string=input("enter a string :")
print("new modified string is :", get_str(my_string))