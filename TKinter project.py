"""Pizza order system - Tkinter GUI
This is a pizza GUI program which permits the user to order pizza
and informs the user when the pizza will be deliver."""

#Importing tkinter to create the GUI
from tkinter import *
import tkinter.messagebox
from ShoppingCart import ShoppingCart

#Setting the initial state for App.
class PizzaApp(object):

    def __init__(self):
        self.shoppingCart = ShoppingCart()
        self.showHawaiianPizzaOptionInCheckout = False
        self.showMexicanPizzaOptionInCheckout = False
        self.showPepperoniPizzaOptionInCheckout = False
        self.showNumberOfBuildYourOwnPizzasInCheckout = False

#Button Handlers
    def showHawaiianPizzaInCheckout(self):
        self.shoppingCart.numberOfHawaiianPizzas = 1
        self.showHawaiianPizzaOptionInCheckout = True
        
    def showMexicanPizzaInCheckout(self):
        self.shoppingCart.numberOfMexicanPizzas = 1
        self.showMexicanPizzaOptionInCheckout = True
        
    def showPepperoniPizzaInCheckout(self):
        self.shoppingCart.numberOfPepperoniPizzas = 1
        self.showPepperoniPizzaOptionInCheckout = True

    def resetMainForm(self, checkoutWindow):
        print("form closing")
        self.showHawaiianPizzaOptionInCheckout = False
        self.showMexicanPizzaOptionInCheckout = False
        self.showPepperoniPizzaOptionInCheckout = False
        checkoutWindow.destroy()
    
    def openCheckoutWindow(self):
        newWindow = Toplevel()
        newWindow.bind('<Escape>', lambda e: self.resetMainForm(newWindow))
        newWindow.protocol("WM_DELETE_WINDOW", newWindow.iconify)
        newWindow.title("Fiora's Pizzeria")
        newWindow.geometry("1500x690")
        newWindow.configure(background='black')

#Adding an image to the background of the new window and changing the color.
        bg1 = PhotoImage(file = "photonewwindow.png")
        label1=Label(newWindow,image=bg1)
        label1.image = bg1
        label1.place(x=0,y=0)

#Creating main label widget for new window.
        mainLabel = Label(newWindow,text="Fiora's Pizzeria",relief="solid",width=25,font=self.defult_font)
        mainLabel.place(x=220, y=20)

#Labels for entry boxes on the second window (New Window).
        checkOutLabel = Label(newWindow,text="Checkout",relief="solid",width=15,font=("Arial Nova Light",20))
        checkOutLabel.place(x=10, y=130)

        myCartLabel=Label(newWindow,text="My Cart",relief="solid",width=20,font=("Freestyle Script",25,"bold"))
        myCartLabel.place(x=920,y=20)

        nameLabel = Label(newWindow,text="Full name:",relief="solid",width=15,font=("Arial Nova Light",12))
        nameLabel.place(x=10, y=200)

        addressLabel = Label(newWindow,text="Address:",relief="solid",width=15,font=("Arial Nova Light",12))
        addressLabel.place(x=10, y=290)

        creditCardLabel = Label(newWindow,text="Credit Card Number:",relief="solid",width=20,font=("Arial Nova Light",12))
        creditCardLabel.place(x=10, y=380)

        
#Entry boxes for the second window. 
        nameEnteredEntry = Entry(newWindow, width=40, font=("Arial Nova Light",14))
        nameEnteredEntry.place(x=10,y=240)
   
        addressEnteredEntry = Entry(newWindow, width=40, font=("Arial Nova Light",14))
        addressEnteredEntry.place(x=10,y=330)

        CreditCardEnteredEntry = Entry(newWindow, width=40, font=("Arial Nova Light",14))
        CreditCardEnteredEntry.place(x=10,y=420)

#Results label for the second window. 
        resultLabel=Label(newWindow,text="",width=70,font=("Arial Nova Light",14))
        resultLabel.place(x=10,y=570)

#User Customer Pizza
        userCustomerPizza=Label(newWindow,text=self.shoppingCart.printOrder(),anchor="w",justify= LEFT,width=18, height=11,font=("Arial Nova Light",11))
        userCustomerPizza.place(x=840,y=250)
        
