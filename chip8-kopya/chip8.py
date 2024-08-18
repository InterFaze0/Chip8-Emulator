from cpu import Cpu
from renderer import Renderer
from keyboard import Keyboard
from speaker import Speaker
import time



myRenderer = Renderer()
myKeyboard = Keyboard()
mySpeaker  = Speaker()
myCpu = Cpu(myRenderer,myKeyboard,mySpeaker)


fpsInterval,then,startTime,now,then,elapsed = 0,0,0,0,0,0
fps = 60


def initvm():
    global fpsInterval,then,startTime,now,then,elapsed
    fpsInterval = 1000 / fps
    then = round(time.time() * 1000)
    startTime = then
    myCpu.loadSpriteIntoMemory()
    myCpu.loadRom("BLITZ")
    myCpu.cycle()
    step()
    
   
    

def step():
    global now,then,elapsed
    counter = 0
    while True: 
        now = round(time.time() * 1000)
        elapsed = now - then
        if elapsed > fpsInterval:
            myCpu.cycle()
            print("Cycle: ",counter," Registers:",myCpu.v)
            counter += 1
            
            
        
    
      



initvm()
