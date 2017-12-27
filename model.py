# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:07:48 2017

@author: Danny
"""

import time;

class Model:
    speed = 5
    def __init__(self, lv = 5):
        self.speed = lv
        self.state = "IDLE"
        
    def Set_State(self, key_In):
        if key_In == "":
            print(0)

        elif key_In =="":
            print(1)

        else:
            print(2)
    def Change_Speed(self, lv):
        self.speed = lv
        
    def Get_Speed(self):
        return self.speed
    
class GameModel(Model):
    def __init__(self, lv = 5):
        super().__init__(lv)
        self.frozen_block = []#block [x,y,color]
        self.falling_block = []
        
        #0改隨機
        self.falling_class = 0 # 1 -> 長條,2 -> L,3 -> 反L,4 -> z,5 -> 反z,6 -> T,7 -> 田
        self.board = (8,15)
        self.Play()
        
    def Turn(self):
        if self.falling_class == 1:
            print(1)

        elif self.falling_class == 2:
            print(2)

        elif self.falling_class == 3:
            print(3)

        elif self.falling_class == 4:
            print(4)

        elif self.falling_class == 5:
            print(5)

        elif self.falling_class == 6:
            print(6)

        elif self.falling_class == 7:
            print(7)

        else:
            print("error")
            
    def Move(self):
        
        if not self.Check_Frozen():
            return "Lose"
            
    def Check_Frozen(self):
#        for ... 所有:
#            if 有接觸:
#                self.Check_Erase()
#                return self.Check_End()
        return True#遊戲未結束
               
    def Check_Erase(self):
        print("Erase")
        

    def Check_End(self):
        #改state
        print("Check_End")
        return True
        

    def New_Block(self):
        self.falling_class = 0
        if self.falling_class == 1:
            print(1)

        elif self.falling_class == 2:
            print(2)

        elif self.falling_class == 3:
            print(3)

        elif self.falling_class == 4:
            print(4)

        elif self.falling_class == 5:
            print(5)

        elif self.falling_class == 6:
            print(6)

        elif self.falling_class == 7:
            print(7)

        else:
            print("error")
            
    def Fall_Down(self):
        self.falling_block = [[1,1,1],[1,2,1],[1,3,1],[1,4,1]]
        temp_block =[]
        for index in self.falling_block:
            temp_block.append([index[0], index[1] + 1, index[2]])
            print(temp_block)
        if not self.Check_Frozen():
            return "Lose"
        
    def Play(self):
        exact_Speed = 1 / self.speed
        while self.state == "PLAY":
            time.sleep(exact_Speed)
            if self.Fall_Down() == "Lose":
                self.Set_State("IDLE")
                return
        return
        
a = GameModel()
a.Fall_Down()