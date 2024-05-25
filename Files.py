# fname = input("Enter file name here: ")
# fhand = open(fname)
# count = 0 
# for line in fhand :
#     if line.startswith("subject:") :
#         count = count + 1
# print("There were", count, "subject lines in" , fhand)

"""Assignment question"""
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
float_numbers = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    final_float = float(line.split(":")[1]) #[1]this accesses the second element of the list created by the split method.
    float_numbers.append(final_float)
# print (float_numbers)
    #print (ffinal_float)

count = 0
total = 0

for number in float_numbers:
    count = count + 1
    # print (count)
    total = total + number
print ("Average spam confidence: ", total/count)














