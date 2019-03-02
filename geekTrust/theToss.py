import random

class TheToss():
    def __init__(self,weather,time):
        self.weather = weather.lower()
        self.time = time.lower()
    def toss(self):
        winner = random.choice(["Lengaburu","Enchai"])
        print ("")
        
        if winner == "Lengaburu":
            if self.weather == "clear" and self.time == "day":
                print ("Lengaburu wins the toss and bats.")
            elif self.weather == "cloudy" and self.time == "night":
                print ("Lengaburu wins the toss and bowls.")
            else:
                print ("Lengaburu wins the toss and bats.")

        elif winner == "Enchai":
            if self.weather == "clear" and self.time == "day":
                print ("Enchai wins the toss and bowls.")
            elif self.weather == "cloudy" and self.time == "night":
                print ("Enchai wins the toss and bats.")
            else:
                print ("Enchai wins the toss and bats.")      

print ("Enter the weather and time(day/night):")
weather,time =  input().split()       
tossResult = TheToss(weather,time)
tossResult.toss()


