str=input("Enter any sentence:")
c=str.split()
l=[]
print(c)
p=0
for i in c:
    v=i[::-1]
    if(v==i):
        print(i)
        l.append(i)
        p=p+1

print("Total {} palindrome words in string:{}".format(p,l))
