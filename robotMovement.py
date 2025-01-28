import math
import numpy.matlib as np

#   math.cos(x) -> cos(x) x = radians
#   math.sin(x) -> sin(x) x = radians
#   math.degrees(x) -> radians -> degrees
#   math.radians(x) -> degrees -> radians

class RobotSimulation:
    def __init__(self, robotRow, robotColumn, robotTheta, speed):
        self.robotRow = robotRow
        self.robotColumn = robotColumn
        self.robotTheta = robotTheta
        self.speed = speed


    def showInfo(self):     #   prints robot details
        print(f"Column: {self.robotColumn}")
        print(f"Row: {self.robotRow}")
        print(f"Theta: {self.robotTheta}")
    
    def moveRobot(self):    #   moves robot using column, row, and theeta   
        #   calculates column and row displacement
        thetaR = math.radians(self.robotTheta)
        columnDisplacement = math.cos(thetaR)
        rowDisplacement = math.sin(thetaR)

        #   calculates new column and row
        self.robotColumn = self.robotColumn + columnDisplacement * self.speed
        self.robotRow = self.robotRow - rowDisplacement * self.speed

    def getDist(self, grid, thetaOffset):   #   calculates distance from robot to object with 100 unit range
        #   -1 = no object found
        #   1 -> 100 = object found 1 -> 100 units away
        distance = -1

        #   calculates column and row displacement ahead of bot
        thetaR = math.radians(self.robotTheta)
        thetaOffsetR = math.radians(thetaOffset)
        columnDisplacement = math.cos(thetaR + thetaOffsetR)
        rowDisplacement = math.sin(thetaR + thetaOffsetR)

        #   loops from 1 to 100, to check for 100 units ahead of robot
        for i in range(1, 100, 1):
            newColumn = round(self.robotColumn + columnDisplacement * i)
            newRow = round(self.robotRow - rowDisplacement * i)

            #   checks to ensure robot range is within the grid range
            if ((newColumn >= 0 and newRow >= 0) and (newColumn <= 999 and newRow <= 999)):
                #   true if robot detects obstacle
                if (grid[newRow, newColumn] == 255):
                    distance = math.sqrt((self.robotColumn - newColumn) ** 2 + (self.robotRow - newRow) ** 2)
        
        return distance

def main():
    #   declaring grid
    gridPathfinding = np.zeros((1000, 1000))

    #   adds a border to the grid
    gridPathfinding[5, :] = 255
    gridPathfinding[995, :] = 255
    gridPathfinding[:, 5] = 255
    gridPathfinding[:, 995] = 255

    robotTest = RobotSimulation(robotRow = 700, robotColumn = 700, robotTheta = 45, speed = 2)
    # robotTest.showInfo()
    
    print(robotTest.getDist(gridPathfinding, 0))

    # for i in range(6):
    #     robotTest.moveRobot()
    #     robotTest.showInfo()
    
if __name__ == "__main__":
    main()