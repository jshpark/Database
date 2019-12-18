import csv
import random
import names
from MajorGenerator import randomStats
from AdvisorGenerator import randomAdvisor

with open('data.csv', 'w', newline='') as csvfile:
    for x in range(500):
        stats_Full = randomStats()
        major = stats_Full[0]
        college = stats_Full[1]  # THIS IS HOW TO GET RANDOM MAJOR AND THEIR CORRESPONDING COLLEGES
        major_id = stats_Full[2]
        college_id = stats_Full[3]

        advisor_Stats = randomAdvisor()
        advisor_name = advisor_Stats[0]               # THIS IS HOW TO GET RANDOM ADVISO
        # RS
        advisor_Id = advisor_Stats[1]

        studentName = names.get_full_name()
        studentGPA = round(random.uniform(2, 4), 2)

        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        #CSV Format
        #student_ID, student_Name, GPA, AdvisorName, Advisor_ID, Major, Major_ID, College, College_ID
        filewriter.writerow([x+1, studentName, studentGPA, advisor_name, int(advisor_Id), major, int(major_id), college, int(college_id)])

