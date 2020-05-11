class Kitty:
    
    def __init__ (self, catName, meowSound):
        self.name = catName
        self.sound = meowSound

    def __repr__(self):
        s = "the kitty's name is " + (self.name) + " and the sound she makes is " + (self.sound)
        return s

    def setSound(self, meowSound):
        self.sound = meowSound

    def getSound(self):
        return self.sound

    def likesMilk(self):
        return True