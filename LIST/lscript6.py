def createlist():
    n=int(input("Enter a number of list element you want:"))
    l=[]
    for i in range(0,n):
        l.append(int(input("Enter a elment of list {}:".format(i))))
    return l
def evenodd(l):
    even=[]
    odd=[]
    e=0
    o=0
    for i in l:
        if(i%2==0):
            even.append(i)
            e=e+1
        else:
            odd.append(i)
            o=o+1
    print("The total number of even are {}: {}".format(e,even))
    print("The total number of odd are {}: {}".format(o,odd))



k=createlist()
evenodd(k)

