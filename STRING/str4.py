a = []  # change variable name to small letters
b = "y"

while b == "y" or b == "Y":
    print("\n1. Add items to list.")
    print("\n2. Print strings with even length.")
    print("\n3. Replace odd characters of string with index number.")
    print("\n4. Extract characters from string based on start and end index.\n")
    
    c = int(input("Enter your choice: "))

    if c == 1:
        x = "y"
        while x == "y" or x == "Y":
            i = input("Enter your string: ")
            a.append(i)
            x = input("Add string (y/Y): ")

    elif c == 2:
        v = []
        count = 0
        for i in a:
            if len(i) % 2 == 0:
                v.append(i)
                count += 1
        if count > 0:
            print("Strings with even length: ", v)
        else:
            print("No strings with even length.")

    b = input("Do you want to continue (y/Y): ")
