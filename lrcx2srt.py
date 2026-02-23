ori=[]
tr=[]
stamp=[]
tryes=False
path=input("输入路径：")
if path[0]=="'":
    path=path[1:-1]
with open(path, "r") as file:
    flag = False
    for line in file:
        if line[0:4] == '[00:':
            flag = True
        if '[tt]' in line or "\n" == line[11:]:
            continue
        if '[tr:zh-Hans]' in line:
            if "\n" in line:
                tr.append(line[23:-1])
            else :
                tr.append(line[23:])
            tryes=True
            continue
        if flag == True:
            stamp.append(line[0:11])
            ori.append(line[11:-1])
with open('/Users/andyw/Desktop/result.srt', "w") as file:
    for i in range(len(ori)):
        file.write(str(i+1))
        file.write("\n")
        if i == len(ori) - 1:
            x=str(int(stamp[i][4:6])+5)
            if len(x)==1:
                x="0"+x
            file.write("01:" + stamp[i][1:6] + "," + stamp[i][7:-1] + " --> " + "01:" + stamp[i][1:4]+x+ "," + stamp[i][7:-1])
        else:
            file.write("01:" + stamp[i][1:6] + "," + stamp[i][7:-1] + " --> " + "01:" + stamp[i + 1][1:6] + "," + stamp[i + 1][7:-1])
        file.write("\n")
        file.write("<b>"+ori[i]+"</b>")
        if tryes:
            if i-(len(ori)-len(tr))>=0:
                file.write("\n")
                file.write("<b>" + tr[i-(len(ori)-len(tr))] + "</b>")
        file.write("\n")
        file.write("\n")