#Complete Order button
        def displayCompleteOrder():
            name =str(nameEnteredEntry.get())
            answer = "Thank you for your order! " + name + ", your order will be deliver in 30 minutes."
            resultLabel.config(text = answer)

        completeOrder = Button(newWindow, text="Complete Order", command=displayCompleteOrder, relief="raised",width=18,font=("Arial Nova Light",15, "bold"))
        completeOrder.place(x=250, y=500)

#Checkout labels - This displays the type of price of each pizza that is chosen on the first page menu.
        yAxis= 100
        choices = ['1','2','3']
        choices1 = ['1','2','3']
        choices2 = ['1','2','3']
        choices = ['1','2','3']
        tkvar = StringVar()
        tkvar1 = StringVar()
        tkvar2 = StringVar()
               
        def priceOfPizzas(*args):
            self.shoppingCart.numberOfHawaiianPizzas = int(variable.get())
            numberOfHawaiianPizzasChosen=int(variable.get())
            answer = int(numberOfHawaiianPizzasChosen) * 15.00 
            resultPricePizzaHawaiian.config(text = '{:.2f}'.format(answer))
            updateTotal()
            
        resultPricePizzaHawaiian=Label(newWindow,text='{:.2f}'.format(self.shoppingCart.getTotalForHawaiianPizzas()),width=15,font=("Arial Nova Light",11))
        resultPricePizzaHawaiian.place(x=1080,y=yAxis)
               
        print(self.showHawaiianPizzaOptionInCheckout)
        if(self.showHawaiianPizzaOptionInCheckout):
            
            variable = StringVar(value='1')
            variable.trace('w', priceOfPizzas)
            optNumberOfHawaiianPizzas = OptionMenu(newWindow, variable, *choices)
            optNumberOfHawaiianPizzas.place(x=1020,y=yAxis)
            
            hawaiianPizzaLabel = Label(newWindow,text="Hawaiian Pizza",relief="solid", width=20,font=("Arial Nova Light",12))
            hawaiianPizzaLabel.place(x=830, y=yAxis)
            yAxis += 45
#
        def priceOfPizzas1(*args):
            self.shoppingCart.numberOfMexicanPizzas = int(variable1.get())
            numberOfMexicanPizzasChosen=int(variable1.get())
            answer = int(numberOfMexicanPizzasChosen) * 15.00
            resultPricePizzasMexican.config(text = '{:.2f}'.format(answer))
            updateTotal()

            
        resultPricePizzasMexican=Label(newWindow,text='{:.2f}'.format(self.shoppingCart.getTotalForMexicanPizzas()),width=15,font=("Arial Nova Light",11))
        resultPricePizzasMexican.place(x=1080,y=yAxis)
        
        print(self.showMexicanPizzaOptionInCheckout)    
        if(self.showMexicanPizzaOptionInCheckout):
            variable1 = StringVar(value='1')
            variable1.trace('w', priceOfPizzas1)
            optNumberOfMexicanPizzas = OptionMenu(newWindow, variable1, *choices1)
            optNumberOfMexicanPizzas.place(x=1020,y=yAxis)
            mexicanPizzaLabel = Label(newWindow,text="Mexican Pizza",relief="solid",width=20,font=("Arial Nova Light",12))
            mexicanPizzaLabel.place(x=830, y=yAxis)
            yAxis += 45


            
        def priceOfPizzas2(*args):
            self.shoppingCart.numberOfPepperoniPizzas = int(variable2.get())
            numberOfPepperoniPizzasChosen=int(variable2.get())
            answer = int(numberOfPepperoniPizzasChosen) * 15.00 
            resultPricePepperoniPizzas.config(text = '{:.2f}'.format(answer))
            updateTotal()
            
        resultPricePepperoniPizzas=Label(newWindow,text='{:.2f}'.format(self.shoppingCart.getTotalForPepperoniPizzas()),width=15,font=("Arial Nova Light",11))
        resultPricePepperoniPizzas.place(x=1080,y=yAxis)

        print(self.showPepperoniPizzaOptionInCheckout)
        if(self.showPepperoniPizzaOptionInCheckout):
            variable2 = StringVar(value='1')
            variable2.trace('w', priceOfPizzas2)           
            optNumberOfPepperoniPizzas = OptionMenu(newWindow, variable2, *choices2)
            optNumberOfPepperoniPizzas.place(x=1020,y=yAxis)
            
            pepperoniPizzaLabel = Label(newWindow,text="Pepperoni Pizza",relief="solid",width=20,font=("Arial Nova Light",12))
            pepperoniPizzaLabel.place(x=830, y=yAxis)
            yAxis += 45

        def priceOfPizzas3(*args):
            self.shoppingCart.numberOfBuildYourOwnPizzas = int(variable3.get())
            numberOfBuildYourOwnPizzasChosen=int(variable3.get())
            answer = int(numberOfBuildYourOwnPizzasChosen) * 15.00 
            resultPriceBuildYourOwnPizzas.config(text = '{:.2f}'.format(answer))
            updateTotal()
            
        resultPriceBuildYourOwnPizzas=Label(newWindow,text='{:.2f}'.format(self.shoppingCart.calculateCustomPizzaOrder()),width=15,font=("Arial Nova Light",11))
        resultPriceBuildYourOwnPizzas.place(x=1080,y=250)
        

        print(self.showNumberOfBuildYourOwnPizzasInCheckout)
        if(self.showNumberOfBuildYourOwnPizzasInCheckout):
            variable3 = StringVar(value='1')
            variable3.trace('w', priceOfPizzas3)           
            optNumberOfBuildYourOwnPizzas = OptionMenu(newWindow, variable3, *choices3)
            optNumberOfBuildYourOwnPizzas.place(x=990,y=250)

            

