from typing import Counter


class Garage():
    NextTicketNumber = 1

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
                 if amount !=0:
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
                  self.spots += 1
                  ticketFound = True
                  if i.paid == True:
                    print('Have a nice day')
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

        



    

        
