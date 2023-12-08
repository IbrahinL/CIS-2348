#Fname: Ibrahin                         #Student ID: 2242810
# opened and getting ready to write
import csv

#The readFiles function reads all the functions in one
def readFiles():
    with open('StudentsMajorsList-3 (1).csv', 'r') as csv1:
        Studentsmajorlist = []
        reader = csv.reader(csv1)
        for info in reader:
            if len(info) < 5:
                info.append("A")
                Studentsmajorlist.append(info)
            else:
                Studentsmajorlist.append(info)

    with open('GPAList-1 (2).csv', 'r') as csv2:
        GPAlist = []
        reader = csv.reader(csv2)
        for info in reader:
            GPAlist.append(info)
    with open('GraduationDatesList-1 (2).csv', 'r') as csv3:
        GradDatelist = []
        reader = csv.reader(csv3)
        for info in reader:
            GradDatelist.append(info)
#I will put all the majors in a list
    student_majors = []
    for smjData in Studentsmajorlist:
        smjData[3].lower()
        if smjData[3] != student_majors:
            student_majors.append(smjData[3].lower())
#will put all the ID in a list
# this for loop will look over GPA with studentID and update the similarities
        studentID = smjData[0]
        for grade in GPAlist:
            stuID = grade[0]
            if stuID == studentID:
                GPA = grade[1]
                smjData.append(GPA)
                break
# this for loop will look over GradDateList with graduate_ID and matches
# graduate_id and studentID
        for graduate in GradDatelist:
            graduate_id = grade[0]
            if graduate_id == studentID:
                break
    return Studentsmajorlist, student_majors

# this function receives the major and overlooks if it's correct with any of the available major
def validateMajor(major, students_major):
    if major in students_major:
        return major
    else:
# this else statement will join all the majors in one string
        majors_str = "".join(students_major)
        majors_str1 = majors_str.split()
        combine_majors = "".join(majors_str1)
        classify_major = major.split()
        derived_major = ""
# in this for loop it checks all the newly imputed words are in the joined major
#
        for information in classify_major:
            if information in combine_majors:
                derived_major += " " + information
        new_major = derived_major.strip()
        if new_major in students_major:
            return new_major
        else:
            return "invalid"
# this main function will return the actual function to perform
# the question of the project
def main():
    Studentsmajorlist, student_majors = readFiles()
    while True:
        input_data = input("Please enter the students major and GPA: ").lower()
        list = input_data.split()
        major = ""
        GPA = ""
        for data in list:
            # during my research for this project I learned that
            # isalpha will separate major and GPA by only reading letters
            if data.isalpha():
                major += " " + data
            else:
                GPA += data
        clean_major = major.strip()

        try:
            Student_GPA = float(GPA)
        except ValueError:
            # if input there is an incorrect input,then the response will be
            # "No such student"
            print("No such student")
            continue
        # calls the function
        major = validateMajor(clean_major, student_majors)
        if major == "invalid":
            # if there is an incorrect input the response will be "No such student"
            print("No such student")
            continue

        answer = []
        final_ans = []
        #loop around students and find tose doing the inputed and validated major
        for info in Studentsmajorlist:
            student_major = info[3].lower()
            GPA = float(info[5])
            graduation = info[-1]
            disciplinary = info[4]
            #will not provide students with disciplinary record and who have already graduated
            if major == student_major and disciplinary != "Y" and "#" not in graduation:
                min1 = Student_GPA - 0.1
                max1 = Student_GPA + 0.1
                # to be in a range of 0.1
                if  GPA >= min1 and GPA <= max1 :
                    answer.append(info)
                # in the you may also consider:, the range is from 2.5
                else:
                    min1 = Student_GPA - 0.25
                    max1 = Student_GPA + 0.25
                    min2 = Student_GPA - 0.1#excludes students in the second query capability.
                    max2 = Student_GPA + 0.1# because it would be repetitive

                    if GPA >= min1 and GPA <= max1 :
                        if not GPA >= min2 and not GPA <= max2:
                            final_ans.append(info)
                            print(f"{info[0]} {info[1]} {info[2]} {info[5]}")

        if len(final_ans) == 0 and len(answer) == 0:#if two above scernarios have no student
            #this loop gets the closest student based on GPA if availbale
            students = []
            ranges = []
            for student in Studentsmajorlist:
                student_major = student[3].lower()
                GPA = float(student[5])
                graduation = student[-1]
                print(graduation)
                disciplinary = student[4]

                if major == student_major and disciplinary != "Y" and "#" not in graduation:
                    students.append(student)
                    # this formula is used to find the difference in between ranges
                    range = abs(GPA - Student_GPA)
                    ranges.append(range)
            if len(students) > 0:
                counter = 0
                min = 100
                # finds minimum range then returns student
                for data in ranges:
                    if data < min:
                        min = data
                    counter += 1

                index = ranges.index(min)
                closest_student = students[index]
                # if the input is too far away from the range, it will input the closest
                print("\nClosest Student: ")
                print(f"{closest_student[0]} {closest_student[1]} {closest_student[2]} {closest_student[5]}")
            else:
                print("\nNo such student")
        else:
            print("\nYour students(s): ")
            for data in answer:
                print(f"{data[0]} {data[1]} {data[2]} {data[5]}")

            if len(final_ans) > 0:
                print("\nYou may also consider: ")
                for data in final_ans:
                    print(f"{data[0]} {data[1]} {data[2]} {data[5]}")

        quit = input("would you like to start another query: Press the Enter key to continue or q to quit:")
        if quit.lower() == "q":
            exit()
        else:
            continue
main()