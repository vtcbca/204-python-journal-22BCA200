def consecutive_common(n):
    count = 0
    result = []
    for i in range(len(n) - 2):
        if n[i] == n[i + 1] and n[i + 1] == n[i + 2]:
            result.append(n[i])
            count += 1
    if count > 0:
        print(f"Consecutive common numbers in list {n} are: {result}")
    else:
        print("No consecutive numbers in list!")

def take_input():
    lst = []
    n = int(input("How many numbers do you want to enter in the list? "))
    for i in range(n):
        num = int(input("Enter a number: "))
        lst.append(num)
    consecutive_common(lst)

take_input()
