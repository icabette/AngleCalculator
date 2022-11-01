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