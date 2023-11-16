#Fname: Ibrahin                         #Student ID: 2242810
# opened and getting readdy to write
Roster = open('FullRoster.csv', mode="w")
Scholarship = open("ScholarshipCandidates-1.csv", mode= "w")
Disciplined = open("DisciplinedStudents-1.csv",mode= "w")
mj_list = "StudentsMajorsList-3.csv"
GPA = "GPAList-1.csv"
grad_date = "GraduationDatesList-1.csv"
# opened the other files and split them into a list
with open(mj_list) as info1:
    dataA = info1.read().splitlines()
with open(GPA) as info2:
    dataB = info2.read().splitlines()
with open(grad_date) as info3:
    dataC = info3.read().splitlines()
# splits the data, makes it look more organized
for i, j, k in zip(dataA, dataB, dataC):
    x = i.split(",")
    y = j.split(",")
    z = k.split(",")
    Roster.write(x[0] + ", " + x[2] + ", " + y[-1] + ", " +
    x[1] + ", " + z[-1] + ", " + x[4])
    Roster.write("\n")
for i, j, k in zip(dataA, dataB, dataC):
    x = i.split(",")
    y = j.split(",")
    z = k.split(",")
    mj_list.replace(" ","")
    lists = open(mj_list+"ComputerInformationSystemsStudents.csv", mode= "w")
    lists.write(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + z[-1] + ", " + x[4] + ", ")
    lists.write("\n")

for i, j, k in zip(dataA, dataB, dataC):
    x = i.split(",")
    y = j.split(",")
    z = k.split(",")
    mj_list.replace(" ", "")
    lists = open(mj_list +"ComputerScience.csv", mode="w")
    lists.write(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + z[-1] + ", " + x[4])
    lists.write("\n")
lists.close()

for i, j, k in zip(dataA, dataB, dataC):
    x = i.split(",")
    y = j.split(",")
    z = k.split(",")
    mj_list.replace("", "")
    lists = open(mj_list + "Physics.csv", mode="w")
    lists.write(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + z[-1] + ", " + x[4])
    lists.write("\n")
    for i, j, k in zip(dataA, dataB, dataC):
        x = i.split(",")
        y = j.split(",")
        z = k.split(",")
        mj_list.replace(" ", "")
        lists = open(mj_list + "ElectricalEngineer.csv", mode="w")
        lists.write(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + z[-1] + ", " + x[4])
        lists.write("\n")
    lists.close()
# combines the
for i, j, k in zip(dataA, dataB, dataC):
    x = i.split(",")
    y = j.split(",")
    z = k.split(",")
    if float(y[-1]) > 3.8:
        Scholarship.write(x[0] + ", " + x[1] + ", " + x[2] + ", " +
        x[3] + ", " + y[-1])
        Scholarship.write("\n")
for i, j, k in zip(dataA, dataB, dataC):
    x = i.split(",")
    y = j.split(",")
    z = k.split(",")
    if i[-1] == "Y":
        Disciplined.write(x[0] + ", " + x[1] + ", " + x[2] + ", " +
       z[-1])
        Disciplined.write("\n")

Roster.close()
Scholarship.close()
Disciplined.close()
