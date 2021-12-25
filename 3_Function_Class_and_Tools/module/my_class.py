
class Hotel():
    
    hType = "5 star" # class variable
    
    def __init__(self, nGuest, nRoom, nHall):
        self.nGuest = nGuest # instance variables
        self.nRoom = nRoom
        self.nHall = nHall+1
        self.__hidVar = 5 # private

    def getInfo(self):
        print("Number of guests is {}".format(self.nGuest))
        print("Number of rooms is {}".format(self.nRoom))
        print("Number of halls is {}".format(self.nHall))
        return "something"
    
    def setGuest(self, nGuest):
        self.nGuest = nGuest
        
    def getGuest(self):
        return self.nGuest

    def setRoom(self, nRoom):
        self.nRoom = nRoom

    def setHall(self, nHall):
       self.nHall = nHall
   
    def dispHid(self):
       print(self.__hidVar)
       
       
class bigHotel(Hotel):
    
    def __init__(self):
        super().__init__(1500,1000,100)
        # Hotel.__init__(self, 1500, 1000, 100)
        
    def getNumber(self):
        return self.nGuest + self.nRoom + self.nHall
        

