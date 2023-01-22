class V2d:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"    


class V3d(V2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

vector2d=V2d(5,8)
vector3d=V3d(5,9,15)
print(vector2d)
print(vector3d)


