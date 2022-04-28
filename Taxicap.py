#Author: Faith Elledge
#GRithub user: Elledgef
#Date: 4/27
#Description: Private data members that hold y coordinates, x coordinates and odometer reading

class taxticab:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.ometer = 0

    def movex(self, value):
        self.xcoord += value
        self.ometer += abs(value)

    def movey(self, value):
        self.ycoord += value
        self.ometer += abs(value)

    def forxcoord(self):
        return self.xcoord

    def forycoord(self):
        return self.ycoord

    def forometer(self):
        return self.ometer
