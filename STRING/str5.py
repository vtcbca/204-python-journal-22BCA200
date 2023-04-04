def symme(s):
    h = len(s) 
    x = s[:h]
    y = s[h:]
    if x == y:
        print("String is symmetric.")
    else:
        print("String is not symmetric.")

def inputstr():
    a = input("Enter a string:")
    symme(a)

inputstr()
