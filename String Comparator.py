str_1='Some VeryVery LongString with id 1 and a lot of text after that if...'
str_2='Some VeryVery LongString with id 2 and a lot of text after that if...'

diff_1 = ""
diff_2 = ""
diff_start_index = 0
for k in range(0,len(str_2)):
    if str_1[k] != str_2[k]:
        diff_start_index = k

for i in range(0,len(str_2)):
    if str_1[i] == str_2[i]:
        pass
    else:
        diff_1 += str_1[i]
        diff_2 += str_2[i]
print("\nStrings are different starting from character № %d\n"
      % diff_start_index)
print("String 1: " + diff_1)
print("String 2: " + diff_2)
