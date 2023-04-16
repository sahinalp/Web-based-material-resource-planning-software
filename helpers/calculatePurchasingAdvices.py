from entities.my_model_s import My_model_s
from entities.my_semi import My_semi
from entities.stock import Stock
from entities.purchasingAdvices import PurchasingAdvices

class CalculatePurchasingAdvices:
    def __init__(self,code,count,stock,purchasing_advices):
        self.count=count
        self.stock=stock
        self.purchasing_advices=purchasing_advices
        if code==My_model_s().getCode():
            self.model=My_model_s(count=count)
        else:
            self.model=My_semi(count=count)

    def getData(self):
        data=[]
        for value in dir(self.purchasing_advices):
            if value[0]=="_":
                continue
            else:
                temp=[]
                temp.append(value)
                temp.append(getattr(self.purchasing_advices, value))
                temp.append(self.model.getUnit(value))
                data.append(temp)
        
        return data
    
    def calculateWheelQuantity(self):
        wheel_quantity=self.stock.wheel-self.model.wheel_quantity
        if wheel_quantity<=0:
            self.stock.wheel=0.0
            self.purchasing_advices.wheel=-wheel_quantity+self.purchasing_advices.wheel
        else:
            self.stock.wheel=wheel_quantity

    def calculateSteeringWheelQuantity(self):
        steering_wheel_quantity=self.stock.steering_wheel-self.model.steering_wheel_quantity
        if steering_wheel_quantity<=0:
            self.stock.steering_wheel=0.0
            self.purchasing_advices.steering_wheel=-steering_wheel_quantity+self.purchasing_advices.steering_wheel
        else:
            self.stock.wheel=steering_wheel_quantity
    
    def calculateSeatQuantity(self):
        seat_quantity=self.stock.seat-self.model.seat_quantity
        if seat_quantity<=0:
            self.stock.seat=0.0
            self.purchasing_advices.seat=-seat_quantity+self.purchasing_advices.seat
        else:
            self.stock.seat=seat_quantity
    
    def calculateMirrorQuantity(self):
        total_polymer=0.0
        if self.model.getCode()==My_model_s().getCode():
            left_mirror=self.stock.left_mirror-self.model.left_mirror_quantity
            if left_mirror<=0:
                glass=self.stock.glass-self.model.getLeftGlass(-left_mirror)
                if glass<=0:
                    self.stock.glass=0.0
                    self.purchasing_advices.glass=-glass+self.purchasing_advices.glass
                else:
                    self.stock.glass=glass

                self.stock.left_mirror=0.0
                left_mirror_holder=self.stock.left_mirror_holder-self.model.left_mirror_holder
                if left_mirror_holder<=0:
                    self.left_mirror_holder=0
                    total_polymer+=self.model.getLeftMirrorHolderPolymer(left_mirror_quantity=-left_mirror,left_mirror_holder=-left_mirror_holder)
                else:
                    self.stock.left_mirror_holder=left_mirror_holder
            else:
                self.stock.left_mirror=left_mirror

            right_mirror=self.stock.right_mirror-self.model.right_mirror_quantity
            if right_mirror<=0:

                glass=self.stock.glass-self.model.getRightGlass(-right_mirror)
                if glass<=0:
                    self.stock.glass=0.0
                    self.purchasing_advices.glass=-glass+self.purchasing_advices.glass
                else:
                    self.stock.glass=glass

                self.stock.right_mirror=0.0
                right_mirror_holder=self.stock.right_mirror_holder-self.model.right_mirror_holder
                if right_mirror_holder<=0:
                    self.right_mirror_holder=0
                    total_polymer+=self.model.getRightMirrorHolderPolymer(right_mirror_quantity=-right_mirror,right_mirror_holder=-right_mirror_holder)
                else:
                    self.stock.right_mirror_holder=right_mirror_holder
            else:
                self.stock.right_mirror=right_mirror
            
            mid_mirror=self.stock.mid_mirror-self.model.mid_mirror_quantity
            if mid_mirror<=0:

                glass=self.stock.glass-self.model.getMidGlass(-mid_mirror)
                if glass<=0:
                    self.stock.glass=0.0
                    self.purchasing_advices.glass=-glass+self.purchasing_advices.glass
                else:
                    self.stock.glass=glass

                self.stock.mid_mirror=0.0
                mid_mirror_holder=self.stock.mid_mirror_holder-self.model.mid_mirror_holder
                if mid_mirror_holder<=0:
                    self.mid_mirror_holder=0
                    total_polymer+=self.model.getMidMirrorHolderPolymer(mid_mirror_quantity=-mid_mirror,mid_mirror_holder=-mid_mirror_holder)
                else:
                    self.stock.mid_mirror_holder=mid_mirror_holder
            else:
                self.stock.mid_mirror=mid_mirror

            self.purchasing_advices.polymer+=total_polymer
        else:
            big_left_mirror=self.stock.big_left_mirror-self.model.big_left_mirror_quantity
            if big_left_mirror<=0:

                glass=self.stock.glass-self.model.getLeftGlass(-big_left_mirror)
                if glass<=0:
                    self.stock.glass=0.0
                    self.purchasing_advices.glass=-glass+self.purchasing_advices.glass
                else:
                    self.stock.glass=glass

                camera=self.stock.camera-self.model.getLeftCamera(-big_left_mirror)
                if camera<=0:
                    self.stock.camera=0.0
                    self.purchasing_advices.camera=-camera+self.purchasing_advices.camera
                else:
                    self.stock.camera=camera

                self.stock.big_left_mirror=0.0
                big_left_mirror_holder=self.stock.big_left_mirror_holder-self.model.big_left_mirror_holder
                if big_left_mirror_holder<=0:
                    self.big_left_mirror_holder=0
                    total_polymer+=self.model.getBigLeftMirrorHolderPolymer(big_left_mirror_quantity=-big_left_mirror,big_left_mirror_holder=-big_left_mirror_holder)
                else:
                    self.stock.big_left_mirror_holder=big_left_mirror_holder
            else:
                self.stock.big_left_mirror=big_left_mirror

            big_right_mirror=self.stock.big_right_mirror-self.model.big_right_mirror_quantity
            if big_right_mirror<=0:

                glass=self.stock.glass-self.model.getRightGlass(-big_right_mirror)
                if glass<=0:
                    self.stock.glass=0.0
                    self.purchasing_advices.glass=-glass+self.purchasing_advices.glass
                else:
                    self.stock.glass=glass

                camera=self.stock.camera-self.model.getRightCamera(-big_right_mirror)
                if camera<=0:
                    self.stock.camera=0.0
                    self.purchasing_advices.camera=-camera+self.purchasing_advices.camera
                else:
                    self.stock.camera=camera

                self.stock.big_right_mirror=0.0
                big_right_mirror_holder=self.stock.big_right_mirror_holder-self.model.big_right_mirror_holder
                if big_right_mirror_holder<=0:
                    self.big_right_mirror_holder=0
                    total_polymer+=self.model.getBigRightMirrorHolderPolymer(big_right_mirror_quantity=-big_right_mirror,big_right_mirror_holder=-big_right_mirror_holder)
                else:
                    self.stock.big_right_mirror_holder=big_right_mirror_holder
            else:
                self.stock.big_right_mirror=big_right_mirror
            self.purchasing_advices.polymer+=total_polymer

    def calculateLcdMonitor(self):
        if self.model.getCode()==My_semi().getCode():
            lcd_monitor_quantity=self.stock.lcd_monitor-self.model.lcd_monitor_quantity
            if lcd_monitor_quantity<=0:
                self.stock.lcd_monitor=0.0
                self.purchasing_advices.lcd_monitor=-lcd_monitor_quantity+self.purchasing_advices.lcd_monitor
            else:
                self.stock.lcd_monitor=lcd_monitor_quantity