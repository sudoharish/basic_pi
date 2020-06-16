import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
btp = 2
rdp = 3
GPIO.setup(btp, GPIO.OUT,   initial=GPIO.LOW  )
GPIO.setup(rdp, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as #input (button)  
   # set GPIO24 as an output (LED)  

try:  
    while True:
      print("sleep 2 sec")
      sleep(2)         # wait 0.1 seconds  
      GPIO.output(btp,1)
      print("gpio pin set High")
      sleep(0.3)
      GPIO.output(btp,0)
      sleep(1)
      GPIO.output(btp,1)
 


      if not GPIO.input(rdp):
         print("high")
      else:
         print("low")
      GPIO.output(btp,0)
      
      
      
    
  
  
finally:                   # this block will run no matter how the try block exits  
    #GPIO.output(btp,0)
    #GPIO.cleanup()
    # clean up after yoursel
    print("h")
