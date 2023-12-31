#Challenge 1: Square Numbers and Return Their Sum

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

point_instance = Point(1, 3, 5)
result = point_instance.sqSum()
print(result)  
