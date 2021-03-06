from juniorcup import *

r0 = Robot(0)
r1 = Robot(1)
speed = 255
cmp0 = 0
cmp1 = 0



def motor0(ml1, ml2, mr2, mr1):
    r0.motor(ml1 + cmp0, ml2 + cmp0, mr2 + cmp0, mr1 + cmp0)


def motor1(ml1, ml2, mr2, mr1):
    r1.motor(ml1 + cmp1, ml2 + cmp1, mr2 + cmp1, mr1 + cmp1)

def move0(dir):
    if(dir == 0):      motor0(speed   , speed   , -speed  , -speed   )
    if(dir == 1):      motor0(speed   , speed/2 , -speed  , -speed/2 )
    if(dir == 2):      motor0(speed   , 0       , -speed  , 0        )
    if(dir == 3):      motor0(speed   , -speed/2, -speed  , speed/2  )
    if(dir == 4):      motor0(speed   , -speed  , -speed  , speed    )
    if(dir == 5):      motor0(speed/2 , -speed  , -speed/2, speed    )
    if(dir == 6):      motor0(0       , -speed  , 0       , speed    )
    if(dir == 7):      motor0(-speed/2, -speed  , speed/2 , speed    )    
    
    if(dir == 8):      motor0(-speed  , -speed  , speed   , speed    )
    
    if(dir == 9):      motor0(-speed   , -speed/2, speed   , speed/2 )
    if(dir == 10):     motor0(-speed   , 0       , speed   , 0       )
    if(dir == 11):     motor0(-speed   , speed/2 , speed   , -speed/2)
    if(dir == 12):     motor0(-speed   , speed   , speed   , -speed  )
    if(dir == 13):     motor0(-speed/2 , speed   , speed/2 , -speed  )
    if(dir == 14):     motor0(0        , speed   , 0       , -speed  )
    if(dir == 15):     motor0(speed/2  , speed   , -speed/2, -speed  )

def move1(dir):
    if(dir == 0):      motor1(speed   , speed   , -speed  , -speed   )
    if(dir == 1):      motor1(speed   , speed/2 , -speed  , -speed/2 )
    if(dir == 2):      motor1(speed   , 0       , -speed  , 0        )
    if(dir == 3):      motor1(speed   , -speed/2, -speed  , speed/2  )
    if(dir == 4):      motor1(speed   , -speed  , -speed  , speed    )
    if(dir == 5):      motor1(speed/2 , -speed  , -speed/2, speed    )
    if(dir == 6):      motor1(0       , -speed  , 0       , speed    )
    if(dir == 7):      motor1(-speed/2, -speed  , speed/2 , speed    )    
    
    if(dir == 8):      motor1(-speed  , -speed  , speed   , speed    )
    
    if(dir == 9):      motor1(-speed   , -speed/2, speed   , speed/2 )
    if(dir == 10):     motor1(-speed   , 0       , speed   , 0       )
    if(dir == 11):     motor1(-speed   , speed/2 , speed   , -speed/2)
    if(dir == 12):     motor1(-speed   , speed   , speed   , -speed  )
    if(dir == 13):     motor1(-speed/2 , speed   , speed/2 , -speed  )
    if(dir == 14):     motor1(0        , speed   , 0       , -speed  )
    if(dir == 15):     motor1(speed/2  , speed   , -speed/2, -speed  )

def shift0(dir):
    if(dir == 0):      motor0(speed   , speed   , -speed  , -speed   )#0

    if(dir == 1):      motor0(speed   , -speed  , -speed  , speed    )#4
    if(dir == 2):      motor0(speed/2 , -speed  , -speed/2, speed    )#5
    if(dir == 3):      motor0(0       , -speed  , 0       , speed    )#6
    if(dir == 4):      motor0(-speed/2, -speed  , speed/2 , speed    )#7
    if(dir == 5):      motor0(-speed  , -speed  , speed   , speed    )#8
    if(dir == 6):      motor0(-speed   , -speed/2, speed   , speed/2 )#9
    if(dir == 7):      motor0(-speed   , 0       , speed   , 0       )#10   
    
    if(dir == 8):      motor0(speed/2 , -speed  , -speed/2, speed    )#5
    
    if(dir == 9):      motor0(0       , -speed  , 0       , speed    )#6 
    if(dir == 10):     motor0(-speed/2, -speed  , speed/2 , speed    )#7
    if(dir == 11):     motor0(-speed  , -speed  , speed   , speed    )#8
    if(dir == 12):     motor0(-speed   , -speed/2, speed   , speed/2 )#9
    if(dir == 13):     motor0(-speed   , 0       , speed   , 0       )#10 
    if(dir == 14):     motor0(-speed   , speed/2 , speed   , -speed/2)#11
    if(dir == 15):     motor0(-speed   , speed   , speed   , -speed  )#12

def shift1(dir):
    if(dir == 0):      motor1(speed   , speed   , -speed  , -speed   )#0

    if(dir == 1):      motor1(speed   , -speed  , -speed  , speed    )#4
    if(dir == 2):      motor1(speed/2 , -speed  , -speed/2, speed    )#5
    if(dir == 3):      motor1(0       , -speed  , 0       , speed    )#6
    if(dir == 4):      motor1(-speed/2, -speed  , speed/2 , speed    )#7
    if(dir == 5):      motor1(-speed  , -speed  , speed   , speed    )#8
    if(dir == 6):      motor1(-speed   , -speed/2, speed   , speed/2 )#9
    if(dir == 7):      motor1(-speed   , 0       , speed   , 0       )#10   
    
    if(dir == 8):      motor1(speed/2 , -speed  , -speed/2, speed    )#5
    
    if(dir == 9):      motor1(0       , -speed  , 0       , speed    )#6 
    if(dir == 10):     motor1(-speed/2, -speed  , speed/2 , speed    )#7
    if(dir == 11):     motor1(-speed  , -speed  , speed   , speed    )#8
    if(dir == 12):     motor1(-speed   , -speed/2, speed   , speed/2 )#9
    if(dir == 13):     motor1(-speed   , 0       , speed   , 0       )#10 
    if(dir == 14):     motor1(-speed   , speed/2 , speed   , -speed/2)#11
    if(dir == 15):     motor1(-speed   , speed   , speed   , -speed  )#12

