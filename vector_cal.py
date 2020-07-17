class Vector5D:
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return 'Vectors are identical'
        else :
            return 'Vectors are different'
    
    def __del__(self):
        print("This Process is End!")


v1=Vector5D(1,2,3)
v2=Vector5D(1,2,4)
v3 = (v1 == v2)
print(v3)