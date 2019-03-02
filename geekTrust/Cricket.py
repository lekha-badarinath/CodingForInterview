import random
import time

def partTwo():
    score = 40; ballsPerOver = 6; overs = 4
    probabilities = ["Dot Ball",1,2,3,4,5,6,"Out"]
    players = ["Kirat Boli","N.S Nodhi","R Rumrah","Shashi Henra"]
    board = {
            "Kirat Boli": [5,    30,    25,    10,    15,    1,    9,    5],
            "N.S Nodhi" : [10,    40,    20,    5,    10,    1,    4,    10],
            "R Rumrah" :  [20,    30,    15,    5,    5,    1,    4,    20],
            "Shashi Henra" : [30,    25,    5,    0,    5,    1,    4,    30]
        }
    score_board = {}
    for player in players:
        score_board[player] = [0,0]
    playing = [players[0],players[1]]
    players.pop(0)
    players.pop(0)
    count = 0
    while overs > 0:
        print ("%d overs left. %d runs to win\n" %(overs,score))
        for ball in range(0, ballsPerOver):
            run = random.choices(probabilities, board[playing[0]])
            run = run[0]        
            score_board[playing[0]][1] = score_board[playing[0]][1]+1
                        
            if run ==1:
                print ("%d.%d %s scores %d run" %(count, ball+1, playing[0], run))
            elif run in [2,3,4,5,6]:
                print ("%d.%d %s scores %d runs" %(count, ball+1, playing[0], run))
            else:
                print ("%d.%d %s %s" %(count, ball+1, playing[0], run))

            if type(run) is not str:
                score -= run
                score_board[playing[0]][0] = score_board[playing[0]][0]+run
                if run in [1,3,5]:
                    playing = playing[::-1]
            
            if run == "Out":
                if len(players)!=0:
                    playing.pop(0)
                    playing.insert(0,players[0])
                    players.pop(0)
                else:
                    playing.pop(0)
                    print ("\nAll out. Game over!")
                    break
                
            if score < 0:
                break
        
        ballsRemaining = overs*6-(ball+1)
        playing = playing[::-1]
        count += 1
        print ("")
        
        if (score < 0):
            print ("Lengaburu won by %d wicket(s) and with %d balls remaining." %(len(players)+1, ballsRemaining))
            break
        
        if len(playing)==1:
            print ("Enchai won with %d balls remaining.\n" %(ballsRemaining))
            break
        
        overs -= 1
        time.sleep(1)
    if (score > 0 & len(playing)>1):
        print ("Enchai won by %d run" %(40-score))
    elif (score == 0):
        print ("It's a tie!")    
    
    print ("Lengaburu scores")
    for scores in score_board:
        print ("%s - %d (%d balls)" %(scores,score_board[scores][0],score_board[scores][1]))
    
partTwo()
