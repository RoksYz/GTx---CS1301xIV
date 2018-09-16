from math import sin, cos, atan2, radians, degrees, sqrt

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

#print (with room for rounding errors):
#Magnitude: 500
#Horizontal: 250.0
#Vertical: 433.0127018922193
#Angle in Degrees: 60.0
#Angle in Radians: 1.0471975511965976
a_force = Force(500, 60)
print("Magnitude:", a_force.magnitude)
print("Horizontal:", a_force.get_horizontal())
print("Vertical:", a_force.get_vertical())
print("Angle in Degrees:", a_force.get_angle())
print("Angle in Radians:", a_force.get_angle(use_degrees = False))
