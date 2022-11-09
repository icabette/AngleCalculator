import xlsReader as xls
import type

def main() -> int:
    imu:list = [type.IMU()]
    for sc in range(1,type.TAS):
        imu.append(type.IMU())

    wb = xls.readExcel()
    ws = wb.active
    sensorCount = 0
    xyzCount = 0
    for row in ws.iter_rows(min_row=2,max_row=12,min_col=2,max_col=55, values_only=True):
        for value in row:
            if xyzCount%6 == 0:
                imu[sensorCount].setAccX(value)
            if xyzCount%6 == 1:
                imu[sensorCount].setAccY(value)
            if xyzCount%6 == 2:
                imu[sensorCount].setAccZ(value)
            if xyzCount%6 == 3:
                imu[sensorCount].setGyX(value)
            if xyzCount%6 == 4:
                imu[sensorCount].setGyY(value)
            if xyzCount%6 == 5:
                imu[sensorCount].setGyZ(value)
            xyzCount += 1
            if ( xyzCount > 0 and (xyzCount%6 == 0)):
                sensorCount += 1
            if ( sensorCount == type.TAS):
                for i in range (0,type.TAS):
                    print(i," : ",imu[i].getAccAngle())
                sensorCount = 0

    return 0

if __name__ == "__main__":
    main()