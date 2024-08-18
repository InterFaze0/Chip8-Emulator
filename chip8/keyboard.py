import pygame,sys
class Keyboard:
    def __init__(self):
        self.keyMap = {
            49:  0x1, # 1
			50:  0x2, # 2
			51:  0x3, # 3
			52:  0xc, # 4
			113: 0x4, # Q
			119: 0x5, # W
			101: 0x6, # E
			114: 0xD, # R
			97:  0x7, # A
			115: 0x8, # S
			100: 0x9, # D
			102: 0xE, # F
			122: 0xA, # Z
			120: 0x0, # X
			99:  0xB, # C
			118: 0xF  # V
        }
        self.keyValue = {
            0x1:False, # 1
			0x2:False, # 2
			0x3:False, # 3
			0xc:False, # 4
			0x4:False, # Q
			0x5:False, # W
			0x6:False, # E
			0xD:False, # R
			0x7:False, # A
			0x8:False, # S
			0x9:False, # D
			0xE:False, # F
			0xA:False, # Z
			0x0:False, # X
			0xB:False, # C
			0xF:False  # V
		}
    def listenTheKeyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_2:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_3:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_4:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_q:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_w:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_e:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_r:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_a:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_s:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_d:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_f:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_z:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_x:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_c:
                    self.keyValue[self.keyMap[event.key]] = True
                if event.key == pygame.K_v:
                    self.keyValue[self.keyMap[event.key]] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_2:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_3:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_4:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_q:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_w:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_e:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_r:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_a:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_s:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_d:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_f:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_z:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_x:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_c:
                    self.keyValue[self.keyMap[event.key]] = False
                if event.key == pygame.K_v:
                    self.keyValue[self.keyMap[event.key]] = False
        

   