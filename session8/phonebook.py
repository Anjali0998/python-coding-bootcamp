numbers_of_entries = int(input("Enter number of entries"))

print("okay, Enter name and numbers respectively for each of them")

file = open("num.txt", "w")

for i in range(0, numbers_of_entries):
    name=input("name: ")
    number=input("number: ")
    entry= f"{name}: {number}\n"
    file.write(entry)
    if i==(numbers_of_entries -1):
        print("Done!")
    else:
        print("okay next one!")

 file.close()
            