import machine
import time

while True:  #Loop forever

    joyStick_X = machine.ADC(machine.Pin(26)) #Set up joystick X & Y
    joyStick_Y= machine.ADC(machine.Pin(27))
    
    servo1 = machine.PWM(machine.Pin(16)) #Set up servos
    servo2 = machine.PWM(machine.Pin(15))
    
    servo1.freq(50) #Change servo freq
    servo2.freq(50)
    
    switch = machine.Pin(0, machine.Pin.IN) #Set up joystick button
    
    Led = machine.Pin("LED", machine.Pin.OUT) #Set up LED
    

    valueX = joyStick_X.read_u16() #Get joystick resistence value
    valueY = joyStick_Y.read_u16()
    
    
    if valueX > 45000:  #If joystick location is right
        servo1.duty_ns(1420000) #Servo move
        print("right")
    elif valueX < 15000:  #If joystick location is left
        servo1.duty_ns(1580000) #Servo move
        print("not right")
    else:
        servo1.duty_ns(0) #Servo no move
        servo1.deinit()
        
        
    if valueY > 45000:  #If joystick location is up
        servo2.duty_ns(1420000) #Servo move
        print("up")
    elif valueY < 15000:  #If joystick location is down
        servo2.duty_ns(1580000) #Servo move
        print("not up")
    else:
        servo2.duty_ns(0) #Servo no move
        servo2.deinit()
        
    if switch.value() == 1:  #Make LED go on with switch
        Led.value(1)
    else: #Make LED go off without switch
        Led.value(0)
        
        
        
        
    
    time.sleep(0.1) #little wait
