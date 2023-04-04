filename=["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
l=[]
for i in filename:
    if(i.endswith(".c")):
        l.append(i[:-2]+".py")
    else:
        l.append(i)
print(l)