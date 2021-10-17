
class Hotel:
    
    hType = "5 star" # class variable
    
    def __init__(self, nGuest, nRoom, nHall):
        self.nGuest = nGuest # instance variables
        self.nRoom = nRoom
        self.nHall = nHall
        self.__hidVar = 5 # private

    def getInfo(self):
        return self.nGuest*1000
    
    def setGuest(self, nGuest):
        self.nGuest = nGuest

    def setRoom(self, nRoom):
        self.nRoom = nRoom

    def setHall(self, nHall):
       self.nHall = nHall
   
    def dispHid(self):
       print(self.__hidVar)
       
       
class bigHotel(Hotel):
    
    def __init__(self):
        # super().__init__(1500,1000,100)
        Hotel.__init__(self, 1500, 1000, 100)
        