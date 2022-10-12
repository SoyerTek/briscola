class Card:
    def __init__(self, number=0, seed="") -> None:
        """
        A card with its number=0..10
        and seed = "B", "C", "D", "S" 
        """
        self.number = number
        self.seed = seed
    
    def __str__(self):
        return self.seed + str(self.number)
    
    def getPointsValue(self) -> int:
        """
        returns the point value of the card
        """
        match self.number:
            case 1 : return 11 #Asso
            case 3 : return 10 #Tre
            case 8 : return 2  #Fante
            case 9 : return 3  #Cavallo
            case 10 : return 4 #Re
            case _ : return 0
    
    def getValue(self) -> int:
        """
        returns max(number, pointVal*10)
        """
        #110, 100, 40, 30, 20, 7, 6, 5, 4, 2
        return max(self.number, self.getPointsValue() * 10)