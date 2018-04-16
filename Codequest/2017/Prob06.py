import operator

# Import file
filename = 'Prob06.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        schoolName = file.readline().strip()

        students = int(file.readline().strip())

        studentDict = {}

        while students > 0:

            studentInfo = file.readline().strip().split(':')
            studentName = studentInfo[0]
            studentsGrades = studentInfo[1].split(',')

            totalGradePoints = 0
            totalCreditHours = 0

            for grade in studentsGrades:
                letterGrade = 0

                if grade[0] == 'A':
                    letterGrade = 4
                elif grade[0] == 'B':
                    letterGrade = 3
                elif grade[0] == 'C':
                    letterGrade = 2
                elif grade[0] == 'D':
                    letterGrade = 1

                creditHours = int(grade[1])
                totalCreditHours += creditHours

                gradePoints = letterGrade * creditHours
                totalGradePoints += gradePoints

            totalGPA = totalGradePoints / totalCreditHours

            studentDict[studentName] = [totalGPA, totalCreditHours]

            students -= 1

        valedictorian = sorted(studentDict.items(), key=lambda x: x[1], reverse=True)[0]

        print('%s = %s' % (schoolName, valedictorian[0]))

        test_cases -= 1