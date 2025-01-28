from fuzzylogic.classes import Domain, Rule
from fuzzylogic.functions import R, S, trapezoid, triangular
import matplotlib.pyplot as plt

leftObstacleSensor = Domain("Left Distance", 0, 100, res = 0.1)
rightObstacleSensor = Domain("Right Distance", 0, 100, res = 0.1)
#   members for each fuzzy logic
leftObstacleSensor.veryStrong = S(0, 25)
leftObstacleSensor.strong = trapezoid(0, 25, 25, 50)
leftObstacleSensor.medium = trapezoid(25, 50, 50, 75)
leftObstacleSensor.weak = trapezoid(50, 75, 75, 100)
leftObstacleSensor.veryWeak = R(75, 100)

rightObstacleSensor.veryStrong = S(0, 25)
rightObstacleSensor.strong = trapezoid(0, 25, 25, 50)
rightObstacleSensor.medium = trapezoid(25, 50, 50, 75)
rightObstacleSensor.weak = trapezoid(50, 75, 75, 100)
rightObstacleSensor.veryWeak = R(75, 100)

#   turning radius
turningRadius = Domain("Theta", -50.5, 50.5, res = 0.1)
turningRadius.mediumRight = triangular(-50.5, -49.5)
turningRadius.smallRight = triangular(-25.5, -24.5)
turningRadius.noTurn = triangular(-0.5, 0.5)
turningRadius.smallLeft = triangular(24.5, 25.5)
turningRadius.mediumLeft = triangular(49.5, 50.5)

#   rules
R1 = Rule({(leftObstacleSensor.veryStrong, rightObstacleSensor.veryStrong) : turningRadius.noTurn})
R2 = Rule({(leftObstacleSensor.veryStrong, rightObstacleSensor.strong) : turningRadius.smallRight})
R3 = Rule({(leftObstacleSensor.veryStrong, rightObstacleSensor.medium) : turningRadius.smallRight})
R4 = Rule({(leftObstacleSensor.veryStrong, rightObstacleSensor.weak) : turningRadius.mediumRight})
R5 = Rule({(leftObstacleSensor.veryStrong, rightObstacleSensor.veryWeak) : turningRadius.mediumRight})
R6 = Rule({(leftObstacleSensor.strong, rightObstacleSensor.veryStrong) : turningRadius.smallLeft})
R7 = Rule({(leftObstacleSensor.strong, rightObstacleSensor.strong) : turningRadius.noTurn})
R8 = Rule({(leftObstacleSensor.strong, rightObstacleSensor.medium) : turningRadius.smallRight})
R9 = Rule({(leftObstacleSensor.strong, rightObstacleSensor.weak) : turningRadius.mediumRight})
R10 = Rule({(leftObstacleSensor.strong, rightObstacleSensor.veryWeak) : turningRadius.mediumRight})
R11 = Rule({(leftObstacleSensor.medium, rightObstacleSensor.veryStrong) : turningRadius.smallLeft})
R12 = Rule({(leftObstacleSensor.medium, rightObstacleSensor.strong) : turningRadius.smallLeft})
R13 = Rule({(leftObstacleSensor.medium, rightObstacleSensor.medium) : turningRadius.noTurn})
R14 = Rule({(leftObstacleSensor.medium, rightObstacleSensor.weak) : turningRadius.smallRight})
R15 = Rule({(leftObstacleSensor.medium, rightObstacleSensor.veryWeak) : turningRadius.smallRight})
R16 = Rule({(leftObstacleSensor.weak, rightObstacleSensor.veryStrong) : turningRadius.mediumLeft})
R17 = Rule({(leftObstacleSensor.weak, rightObstacleSensor.strong) : turningRadius.mediumLeft})
R18 = Rule({(leftObstacleSensor.weak, rightObstacleSensor.medium) : turningRadius.smallLeft})
R19 = Rule({(leftObstacleSensor.weak, rightObstacleSensor.weak) : turningRadius.noTurn})
R20 = Rule({(leftObstacleSensor.weak, rightObstacleSensor.veryWeak) : turningRadius.smallRight})
R21 = Rule({(leftObstacleSensor.veryWeak, rightObstacleSensor.veryStrong) : turningRadius.mediumLeft})
R22 = Rule({(leftObstacleSensor.veryWeak, rightObstacleSensor.strong) : turningRadius.mediumLeft})
R23 = Rule({(leftObstacleSensor.veryWeak, rightObstacleSensor.medium) : turningRadius.smallLeft})
R24 = Rule({(leftObstacleSensor.veryWeak, rightObstacleSensor.weak) : turningRadius.smallLeft})
R25 = Rule({(leftObstacleSensor.veryWeak, rightObstacleSensor.veryWeak) : turningRadius.noTurn})

rules = sum([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25])
# rules = R1 and R2 and R3 and R4 and R5 and R6 and R7 and R8 and R9 and R10 and R11 and R12 and R13 and R14 and R15 and R16 and R17 and R18 and R19 and R20 and R21 and R22 and R23 and R24 and R25

def fuzzyObjectAvoidance(leftDist, rightDist):  #   return turning angle
    values = {leftObstacleSensor : leftDist, rightObstacleSensor : rightDist}
    return(rules(values))

def main():
    # leftObstacleSensor.veryStrong.plot()
    # leftObstacleSensor.strong.plot()
    # leftObstacleSensor.medium.plot()
    # leftObstacleSensor.weak.plot()
    # leftObstacleSensor.veryWeak.plot()

    turningRadius.mediumRight.plot()
    turningRadius.smallRight.plot()
    turningRadius.noTurn.plot()
    turningRadius.smallLeft.plot()
    turningRadius.mediumLeft.plot()

    plt.show()

    print(fuzzyObjectAvoidance(100, 100))


if __name__ == "__main__":
    main()
