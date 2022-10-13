from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for x in range (10):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == "red":
        for x in range(10):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(10):
            robotArm.moveLeft()

    else:
        robotArm.drop()
        robotArm.moveRight()
        for x in range (1):
            robotArm.grab()
            robotArm.scan()
            if robotArm.scan() == "red":
                for x in range(10):
                    robotArm.moveRight()
                robotArm.drop()
                for x in range(10):
                    robotArm.moveLeft()
            else:
                robotArm.drop()
                robotArm.moveRight()
                for x in range (1):
                    robotArm.grab()
                    robotArm.scan()
                    if robotArm.scan() == "red":
                        for x in range(10):
                            robotArm.moveRight()
                        robotArm.drop()
                        for x in range(10):
                            robotArm.moveLeft()
            
            






# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()