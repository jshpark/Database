import random

MajorDict={
    "Accounting" : "The George L. Argyros School of Business and Economics",
    "Business Administration" : "The George L. Argyros School of Business and Economics",
    "Economics" : "The George L. Argyros School of Business and Economics",
    "Integrated Educational Studies" : "Donna Ford Attallah College of Educational Studies",
    "Applied Human Physiology" : "Crean College of Health and Behavioral Sciences",
    "Health Sciences" : "Crean College of Health and Behavioral Sciences",
    "Psychology" : "Crean College of Health and Behavioral Sciences",
    "Film Studies" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Public Relations and Advertising" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Animation and Visual Studios" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Broadcast Journalism and Documentary" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Creative Producing" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Film Production" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Screen Acting" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Screenwriting" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Television Writing and Production" : "Lawrence and Kristina Dodge College of Film and Media Arts",
    "Biochemistry and Molecular Biology" : "Schmid College of Science and Technology",
    "Biological Sciences" : "Schmid College of Science and Technology",
    "Chemistry" : "Schmid College of Science and Technology",
    "Computer Science" : "Schmid College of Science and Technology",
    "Data Analytics" : "Schmid College of Science and Technology",
    "Environmental Science and Policy" : "Schmid College of Science and Technology",
    "Mathematics" : "Schmid College of Science and Technology",
    "Physics" : "Schmid College of Science and Technology",
    "Software Engineering" : "Schmid College of Science and Technology",
    "Art History" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Art" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Graphic Design" : "Wilkinson College of Arts Humanities and Social Sciences",
    "English" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Creative Writing" : "Wilkinson College of Arts Humanities and Social Sciences",
    "History" : "Wilkinson College of Arts Humanities and Social Sciences",
    "French" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Spanish" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Peace Studies" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Philosophy" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Political Science" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Religious Studies" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Sociology" : "Wilkinson College of Arts Humanities and Social Sciences",
    "Communication Studies" : "School of Communication",
    "Strategic and Corporate Communication" : "School of Communication",
    "Dance" : "College of Performing Arts",
    "Dance Performance" : "College of Performing Arts",
    "Music" : "College of Performing Arts",
    "Theatre" : "College of Performing Arts",
    "Theatre Performance" : "College of Performing Arts",
    "Pharmacy" : "School of Pharmacy"
}

MajorIdDict={
    "Accounting" : 1,
    "Business Administration" : 2,
    "Economics" : 3,
    "Integrated Educational Studies" : 4,
    "Applied Human Physiology" : 5,
    "Health Sciences" : 6,
    "Psychology" : 7,
    "Film Studies" : 8,
    "Public Relations and Advertising" : 9,
    "Animation and Visual Studios" : 10,
    "Broadcast Journalism and Documentary" : 11,
    "Creative Producing" : 12,
    "Film Production" : 13,
    "Screen Acting" : 14,
    "Screenwriting" : 15,
    "Television Writing and Production" : 16,
    "Biochemistry and Molecular Biology" : 17,
    "Biological Sciences" : 18,
    "Chemistry" : 19,
    "Computer Science" : 20,
    "Data Analytics" : 21,
    "Environmental Science and Policy" : 22,
    "Mathematics" : 23,
    "Physics" : 24,
    "Software Engineering" : 25,
    "Art History" : 26,
    "Art" : 27,
    "Graphic Design" : 28,
    "English" : 29,
    "Creative Writing" : 30,
    "History" : 31,
    "French" : 32,
    "Spanish" : 33,
    "Peace Studies" : 34,
    "Philosophy" : 35,
    "Political Science" : 36,
    "Religious Studies" : 37,
    "Sociology" : 38,
    "Communication Studies" : 39,
    "Strategic and Corporate Communication" : 40,
    "Dance" : 41,
    "Dance Performance" : 42,
    "Music" : 43,
    "Theatre" : 44,
    "Theatre Performance" : 45,
    "Pharmacy" : 46
}

CollegeIdDict={
    "The George L. Argyros School of Business and Economics" : 1,
    "Donna Ford Attallah College of Educational Studies" : 2,
    "Crean College of Health and Behavioral Sciences" : 3,
    "Lawrence and Kristina Dodge College of Film and Media Arts" : 4,
    "Schmid College of Science and Technology" : 5,
    "Wilkinson College of Arts Humanities and Social Sciences" : 6,
    "School of Communication" : 7,
    "College of Performing Arts" : 8,
    "School of Pharmacy" : 9
}


majorInt = 1

def randomStats():
    major = random.choice(list(MajorDict.keys()))
    college = MajorDict.get(major, "")
    major_id = MajorIdDict.get(major, "")
    college_id = CollegeIdDict.get(college, "")

    #if key_string not in MajorIdDict: FIND A WAY TO RETURN MAJOR ID AND COLLEGE ID
    return major, college, major_id, college_id