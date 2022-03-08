class ShoppingCart():
    def __init__(self):
        
        self.standardPizzaPrice = 15.00
        self.numberOfHawaiianPizzas = 0
        self.numberOfMexicanPizzas = 0
        self.numberOfPepperoniPizzas = 0
        
        self.hasOnions = False
        self.hasPeppers = False
        self.hasChicken = False
        self.hasSausage = False
        self.hasMushrooms = False
        self.hasTomatoes = False
        self.hasPepperoni = False
        self.hasBacon = False

    def getTotalForMexicanPizzas(self):
        return (self.standardPizzaPrice * self.numberOfMexicanPizzas) if self.numberOfMexicanPizzas > 0 else 0 
        
    def getTotalForHawaiianPizzas(self):
        return (self.standardPizzaPrice * self.numberOfHawaiianPizzas) if self.numberOfHawaiianPizzas > 0 else 0

    def getTotalForPepperoniPizzas(self):
        return (self.standardPizzaPrice * self.numberOfPepperoniPizzas) if self.numberOfPepperoniPizzas > 0 else 0

    def calculateCustomPizzaOrder(self):
        total = 0.0
        if self.hasOnions:
            total = 15.00
        elif self.hasPeppers:
            total = 15.00
        elif self.hasChicken:
            total = 15.00
        elif self.hasSausage:
            total = 15.00
        elif self.hasMushrooms:
            total = 15.00
        elif self.hasTomatoes:
            total = 15.00
        elif self.hasPepperoni:
            total = 15.00
        elif self.hasBacon:
            total = 15.00
        return total
    
    def getTotalBill(self):
        total = self.calculateCustomPizzaOrder()
        total += self.getTotalForMexicanPizzas()
        total += self.getTotalForHawaiianPizzas()
        total += self.getTotalForPepperoniPizzas()         
        return '{:.2f}'.format(total)

    
    def printOrder(self):
        selection = "";
        if self.hasOnions:
            selection += "-Onions\n"
        if self.hasPeppers:
            selection += "-Peppers\n"
        if self.hasChicken:
            selection += "-Chicken\n"
        if self.hasSausage:
            selection += "-Sausage\n"
        if self.hasMushrooms:
            selection += "-Mushrooms\n"
        if self.hasTomatoes:
            selection += "-Tomatoes\n"
        if self.hasPepperoni:
            selection += "-Pepperoni\n"
        if self.hasBacon:
            selection += "-Bacon\n"

              
                   
        return "Build Your Own Pizza\n ingredients:\n" + selection 
    
