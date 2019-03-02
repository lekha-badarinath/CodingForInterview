import random
import time

class TheLastFour():
    def __init__(self):
        self.score = 40             #The number of runs needs to win
        self.overs = 4              #No. of overs remaining
        self.probabilities = ["Dot Ball",1,2,3,4,5,6,"Out"]  
        self.players = []           #list to hold the players' names
        self.playing = []           #list to hold the names of the players who are currently playing
        self.board = {}             #dictionary for the probability board
        self.score_board = {}       #dictionary to store the runs scored and balls used by every player.
            
    def theGame(self):
        ballsPerOver = 6            #No. of balls in 1 over
        count = 0                   
        for player in self.players: #initialing the runs and balls for each player to 0 in score board
            self.score_board[player] = [0,0]
        
        self.playing = [self.players[0],self.players[1]]    
        self.players.pop(0)         #player added to the self.playing list removed, so the next player gets ready to be picked up to bat
        self.players.pop(0)         #since player[1] is also added to the self.playing list, he is removed as well
        
        while self.overs > 0:
            print ("%d overs left. %d runs to win\n" %(self.overs,self.score))
            for ball in range(0, ballsPerOver):
                time.sleep(0.5)
                run = random.choices(self.probabilities, self.board[self.playing[0]])
                run = run[0]        
                self.score_board[self.playing[0]][1] += 1   #counter for adding the number of balls used by the player batting    
                
                if run ==1:
                    print ("%d.%d %s scores %d run" %(count, ball+1, self.playing[0], run))
                elif run in [2,3,4,5,6]:
                    print ("%d.%d %s scores %d runs" %(count, ball+1, self.playing[0], run))
                else:
                    print ("%d.%d %s %s" %(count, ball+1, self.playing[0], run))     
    
                if type(run) is not str:
                    self.score -= run
                    self.score_board[self.playing[0]][0] += run  #counter for adding the runs used by the player batting
                    if run in [1,3,5]:
                        self.playing = self.playing[::-1]  #to change the player batting when run = 1,3 or 5
                
                if run == "Out":
                    self.score_board[self.playing[0]][1] -= 1 #since an "out" ball should not be counted
                    if len(self.players)!=0:
                        self.playing.pop(0)     #if a player gets out, remove him from the "self.playing" list
                        self.playing.insert(0,self.players[0])  #add the player next in line from self.players list to self.playing list 
                        self.players.pop(0)     #remove the player added from the "self.players" list
                    else:
                        self.playing.pop(0)
                        print ("\nAll out. Game over!")
                        break
                    
                if self.score < 0:
                    break  
            time.sleep(0.5)  
            ballsRemaining = self.overs*6-(ball+1)
            self.playing = self.playing[::-1]   #after ever over, the player batting will change
            count += 1
            print ("")
            if (self.score < 0):
                break
               
            if len(self.playing)==1:
                break
 
            self.overs -= 1
         
        
        results = [self.score, self.playing, self.players, ballsRemaining, self.score_board]    
        return results
    
    def match(self):
        self.players = ["Kirat Boli","N.S Nodhi","R Rumrah","Shashi Henra"]
        self.board = {
                    "Kirat Boli": [5,    30,    25,    10,    15,    1,    9,    5],
                    "N.S Nodhi" : [10,    40,    20,    5,    10,    1,    4,    10],
                    "R Rumrah" :  [20,    30,    15,    5,    5,    1,    4,    20],
                    "Shashi Henra" : [30,    25,    5,    0,    5,    1,    4,    30]
                    }
        
        result = self.theGame()     #calling theGame() method from within the match() method
        
        time.sleep(0.5)
        print ("*"*50)
        if result[0] > 0:
            print ("Enchai won by %d runs." %(result[0]))
        elif result[0] == 0:
            print ("It's a tie!.")
        elif result[0] < 0:
            print ("Lengaburu won by %d wicket(s) and with %d balls remaining." %(len(result[2])+1,result[3]))
        print ("*"*50)
        time.sleep(0.5)
        
        print ("Lengaburu scores -")
        for score in result[4]:
            print ("%s - %d (%d balls)" %(score,result[4][score][0],result[4][score][1]))

game = TheLastFour()
game.match()    