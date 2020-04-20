#!/usr/bin/env python3.7
import re
import csv
import sys
import operator
logfile = sys.argv[1]
count = {}
def extract_log(logfile):
    with open(logfile) as f:
        line = f.readlines()

    for log in line:
        error_pattern = r"(?<=ERROR ).*?(?= \()"
        result = re.search(error_pattern,log)
        print(result)
        if result:
            if result[0] not in count:
                count[result[0]] = 0
            count[result[0]] += 1
    print(count)
    count1 = sorted(count.items(),key=operator.itemgetter(1),reverse=True)
           # print(result[0])
    with open("error_message.csv","w") as error_csv:
        writer = csv.writer(error_csv)
        writer.writerow(["Error","Count"])
        for row in count1:
            writer.writerow(row)


        #print(result)
              # if result:
               #    if result not in count:
                #       count[result] = 0
                 #  count[result] += 1

                  # return count

    f.close()
print(extract_log(logfile))
#!/usr/bin/env python3.7
import re
import csv
import sys
import operator


user_gap = {}
logfile = sys.argv[1]
def user_list(logfile):
    with open(logfile) as f:
        line = f.readlines()
        for log in line:
            error_pattern = re.compile(r"(?<=\()(.*)(?=\))")
            result = error_pattern.search(log)
            if result:
                userlist = user_gap.get(result[0])
                if "INFO" in log:
                    if not userlist:
                        user_gap[result[0]] = [1,0]
                    else:
                        user_gap[result[0]] = [userlist[0] + 1,userlist[1]]
                elif "ERROR" in log:
                    if not userlist:
                        user_gap[result[0]] = [0,1]
                    else:
                        user_gap[result[0]] = [userlist[0],userlist[1]+1]








    print(user_gap)
    f.close()
    user_gap1 = sorted(user_gap.items(), key=lambda x: x[1], reverse=True)
    user_sda = sorted(user_gap.keys())
    user_info = []
    for k in user_sda:
        v = user_gap.get(k)

        user_info.append("{},{},{}".format(k,v[0],v[1]))
    print("Hi Test")
    print(user_info.sort())
    with open("user_statistics.csv" ,"w") as user_csv:
        writer1 = csv.writer(user_csv)
        writer1.writerow(["Username","INFO","ERROR"])
        #for row in user_info:
           # print(row.replace("[","")
        writer = csv.writer(user_csv,delimiter='\n')
        writer.writerow(user_info)

print(user_list(logfile))
