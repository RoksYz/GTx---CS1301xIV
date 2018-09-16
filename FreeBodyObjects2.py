from math import atan2, degrees, radians, sin, cos,sqrt
class Force:
    def __init__(self,magnitude,angle):
        self.magnitude =  magnitude
        self.angle = radians(angle)
    def get_horizontal(self):
        horizontal = self.magnitude *cos(self.angle)
        return round(horizontal,3)
    def get_vertical(self):
        vertical = self.magnitude *sin(self.angle)
        return vertical
    def get_angle(self,use_degrees=True):
        if use_degrees==True:
            d = degrees(self.angle)
            return round(d,3)
        else:
             return self.angle

def find_net_force(listforce):
    HC = 0
    VC = 0
    for s in listforce:
        s0 = s.magnitude
        s1 = s.angle

        HC +=s0*cos(s1)
        VC +=s0*sin(s1)
    ResultMagnitude = sqrt(HC**2 + VC**2)
    magnitude =round(ResultMagnitude, 1)
    
    ResultAngle = atan2(VC,HC)
    angle = degrees(ResultAngle)

    return Force(magnitude,angle)

#error-free and print:
#103.1
#-14.036

force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(net_force.get_angle())
