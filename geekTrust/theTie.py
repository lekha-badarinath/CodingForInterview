import random
import time

class TieBreaker():
    def __init__(self):
        self.score = 0          #counter for counting total score
        self.balls = 6          #No. of balls 
        self.probabilities = ["Dot Ball",1,2,3,4,5,6,"Out"]
        self.playing = []       #list containing the players' names.
        self.board = {}         #dictionary for the probability table.      
        self.scoreBoard = {}    #dictionary to store the runs scored and balls used by every player.
    
    def theGame(self):
        self.score = 0          #to reset the counter every time the function is called.
        self.scoreBoard = {}    #to reset the scoreBoard ever time the function ends.
        for player in self.playing:     #initialing the runs and balls for each player to 0 in score board
            self.scoreBoard[player] = [0,0]
        for ball in range(0,self.balls):
            time.sleep(0.5)
            run = random.choices(self.probabilities,self.board[self.playing[0]])    #generates a list of the weighted random number using the probability table.                                                                                    
            run = run[0]
            self.scoreBoard[self.playing[0]][1] += 1 #counter for the number of balls used by the player on crease.
            
            if run ==1:
                print ("0.%d %s scores %d run" %(ball+1, self.playing[0], run))
            elif run in [2,3,4,5,6]:
                print ("0.%d %s scores %d runs" %(ball+1, self.playing[0], run))
            else:
                print ("0.%d %s %s" %(ball+1, self.playing[0], run))            
            
            if type(run) is not str:    #if the run is not a "dot ball" or "Out"
                self.score += run
                self.scoreBoard[self.playing[0]][0] = self.scoreBoard[self.playing[0]][0]+run  #counter for the number of runs made by the player on crease.                
                if run in [1,3,5]:
                    self.playing = self.playing[::-1]   #to change the player batting when run = 1,3 or 5
            
            if run == "Out":
                self.scoreBoard[self.playing[0]][1] -= 1    #since an "out" ball must not be counted
                self.playing.pop(0) #if a player is out, he must be removed from the "playing" list
                break                   
        time.sleep(0.5)
        
        return self.score,self.scoreBoard
    
    def Lengaburu(self):
        print ("Lengaburu innings -\n")
        self.playing = ["Kirat Boli","N.S Nodhi"]
        self.board = {
                "Kirat Boli":[5,    10,    25,    10,    25,    1,    14,    10],
                "N.S Nodhi": [5,    15,    15,    10,    20,    1,    19,    15]}
                

        
        result = self.theGame()  #calling theGame() method in Lengaburu() method and storing the returned values
        
#         print ("\nLengaburu scored - %d runs" %(result[0]))
        return result
  
    def Enchai(self):
        print ("\nEnchai innings -\n")
        self.board = {
                "DB Vellyers":[5,    10,    25,    10,    25,    1,    14,    10],
                "H Mamla":[10,    15,    15,    10,    20,    1,    19,    10]
            }
        self.playing = ["DB Vellyers","H Mamla"]
        
        result = self.theGame() #calling theGame() method in Enchai() method and storing the returned values
        
#         print ("\nEnchai scored - %d runs" %(result[0]))  
        return result
    
    def results(self):
        #this method will call and execute the Lengaburu and Enchai methods and return the final results
        lengaburu = self.Lengaburu()
        enchai = self.Enchai()
        print ("")
        time.sleep(0.5)
        print ("*"*50)
        if lengaburu[0] > enchai[0]:
            print ("Lengaburu won by %d runs." %(lengaburu[0]-enchai[0]))
        elif lengaburu[0] < enchai[0]:
            print ("Enchai won by %d runs." %(enchai[0]-lengaburu[0]))
        elif lengaburu[0] == enchai[0]:
            print ("It's a tie again!")
        print ("*"*50)        
        
        print ("Lengaburu")
        time.sleep(0.5)
        for scores in lengaburu[1]:
            print ("%s - %d(%d balls)" %(scores, lengaburu[1][scores][0], lengaburu[1][scores][1] ))
        time.sleep(0.5)
        print ("\nEnchai")
        for scores in enchai[1]:
            print ("%s - %d(%d balls)" %(scores, enchai[1][scores][0], enchai[1][scores][1] ))

game = TieBreaker()    
game.results()
