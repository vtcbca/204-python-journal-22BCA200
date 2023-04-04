studlist = []

while (more_student=='y' or'Y'):
    sid = int(input("Enter student ID: "))
    sname = input("Enter student name: ")
    spercentage = float(input("Enter student percentage: "))
    
    studlist.extend([sid, sname, spercentage])
    
    more_students = input("Do you want to enter details for more students? (yes=Y/y, No=N/n): ")
    if more_students== 'n' or 'N':
        break

studdict = {}
for i in range(0, len(studlist), 3):
    id = studlist[i]
    name = studlist[i+1]
    percentage = studlist[i+2]
    studdict[id] = [name, percentage]

print("List:", studlist)
print("Dictionary:", studdict)