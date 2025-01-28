import numpy.matlib as np
import matplotlib.pyplot as plt
import csv

from robotMovement import RobotSimulation as Robot
from fuzzyObjectAvoidance import fuzzyObjectAvoidance

#   1 = show trail  0 = disable
SHOWTRAIL = 1

#   1 = CSV output enable 0 = disable
OUTPUTEN = 1
csvOutput = [["Robot Row", "Robot Column", "Left Sensor Dist", "Right Sensor Dist", "Robot Theta", "Turn Angle"]]
csvFilePath = "FuzzyRobotPython/RobotOutput.csv"

#   declaring grid
gridPathfinding = np.zeros((1000, 1000))

#   adds a border to the grid
gridPathfinding[5, :] = 255
gridPathfinding[995, :] = 255
gridPathfinding[:, 5] = 255
gridPathfinding[:, 995] = 255

#   adds a wall as an obstacle for the robot
gridPathfinding[570:572, 250:750] = 255

#   robot declaration
roomba = Robot(robotRow = 700, robotColumn = 700, robotTheta = 145.0, speed = 2)
gridPathfinding[roomba.robotRow - 3 : roomba.robotRow + 3, 
                roomba.robotColumn - 3 : roomba.robotColumn + 3] = 254

#   grid setup
plt.figure(figsize=(10, 10))
plot = plt.imshow(gridPathfinding, cmap = "gray")

while True:
# for i in range(10):
    if SHOWTRAIL == 0:
        gridPathfinding[round(roomba.robotRow - 3.0) : round(roomba.robotRow + 3.0), 
                        round(roomba.robotColumn - 3.0) : round(roomba.robotColumn + 3.0)] = 0

    roomba.moveRobot()

    leftSensorDistance = roomba.getDist(gridPathfinding, 35)
    rightSensorDistance = roomba.getDist(gridPathfinding, -30)
    # if leftSensorDistance == 100 | leftSensorDistance == -1:
    #     leftSensorDistance = 100
    # if rightSensorDistance == 100 | rightSensorDistance == -1:
    #     rightSensorDistance = 100

    gridPathfinding[round(roomba.robotRow - 3.0) : round(roomba.robotRow + 3.0), 
                    round(roomba.robotColumn - 3.0) : round(roomba.robotColumn + 3.0)] = 254

    turn = fuzzyObjectAvoidance(leftSensorDistance, rightSensorDistance)
    # roomba.robotTheta += turn

    #   CSV file output
    if OUTPUTEN == 1:
        csvOutput.append([roomba.robotRow, roomba.robotColumn, 
                        leftSensorDistance, rightSensorDistance, 
                        roomba.robotTheta, turn])
    try:
        with open(file = csvFilePath, mode = "w", newline = "") as file:
            writer = csv.writer(file)
            for row in csvOutput:
                writer.writerow(row)
    except PermissionError:
        print("Writing failed, permission denied")


    #   grid
    plot.set_data(gridPathfinding)
    plt.draw()
    plt.pause(0.01)  # Pause to allow for real-time updates