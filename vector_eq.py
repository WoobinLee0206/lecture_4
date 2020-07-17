class Vector5D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def eq(self, other):
        if(self.x == other.x):
            return '{} == {}'.format(self.x, other.x)
        if(self.y == other.y):
            return '{} == {}'.format(self.y, other.y)

    def __eq__(self, other):
        if(self.x == other.x):
            return '{} == {}'.format(self.x, other.x)
        if(self.y == other.y):
            return '{} == {}'.format(self.y, other.y)
    
v1 = Vector5D(10, 20)
v2 = Vector5D(10, 20)
v3 = v1.eq(v2)
v4 = v1 == v2