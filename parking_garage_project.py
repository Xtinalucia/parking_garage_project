from typing import Counter


class Garage():
<<<<<<< HEAD
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
=======
    NextTicketNumber = 0

    def __init__(self):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}
        self.counter = 0
        self.spots = 100
 
    def takeTicket(self):
        # Create ticket object
        thisTicket = Ticket(self.NextTicketNumber)
        #Increment counter
        self.NextTicketNumber += 1
        #Decrement spots
        self.spots -= 1
        #Add ticekt to list
        self.tickets.append(thisTicket)
        print(f'Your ticket number is {thisTicket.ticketnum}')
        
        
    def payForParking(self):
         ticketId = int(input('What is your ticket number? '))
         ticketFound = False
         for i in self.tickets:
             if i.ticketnum == ticketId:
                 ticketFound = True
                 amount = int(input("Pay amount here! "))
                 if amount != 0:
                    i.paid = True
                    print('Your ticket has been paid, and you have 15 minutes to leave!')
                 else:
                    print('Don\'t be a cheapskate, pay your ticket bro!')
         if not ticketFound:
             print('The ticket number was not found')
    
    def leaveGarage(self): 
         ticketId = int(input('What is your ticket number? '))
         ticketFound = False
         for i in self.tickets:
             if i.ticketnum == ticketId:
                  ticketFound = True
                  self.spots += 1
                  if i.paid == True:
                    print('Have a nice day [Gate Opens]')
                  else:
                    print('This ticket is unpaid, please pay at ticket machine')
         if not ticketFound:
             print('The ticket number was not found')
        
class Ticket():

   def __init__(self, ticketnum):
        self.ticketnum = ticketnum
        self.paid = False



def run():
    garageOne = Garage()
    while True:
        print('Hello Customer!')
        print('')
        print('1 - Get ticket')
        print('2 - Pay for ticket')
        print('3 - Leave garage')
        print('4 - Quit')
        print('')
        option  = int(input('Please select: '))
        if option == 1:
            garageOne.takeTicket()
        elif option == 2:
           garageOne.payForParking()
        elif option == 3:
            garageOne.leaveGarage()
        elif option == 4:
            break

run()

        



    

        
>>>>>>> 1a6f10c5cbb1d2d5eecbe41a7fa3896954461ec7
