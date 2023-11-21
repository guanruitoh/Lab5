from threading import Thread
from hal import hal_adc as adc
from hal import hal_servo as servo
def s():
    while (True):
        angle = adc.get_adc_value(1) * 180/1023
        servo.set_servo_position(angle)
        

def main(): 
    adc.init()
    servo.init()
    x = Thread(target = s)
    x.start()


if __name__ == "__main__":
    main()