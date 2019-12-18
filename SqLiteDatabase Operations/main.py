import sqlite3
from Student import Student
from Simulation import Simulation


connection = sqlite3.connect('StudentDB')
c = connection.cursor()

simulation = Simulation()

repeatCheck = True
while (repeatCheck):
    choice = simulation.startProgram()
    if (choice == 1):
        simulation.choiceOne()

    elif (choice == 2):
        simulation.choiceTwo()

    elif (choice == 3):
        simulation.choiceThree()

    elif (choice == 4):
        simulation.choiceFour()

    elif (choice == 5):
        simulation.choiceFive()

    elif (choice == 6):
        repeatCheck = simulation.choiceSix()

    else:
        print("Please input an existing option.")










