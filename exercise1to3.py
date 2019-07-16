#PROGRAMMING FUNDAMENTALS REINFORCEMENT 4

#1

emotions_dict = {'happy' : 1, 'hunger' : 3, 'stress' : 2}

#2 & 3

class Person:

    def __init__ (self, name, emotion_felt):
        self.name = name 
        self.emotions = emotion_felt

    def emo_level (self):
        for k in self.emotions.keys():
            if self.emotions[k] == 1:
                print("I am feeling a low amount of {}".format(k))
            elif self.emotions[k] == 2:
                print("I am feeling a medium amount of {}".format(k))
            elif self.emotions[k] == 3:
                print("I am feeling a high amount of {}".format(k))

shaheer = Person('Shaheer', emotions_dict)

shaheer.emo_level()