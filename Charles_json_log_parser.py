import json


TEXT_INTRO = "Hello! This is a helper for analyzing tracked Omniture events logged with Charles." \
             "\nIt allows to see list of all the logged actions and " \
             "check list of parameters for each unique action." \
             "\nIt does not allow tester to skip manual investigation of tracking, " \
             "though simplifies it and makes some critical issues obvious." \
             "\n\nTo use this helper:" \
             "\n1. Connect device to Charles and perform different actions that are to be tracked." \
             "\n2. Remove all other content except events for Omniture hosted at https://waterfrontmedia.sc.omtrdc.net" \
             "\n3. Export the Charles log to JSON: File / Export session / JSON Session File and pick any name with *.chlsj extension." \
             "\n4. Specify path to JSON file below." \
             "\n5. Click \"Enter\" and find the report.txt file in the same catalog."
TEXT_INVITE = "\nNow, please specify file pah and name - like D:\\Some_catalog\\filename.chlsj - below:\n"

print(TEXT_INTRO)
file_pathname = raw_input(TEXT_INVITE)
try:
    last_slash_index = file_pathname.rfind("\\")
except IOError:
    print("File not found.")

filename = file_pathname[last_slash_index+1:]
directory = file_pathname[0:last_slash_index+1]

print(filename)
print(directory)

try:
    json_string = open(directory + filename)\
        .read()\
        .decode('utf-8')\
        .replace("%3D"," ")\
        .replace("%20"," ")\
        .replace("%2F","/")\
        .replace("%2C",",")\
        .replace("%3A",":")\
        .replace("%7C","|")\
        .replace("%28","(")\
        .replace("%29",")")\
        .replace("%27","'")\
        .replace("%21","!")
except IOError:
    raw_input("Error occured with JSON file path, name or it's content."
              "\nCheck the file and come back again."
              "\nNow, please press any button to quit the program.")
    quit()

print("JSON string: " + json_string)
json_obj = json.loads(json_string)

#print(len(json_obj[0])) #debug
#print(json_obj[0].get("status")) #debug
#print(json_obj[0].get("actualPort")) #debug

tracked_actions_string = []
for i in range(len(json_obj)):
    tracked_actions_string.append(json_obj[i]
        .get("request")
        .get("body")
        .get("text"))
    #print "Strings: " + str(tracked_actions_string[i]) #debug

tracked_actions_list = []
for i2 in range(len(tracked_actions_string)):
    tracked_actions_list.append(tracked_actions_string[i2].split('&'))
    #print "Lists: " + str(tracked_actions_list[i2]) #debug


events_dics = []
for i3 in range(len(tracked_actions_list)):
    tracked_actions_dic = {}
    for n in range(len(tracked_actions_list[i3])):
        dic_pair = tracked_actions_list[i3][n].split('=')
        if len(dic_pair) == 1:
            dic_pair.append('NULL')
        tracked_actions_dic[dic_pair[0]]=dic_pair[1]
    events_dics.append(tracked_actions_dic)
print ('------------------------------')

events_number = len(events_dics)
print(
"Parsing completed. " \
"\nNumber of events  in  file - " + str(len(json_obj)) + \
"\nNumber of processed events - " + str(events_number)
)

actions = []
for k in range(events_number):
    try:
        #print(events_dics[k]['action']) #debug
        actions.append(events_dics[k]['action'])
    except KeyError:
        1+1
actions_unique = list(sorted(set(actions)))

print(actions)
print(actions_unique)
print("============================"* 4)

filereport_path = directory + "report.txt"
filereport = open(filereport_path, "w+"
                                   "")
filereport.write("Number of unique actions: " + str(len(actions_unique)) + "\n")
filereport.write("\nUnique actions are: ")
for i in actions_unique:
    filereport.write("\n" + str(i))
filereport.write("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                 "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

print("Unique actions with their dimensions:\n")

for i in range(len(actions_unique)):
    action_value = actions_unique[i]
    for k in range(len(events_dics)):
        try:
            if events_dics[k]['action'] == action_value:
                print("Action = " + str(action_value) + ":")
                print(events_dics[k])
                filereport.write("Action = " + str(action_value) + ":\n")

                filereport.write("Number of parameters: " + str(len(events_dics[k])))
                for l, m in sorted(events_dics[k].iteritems()):
                    filereport.write("\n" + str(l) + "=" + str(m))

                #filereport.write(str(events_dics)) #debug
                filereport.write("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
                break
        except KeyError:
            1+1
filereport.close()
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Report is consoled above and written to: " + filereport_path)
raw_input("\nPlease press any button to quit the program.")
print("Bye!")
