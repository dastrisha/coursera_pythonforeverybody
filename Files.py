fname = input("Enter file name here: ")
fhand = open(fname)
count = 0 
for line in fhand :
    if line.startswith("subject: ") :
        count = count + 1
print("There were", count, "subject lines in" , fname)



