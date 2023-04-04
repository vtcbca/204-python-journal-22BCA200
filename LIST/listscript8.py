list=[5,10,15,20,25,50,20]
replace=int(input("Enter a value you want to replace:"))
newvalue=(int(input("Enter a value you want instead of old: ")))
for i in range(len(list)):
    if(list[i]==replace):
        list[i]=newvalue
print(list)