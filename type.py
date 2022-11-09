import math
import time

### CONSTANTS Definition
SS1 = 0
SS2 = 1
SS3 = 2
SS4 = 3
SS5 = 4
SS6 = 5
SS7 = 6
SS8 = 7
SS9 = 8
TAS = 9 # Total Amount of Sensors

class IMU:
    def __init__(self) -> None:
        self.__accX = 0
        self.__accY = 0
        self.__accZ = 0
        self.__gyX = 0
        self.__gyY = 0
        self.__gyZ = 0
        self.__acc = []
        self.__gy = []
        self.__accAngle = []
        self.__gyAngle = []
        self.__kalmanAngle = []
        self.__complAngle = []

    def setAccX(self, x):
        self.__accX = x
    
    def setAccY(self, y):
        self.__accY = y
    
    def setAccZ(self, z):
        self.__accZ = z
    
    def setGyX(self, x):
        self.__gyX = x
    
    def setGyY(self, y):
        self.__gyY = y
    
    def setGyZ(self, z):
        self.__gyZ = z

    def setAcc(self):
        self.__acc.append(self.__accX)
        self.__acc.append(self.__accY)
        self.__acc.append(self.__accZ)

    def getAcc(self) -> list:
        return self.__acc

    def setGy(self):
        self.__gy.append(self.__gyX)
        self.__gy.append(self.__gyY)
        self.__gy.append(self.__gyZ)

    def getGy(self) -> list:
        return self.__gy

    def getAccAngle(self) -> list:
        y_radians = math.atan2(self.__accX, math.sqrt((self.__accY*self.__accY) + (self.__accZ*self.__accZ)))
        x_radians = math.atan2(self.__accY, math.sqrt((self.__accX*self.__accX) + (self.__accZ*self.__accZ)))
        self.__accAngle.clear()
        self.__accAngle.append(math.degrees(x_radians))
        self.__accAngle.append(math.degrees(y_radians))
        return self.__accAngle
    
    def getGyAngle(self,gy, baseGy:list) -> list:
        DEGREE_PER_SECOND = 32767 / 250
        past:time = 0
        now = time.time()
        dt = now - past
        self.__gyAngle.clear()
        self.__gyAngle.append()
        return self.__gyAngle
    
    def getComplAngle(self) -> list:
        return self.__complAngle
    
    def getKalmanAngle(self) -> list:
        return self.__kalmanAngle
    

if __name__ == "__main__":
    imu = [IMU()]
    imu.append(imu[0].setAccX(5000))
    imu.append(imu[0].setAccY(4000))
    imu.append(imu[0].setAccZ(3000))
    imu.append(imu[0].setAcc())
    imu.append(imu[0].setGyX(300))
    imu.append(imu[0].setGyY(200))
    imu.append(imu[0].setGyZ(400))
    imu.append(imu[0].setGy())

    print(imu[0].getAcc(), imu[0].getGy())

    