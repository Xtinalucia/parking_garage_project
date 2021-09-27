class Garage():
    #Attributes: 2 Lists and Dictionary 
    def __init__(self, tickets, parkingspaces, numParkingSpaces, numTickets):
        self.numParkingSpaces = numParkingSpaces
        self.numTickets = numTickets
        self.tickets = []
        self.parkingSpaces = []
        currentTickets = {}
     #Method to decrease ticket and spaces   
    def takeTicket(self):
        self.numTickets = numTickets - 1
        self.numPArkingSpaces = numParkingSpaces - 1
     #Method to pay ticket or assign an id of True/Paid - sent to dictionary  
    def payForParking(self, ticket_id):
        amount = int(input("Collect Payment now"))
        if not amount:
            print("Your ticket is not paid.")
        else:
            currentTickets[ticket_id] = True
      #Method to check if True/Paid  or send back to previous Method to pay    
    def leaveGarage(self, ticket_id):
        if currentTickets[ticket_id] == True:
            print("Thank you, have a nice day.")
        else:
            payForParking(ticket_id)
            
        self.numParkingSpaces = numParkingSpaces + 1
        self.numTickets = numTickets + 1
        
def parkingGarage(Garage):
    garageTickets = []
    garageSpaces = []
    numSpaces = 10
    numTickets = 10
    #parkingGarage = Garage(self, tickets, parkingspaces, numParkingSpaces, numTickets)
     
    print("Ticket amount before:", numTickets)
    Garage.takeTicket()
    print("Ticket amount after:", numTickets)