def out0():
    if(r0.ldr_r > 600):
        while(r0.imin < 8 and r0.min < 700):
            r0.sensor()
            compass()
            if(r0.shr < 300): 
                move0(12)
            else:
                motor0(0,0,0,0)









    if(r0.ldr_l > 600):
        while((r0.imin > 8 or r0.imin ==0) and r0.min < 700):
            r0.sensor()
            compass()
            r1.sensor()
            darvazeban()
            if(r0.shl < 300): 
                move0(4)
            else:
                motor0(0,0,0,0)
    if(r0.ldr_b > 600 or (r0.ldr_r > 600 and r0.ldr_l > 600)):
        while(r0.imin > 4 and r0.imin < 12 and r0.min < 700):
            r0.sensor()
            compass()
            r1.sensor()
            darvazeban()
            if(r0.shb < 300): 
                move0(0)
            else:
                motor0(0,0,0,0)
    if(r0.ldr_f > 600 or (r0.ldr_r > 600 and r0.ldr_l > 600)):

        while(r0.imin < 4 or r0.imin > 12 and r0.min < 700):
            r0.sensor()
            compass()
            r1.sensor()
            darvazeban()
            if(r0.shf < 300): 
                motor0(0,0,0,0)
            else:
                motor0(0,0,0,0)

def out1():
    if(r1.ldr_r > 600):
        while(r1.imin <= 8 and r1.min < 700):
            r1.sensor()
            compass()
            
            if(r1.shr < 300): 
                move1(12)
            else:
                motor1(0,0,0,0)
    if(r0.ldr_l > 600):
        while(r0.imin >= 8 or r0.imin==0 and r0.min < 700):
            r1.sensor()
            compass()
            

            if(r1.shl < 300): 
                move1(4)
            else:
                motor1(0,0,0,0)
    if(r1.ldr_b > 600 or (r1.ldr_r > 600 and r1.ldr_l > 600)):
        while(r1.imin > 4 and r1.imin < 12 and r1.min < 700):
            r1.sensor()
            compass()
            
            if(r1.shb < 300): 
                move1(0)
            else:
                motor1(0,0,0,0)
    if(r1.ldr_f > 600 or (r1.ldr_r > 600 and r1.ldr_l > 600)):

        while(r1.imin < 4 or r1.imin > 12 and r1.min < 700):
            r1.sensor()
            compass()
            
            if(r1.shf < 300): 
                motor1(0,0,0,0)
            else:
                motor1(0,0,0,0)
def compass():
    global cmp1, cmp0
    cmp0=r0.cmp
    if (cmp0<0):        cmp0=cmp0+255
    if (cmp0>128):      cmp0=cmp0-255
    if (cmp0<128):      cmp0=cmp0
    if(cmp0>-40 and cmp0<40):
        cmp0 = -cmp0*4
    else:
        cmp0 = -cmp0*3
        
    cmp1=r1.cmp
    if (cmp1<0):        cmp1=cmp1+255
    if (cmp1>128):      cmp1=cmp1-255
    if (cmp1<128):      cmp1=cmp1
    if(cmp1>-40 and cmp1<40):
        cmp1 = -cmp1*4
    else:
        cmp1 = -cmp1*3

def darvazeban():
    
   
        if(r1.min<800 and r1.shb>400):
            move1(8)
        elif(r1.min<800 and r1.shb<200):
            move1(0)      
        elif(r1.min<800 and r1.imin==0):
            r1.motor(cmp1,cmp1,cmp1,cmp1)
        elif(r1.min<800 and r1.imin<8 and r1.shr>500 ):
            move1(4) 
        elif(r1.min<800 and r1.imin>8 and r1.shl>500):
            move1(12) 
        else: 
            r1.motor(cmp1,cmp1,cmp1,cmp1)

                
while True:

    r0.sensor()
    r1.sensor()
    # r0.printAll()
    # r1.printAll()
    compass()
    ###########################################out
    out0()    
    out1()
    ########################################### taghib va vasat


    if(r0.ldr_r<700 and r0.ldr_l<700):
        if (r0.min<800):      shift0(r0.imin)
        else:             
            if(r0.shb>300):     move0(8)
            elif(r0.shr<750):   move0(12)
            elif(r0.shl<700):   move0(4)
            else:               r0.motor(cmp0,cmp0,cmp0,cmp0)
    else:
        if(r0.ldr_r>700):       move0(12)    
        elif(r0.ldr_l>700):     move0(4)


    if(r1.ldr_r<700 and r1.ldr_l<700 and r1.ldr_f<700 and r1.ldr_b<700):
        if(r1.min<800 and r1.shb>400):
            move1(8)
        elif(r1.min<800 and r1.shb<300):
            move1(0)      
        elif(r1.min<800 and r1.imin==0):
            r1.motor(cmp1,cmp1,cmp1,cmp1)
        elif(r1.min<800 and r1.imin<8 and r1.shr>500 ):
            move1(4) 
        elif(r1.min<800 and r1.imin>8 and r1.shl>500):
            move1(12) 
        else: 
            r1.motor(cmp1,cmp1,cmp1,cmp1)
    else:
        out1()