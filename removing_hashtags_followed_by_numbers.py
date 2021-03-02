# removing of hashtags followed by numbers (e.g.: #18476) from a text file
import re


f_path = "D:/915.txt"
#s = ""

with open(f_path) as doc_:
    s = doc_.read()

print(s)
l = s.split("\n")
print(l)


l1 = []
for i in l:
    l1.append(re.sub("\#+[0-9]+", "", i))

print("---------")
print(l1)

with open(f_path, 'a+') as doc_:
    doc_.write("\n\n---------------------------------\n\n")
    for i in l1:
        doc_.write(i + "\n")
