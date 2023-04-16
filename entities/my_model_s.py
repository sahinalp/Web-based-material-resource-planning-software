from entities.stock import Stock

class My_model_s:
    def __init__(self,count=1):
        self.wheel_quantity=4*count
        self.steering_wheel_quantity=1*count
        self.seat_quantity=4*count
        
        self.right_mirror_quantity=1*count
        self.left_mirror_quantity=1*count
        self.mid_mirror_quantity=1*count

        self.left_mirror_glass=100
        self.right_mirror_glass=100
        self.mid_mirror_glass=200

        self.left_mirror_holder=1
        self.right_mirror_holder=1
        self.mid_mirror_holder=1

        self.left_mirror_holder_polymer=1.5
        self.right_mirror_holder_polymer=1.5
        self.mid_mirror_holder_polymer=2.0
    
    def getLeftGlass(self,left_mirror_quantity=None):
        if left_mirror_quantity==None:
            left_mirror_quantity=self.left_mirror_quantity

        return (left_mirror_quantity*self.left_mirror_glass)
    def getRightGlass(self,right_mirror_quantity=None):
        if right_mirror_quantity==None:
            right_mirror_quantity=self.right_mirror_quantity
        
        return (right_mirror_quantity*self.right_mirror_glass)
    def getMidGlass(self,mid_mirror_quantity=None):
        if mid_mirror_quantity==None:
            mid_mirror_quantity=self.mid_mirror_quantity
        
        return (mid_mirror_quantity*self.mid_mirror_glass)
    def getTotalGlass(self):
        return self.getLeftGlass()+self.getRightGlass()+self.getMidGlass()
    
    def getLeftMirrorHolderPolymer(self,left_mirror_quantity=None,left_mirror_holder=None):
        if left_mirror_quantity==None:
            left_mirror_quantity=self.left_mirror_quantity
        if left_mirror_holder==None:
            left_mirror_holder=self.left_mirror_holder
        return left_mirror_quantity*left_mirror_holder*self.left_mirror_holder_polymer
    
    def getRightMirrorHolderPolymer(self,right_mirror_quantity=None,right_mirror_holder=None):
        if right_mirror_quantity==None:
            right_mirror_quantity=self.right_mirror_quantity
        if right_mirror_holder==None:
            right_mirror_holder=self.right_mirror_holder
        return right_mirror_quantity*right_mirror_holder*self.right_mirror_holder_polymer

    def getMidMirrorHolderPolymer(self,mid_mirror_quantity=None,mid_mirror_holder=None):
        if mid_mirror_quantity==None:
            mid_mirror_quantity=self.mid_mirror_quantity
        if mid_mirror_holder==None:
            mid_mirror_holder=self.mid_mirror_holder
        return mid_mirror_quantity*mid_mirror_holder*self.mid_mirror_holder_polymer
    
    def getTotalPolymer(self):
        return self.getLeftMirrorHolderPolymer()+self.getRightMirrorHolderPolymer()+self.getMidMirrorHolderPolymer()
    
    def getCode(self):
        return "model_s"
    
    def getProductCode(self):
        return "my_model_s"

    def getUnit(self,value=""):
        if value=="glass":
            return "cm2"
        elif value=="polymer":
            return "kg"
        else:
            return "pieces"