#Generating the Total of the Order on the second window.
            
        totalCostOfTheOrder=Label(newWindow,text="The total cost of your order is: $" + str(self.shoppingCart.getTotalBill()),anchor="w",justify= LEFT,width=40, height=3,font=("Arial Nova Light",11))
        totalCostOfTheOrder.place(x=830,y=500)

        def updateTotal():
            totalCostOfTheOrder.config(text ="The total cost of your order is: $" + str(self.shoppingCart.getTotalBill()))

#Generating the main window buttons and labels.
            
    def main_frame(self, window):
        self.defult_font = ("Freestyle Script",40,"bold")

        def generateMenuButton(buttonText, button_Y, commandHandler):
            button1 = Button(window, text=buttonText, relief="raised",command = commandHandler, width=15,font=("Freestyle Script",30,"bold"))
            button1.place(x=60, y=button_Y)

        def generateMenuDescription(widgetText, widget_Y):
            menuLabelDescription=Label(window,text=widgetText,relief="solid",width=35,font=("Bradley Hand ITC",20))
            menuLabelDescription.place(x=400,y=widget_Y)

        def generateByopLabel(widgetText, widget_Y):
            ByopWidget=Label(window, text=widgetText, relief="flat",width=16,font=("Freestyle Script",25,"bold"))
            ByopWidget.place(x=1020, y=widget_Y)
        def generateByopLabel1(widgetText, widget_Y):
            ByopWidget=Label(window, text=widgetText, relief="flat",width=17,font=("Freestyle Script",25,"bold"))
            ByopWidget.place(x=1020, y=widget_Y)
        def generateByopLabel2(widgetText, widget_Y):
            ByopWidget=Label(window, text=widgetText, relief="flat",width=30,justify= LEFT,font=("Freestyle Script",18))
            ByopWidget.place(x=1010, y=widget_Y)
     
          
#Configuration variables.
        buttonStartingPoint_X = 60
        buttonStartingPoint_Y = 250
        pizzaSelectionButtonWidth = 15
        distanceBetweenButtons = 5

#window configuration and addition of an image to the background. 
        window.geometry("1500x690")
        window.title("Fiora's Pizzeria")
        bg = PhotoImage(file = "photo1.png")
        label=Label(window,image=bg)
        label.image = bg
        label.place(x=0,y=0)

#Check buttons for "Build Your Own Pizza!"on main window. 
        def generateCheckButton(buttonText, button_Y, stateVariable): 
            C1 = Checkbutton(window, text =buttonText, variable=stateVariable, onvalue=1, offvalue=0, justify=LEFT,bg="#D2C8CF",padx=10,pady=10,width=10,relief="solid")  
            C1.place(x=1020,y=button_Y)
        def generateCheckButton1(buttonText, button_Y, stateVariable): 
            C1 = Checkbutton(window, text =buttonText, variable=stateVariable, onvalue=1, offvalue=0, justify=LEFT,bg="#D2C8CF",padx=10,pady=10,width=10,relief="solid")  
            C1.place(x=1150,y=button_Y)

