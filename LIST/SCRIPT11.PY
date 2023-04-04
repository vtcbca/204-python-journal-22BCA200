def d(w):
    d = {}
    l = int(input("Enter minimum word length: "))
    for i in w:
        if len(i) >= l:
            d[i] = len(i)
    print(d)

def i():
    s = input("Enter a sentence: ")
    w = s.split()
    d(w)

i()
