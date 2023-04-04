def strcount(l):
    s=0   
    for i in l:
        k=len(i)
        if(k%2==0):
            print(i)
            s=s+1
    print("Total string of even number of character:{}".format(s))

l=[]
for i in range(0,5):
    str=input("Enter string : ")
    l.append(str)
print(l)
strcount(l)