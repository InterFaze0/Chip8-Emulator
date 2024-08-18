import numpy as np
import math,random
class Cpu:
    
    def __init__(self,renderer, keyboard, speaker):
        self.renderer = renderer
        self.keyboard = keyboard
        self.speaker = speaker
        
       
        self.memory = [0] * 4096 #TODO Find how to convert uint8 these lists
        self.v = [0] * 16
        self.i = 0
        self.delayTimer = 0
        self.soundTimer = 0
        self.pc = 0x200
        self.stack = []
        self.paused = False
        self.speed = 10
       
    


        
    def loadSpriteIntoMemory(self):
        sprites = [
            0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
            0x20, 0x60, 0x20, 0x20, 0x70, # 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
            0x90, 0x90, 0xF0, 0x10, 0x10, # 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
            0xF0, 0x10, 0x20, 0x40, 0x40, # 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
            0xF0, 0x90, 0xF0, 0x90, 0x90, # A
            0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
            0xF0, 0x80, 0x80, 0x80, 0xF0, # C
            0xE0, 0x90, 0x90, 0x90, 0xE0, # D
            0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
            0xF0, 0x80, 0xF0, 0x80, 0x80  # F
            ]
        for i in range(len(sprites)):
            self.memory[i] = sprites[i] 
    
    
    def loadProgramIntoMemory(self,program):
        for loc in range(len(program)):
            self.memory[0x200 + loc] = program[loc]


    def loadRom(self,romName):
        myrom = open("roms/" + romName,"rb")
        myromasuint = np.fromfile(myrom, dtype=np.uint8)
        
        newuinteight = [int(myromasuint[i]) for i in range(len(myromasuint))]
        self.loadProgramIntoMemory(newuinteight)
       
    def cycle(self):
        for i in range(self.speed):
            if (self.paused == False):
                opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
                self.keyboard.listenTheKeyboard()
                self.executeInstruction(opcode)
                

               
           
        
        if not self.paused:
            self.updateTimers()
            
        # TODO self.playSound()
        
        self.renderer.render()       
    
    def updateTimers(self):
        if self.delayTimer > 0:
            self.delayTimer -= 1
        if self.soundTimer > 0:
            self.soundTimer -= 1
    #TODO def playsound()
    
    def executeInstruction(self,opcode):
        self.pc += 2
        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4
        
        if (opcode & 0xF000) == 0x0000:
            if(opcode) == 0x00E0:
                self.renderer.clear()
            elif opcode == 0x00EE:
                self.pc = self.stack.pop()
        elif (opcode & 0xF000) == 0x1000:
            self.pc = (opcode & 0xFFF)
        elif (opcode & 0xF000) == 0x2000:
            self.stack.append(self.pc)
            self.pc = (opcode & 0xFFF)
        elif (opcode & 0xF000) == 0x3000:
            if (self.v[x] == (opcode & 0xFF)):
                self.pc += 2
        elif (opcode & 0xF000) == 0x4000:
            if (self.v[x] != (opcode & 0xFF)):
                self.pc += 2
        elif (opcode & 0xF000) == 0x5000:
            if (self.v[x] == self.v[y]):
                self.pc += 2
        elif (opcode & 0xF000) == 0x6000:
            self.v[x] = int(np.uint8((opcode & 0xFF)))
        elif (opcode & 0xF000) == 0x7000:
            self.v[x] = int(np.uint8(self.v[x]) + np.uint8((opcode & 0xFF)))
        elif (opcode & 0xF000) == 0x8000:
            if (opcode & 0xF) == 0x0:
                self.v[x] = self.v[y]
                self.v[x] = int(np.uint8(self.v[x]))
            elif (opcode & 0xF) == 0x1:
                self.v[x] |= self.v[y]
                self.v[x] = int(np.uint8(self.v[x]))
            elif (opcode & 0xF) == 0x2:
                self.v[x] &= self.v[y]
                self.v[x] = int(np.uint8(self.v[x]))
            elif (opcode & 0xF) == 0x3:
                self.v[x] ^= self.v[y]
                self.v[x] = int(np.uint8(self.v[x]))
            elif (opcode & 0xF) == 0x4:
                self.v[x] = np.uint8(self.v[x]) + np.uint8(self.v[y])
                self.v[x] = int(np.uint8(self.v[x]))
                sum = self.v[x]
                self.v[0xF] = 0
                if (sum > 0xFF):
                    self.v[0xF] = 1
                self.v[x] = int(np.uint8((sum)))
            elif (opcode & 0xF) == 0x5:
                self.v[0xF] = 0
                if (self.v[x] > self.v[y]):
                    self.v[0xF] = 1
                self.v[x] = np.uint8(self.v[x]) - np.uint8(self.v[y])
                self.v[x] = int(np.uint8(self.v[x]))
            elif (opcode & 0xF) == 0x6:
                self.v[0xF] = int(np.uint8((self.v[x] & 0x1)))
                self.v[x] >>= 1
            elif (opcode & 0xF) == 0x7:
                self.v[0xF] = 0
                if (self.v[y] > self.v[x]):
                    self.v[0xF] = 1
                self.v[x] = int(np.uint8(self.v[y])) - int(np.uint8(self.v[x]))
            elif (opcode & 0xF) == 0xE:
                self.v[0xF] =int(np.uint8((self.v[x] & 0x80)))
                self.v[x] <<= 1 
        elif (opcode & 0xF000) == 0x9000:
            if (self.v[x] != self.v[y]):
                self.pc += 2
        elif (opcode & 0xF000) == 0xA000:
            self.i = (opcode & 0xFFF)
        elif (opcode & 0xF000) == 0xB000:
            self.pc = (opcode & 0xFFF) + self.v[0]
        elif (opcode & 0xF000) == 0xC000:
            rand = math.floor(random.random() * 0xFF)
            self.v[x] = rand & (opcode & 0xFF)
        elif (opcode & 0xF000) == 0xD000:
            widht = 8
            height = (opcode & 0xF)
            self.v[0xF] = 0
            for row in range(height):
                sprite = self.memory[self.i + row]
                for col in range(widht):
                    if ((sprite & 0x80) > 0):
                        if self.renderer.setPixel(self.v[x] + col, self.v[y] + row):
                            self.v[0xF] = int(np.uint8(1))
                    sprite <<= 1        
        elif (opcode & 0xF000) == 0xE000:
            if (opcode & 0xFF) == 0x9E:
                if (self.keyboard.keyValue[self.v[x]]):
                    self.pc += 2
            elif (opcode & 0xFF) == 0xA1:
                if (not self.keyboard.keyValue[self.v[x]]):
                    self.pc += 2
        elif (opcode & 0xF000) == 0xF000:
            if (opcode & 0xFF) == 0x07:
                self.v[x] = int(np.uint8(int(self.delayTimer)))
            elif (opcode & 0xFF) == 0x0A:
                self.paused = True
                controller = True
                while controller:
                    self.keyboard.listenTheKeyboard()
                    for i in range(16):
                        if self.keyboard.keyValue[i]:
                            self.v[x] = int(np.uint8(i))
                            controller = False
                            break
                self.paused = False
            elif (opcode & 0xFF) == 0x15:
                self.delayTimer = self.v[x]
            elif (opcode & 0xFF) == 0x18:
                self.soundTimer = self.v[x]
            elif (opcode & 0xFF) == 0x1E:
                self.i += self.v[x]
                
            elif (opcode & 0xFF) == 0x29:
                self.i = self.v[x] * 5 
                
            elif (opcode & 0xFF) == 0x33:
                self.memory[self.i] = int(self.v[x] / 100)
                self.memory[self.i + 1] = int((self.v[x] % 100) / 10)
                self.memory[self.i + 2] = int(self.v[x] % 10)

            elif (opcode & 0xFF) == 0x55:
                for registerIndex in range((x+1)):
                    self.memory[self.i + registerIndex] = self.v[registerIndex]


            elif (opcode & 0xFF) == 0x65:
                for registerIndex in range((x+1)):
                    self.v[registerIndex] = self.memory[self.i + registerIndex]
                
        else:
            print("Error: " + str(opcode))


