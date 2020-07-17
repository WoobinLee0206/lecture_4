class Vector4D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mod(self, other):
        return Vector4D(self.x % other.x, self.y % other.y)

    def __mod__(self, other):
        return Vector4D(self.x % other.x, self.y % other.y)
    

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    
v1 = Vector4D(10, 20)
v2 = Vector4D(30, 40)
v3 = v1.mod(v2)
v4 = v1 % v2
print(v3)
print(v4)