class My_semi:
    def __init__(self,count=1):
        self.wheel_quantity=8*count
        self.steering_wheel_quantity=1*count
        self.seat_quantity=1*count

        self.big_right_mirror_quantity=1*count
        self.big_left_mirror_quantity=1*count
        self.lcd_monitor_quantity=2*count

        self.big_left_mirror_glass=300
        self.big_right_mirror_glass=300

        self.big_left_mirror_holder=1
        self.big_right_mirror_holder=1

        self.big_left_mirror_camera=1
        self.big_right_mirror_camera=1
        
        self.big_left_mirror_holder_polymer=5.0
        self.big_right_mirror_holder_polymer=5.0

    def getLeftGlass(self,big_left_mirror_quantity=None):
        if big_left_mirror_quantity==None:
            big_left_mirror_quantity=self.big_left_mirror_quantity

        return (big_left_mirror_quantity*self.big_left_mirror_glass)
    def getRightGlass(self,big_right_mirror_quantity=None):
        if big_right_mirror_quantity==None:
            big_right_mirror_quantity=self.big_right_mirror_quantity
        
        return (big_right_mirror_quantity*self.big_right_mirror_glass)
    
    def getTotalGlass(self):
        return self.getRightGlass()+self.getRightGlass()

    def getLeftCamera(self,big_left_mirror_quantity=None):
        if big_left_mirror_quantity==None:
            big_left_mirror_quantity=self.big_left_mirror_quantity

        return (big_left_mirror_quantity*self.big_left_mirror_camera)
    def getRightCamera(self,big_right_mirror_quantity=None):
        if big_right_mirror_quantity==None:
            big_right_mirror_quantity=self.big_right_mirror_quantity
        
        return (big_right_mirror_quantity*self.big_right_mirror_camera)
    
    def getTotalCamera(self):
        return self.getLeftCamera()+self.getRightCamera()

    def getBigLeftMirrorHolderPolymer(self,big_left_mirror_quantity=None,big_left_mirror_holder=None):
        if big_left_mirror_quantity==None:
            big_left_mirror_quantity=self.big_left_mirror_quantity
        if big_left_mirror_holder==None:
            big_left_mirror_holder=self.big_left_mirror_holder
        return big_left_mirror_quantity*big_left_mirror_holder*self.big_left_mirror_holder_polymer

    def getBigRightMirrorHolderPolymer(self,big_right_mirror_quantity=None,big_right_mirror_holder=None):
        if big_right_mirror_quantity==None:
            big_right_mirror_quantity=self.big_right_mirror_quantity
        if big_right_mirror_holder==None:
            big_right_mirror_holder=self.big_right_mirror_holder
        return big_right_mirror_quantity*big_right_mirror_holder*self.big_right_mirror_holder_polymer

    def getTotalPolymer(self):
        return self.getBigLeftMirrorHolderPolymer()+self.getBigRightMirrorHolderPolymer()

    def getTotalCamera(self):
        return (self.big_left_mirror_quantity*self.big_left_mirror_camera)+(self.big_right_mirror_quantity*self.big_right_mirror_camera)
    
    def getCode(self):
        return "semi"
    
    def getProductCode(self):
        return "my_semi"

    def getUnit(self,value=""):
        if value=="glass":
            return "cm2"
        elif value=="polymer":
            return "kg"
        else:
            return "pieces"