#Creating the label widget for the main window. 
        mainLabel=Label(window,text="Fiora's Pizzeria",relief="solid",width=25,font=self.defult_font)
        mainLabel.place(x=400,y=70)

#Creating second label "Menu."
        menuLabel=Label(window,text="Menu",relief="solid",width=10,font=self.defult_font)
        menuLabel.place(x=80,y=150)

        pizzaSize=Label(window, text="All our pizzas are 15 inches for only 15 dollars!", relief="solid",width=40,font=("Freestyle Script",18))
        pizzaSize.place(x=460, y=150)

      
#Creating menu buttons.
        generateMenuButton("Hawaiian Pizza", 250, self.showHawaiianPizzaInCheckout)
        generateMenuButton("Mexican Pizza", 400, self.showMexicanPizzaInCheckout)
        generateMenuButton("Pepperoni Pizza", 550, self.showPepperoniPizzaInCheckout)

       
#Creating third label "Pizza menu description with image."
        generateMenuDescription("Classic Hawaiian Pizza with the house sauce, \rcheese, pineapple and cooked ham.", 255)
        generateMenuDescription("Authentic Mexican Pizza with enchilada sauce, \rmelty cheese, refried beans, and ground beef.", 405)
        generateMenuDescription("Tasty pepperoni pizza with special tomato sauce, \rmelty cheese, and pepperoni.", 555)

#Creating "build your own pizza" buttons.
        generateByopLabel("Build your own Pizza!", 30)
        generateByopLabel2("All are available with our crunchy thin \npizza crust.", 70)
        generateByopLabel1("Veggies", 135)
        generateByopLabel1("Meats", 300)


        onionCheckboxState = IntVar()
        peppersCheckboxState = IntVar()
        chickenCheckboxState = IntVar()
        sausageCheckboxState = IntVar()
        mushroomsCheckboxState = IntVar()
        tomatoesCheckboxState = IntVar()
        pepperoniCheckboxState = IntVar()
        baconCheckboxState = IntVar()

        def addCustomPizzaToShoppingCart():
            self.shoppingCart.hasOnions = onionCheckboxState.get() == 1
            self.shoppingCart.hasPeppers = peppersCheckboxState.get() == 1
            self.shoppingCart.hasChicken = chickenCheckboxState.get() == 1
            self.shoppingCart.hasSausage = sausageCheckboxState.get() == 1
            self.shoppingCart.hasMushrooms = mushroomsCheckboxState.get() == 1
            self.shoppingCart.hasTomatoes = tomatoesCheckboxState.get() == 1
            self.shoppingCart.hasPepperoni = pepperoniCheckboxState.get() == 1
            self.shoppingCart.hasBacon = baconCheckboxState.get() == 1
            
#Creating Check Buttons on the main window.
        generateCheckButton("Onions",190,onionCheckboxState)        
        generateCheckButton("Peppers",240, peppersCheckboxState)
        generateCheckButton("Chicken",360, chickenCheckboxState)       
        generateCheckButton("Sausage",410, sausageCheckboxState)
        generateCheckButton1("Mushrooms",190, mushroomsCheckboxState)
        generateCheckButton1("Tomatoes",240, tomatoesCheckboxState)
        generateCheckButton1("Pepperoni",360, pepperoniCheckboxState)
        generateCheckButton1("Bacon",410, baconCheckboxState)

#Creating the "Create" button for build your own pizza.
   
        createButton = Button(window, text="Create", bg="#CDC3CF",command = addCustomPizzaToShoppingCart,relief="raised",width=15,font=("Freestyle Script",15,"bold"))
        createButton.place(x=1070, y=475)

#Creating "Checkout" button on the second window. 
        checkoutButton = Button(window, text="Checkout", command = self.openCheckoutWindow,relief="raised",width=15,font=("Freestyle Script",30,"bold"))
        checkoutButton.place(x=1020, y=550)

window = Tk()
app = PizzaApp()
app.main_frame(window)
window.mainloop()
