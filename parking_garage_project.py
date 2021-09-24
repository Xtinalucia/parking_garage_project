class Garage():

    tickets = []
    parkingSpaces = []
    currentTicket = {}

    def __init__(self, ticket=25, parking=25):
        self.ticket = ticket
        self.parking = parking

    def takeTicket(self):
        self.ticket -=1
        print(f'There are {self.ticket} tickets left')
        self.parking -=1
        print(f'There are {self.parking} parking spaces left')

    def payForParking(self):
         amount = int(input("Pay amount here! "))
         if amount !=0:
            print('Your ticket has been paid, and you have 15 minutes to leave!')
         else:
            print('Don\'t be a cheapskate, pay your ticket bro!')

test = Garage()
test.takeTicket()
test.payForParking()

#     def leaveGarage(self):
#         pass   

# def add(self):
#         item_name = input('What is the name of the item you would like to add? ')
#         item_price = float(input(f'What is the price of {item_name}? '))
#         item = Item(item_name, item_price)
#         self.cart.append(item)
#         print(f'{item.name} has been added to your cart.')
    
#     def remove(self):
#         item_to_remove = input("What item would you like to remove? ")
#         cart_item_names = set([item.name for item in self.cart])
#         if item_to_remove in cart_item_names:
#             for i in range(len(self.cart)):
#                 if self.cart[i].name == item_to_remove:
#                     removed_item = self.cart.pop(i)
#                     break
#             print(f"{removed_item.name} has been removed from your cart.")
#         else:
#             print(f"{item_to_remove} is not in your cart")
    
#     def clear(self):
#         self.cart.clear()
#         print("Your cart has been cleared")
    
#     def show(self):
#         for item in self.cart:
#             print(f"{item.name} - ${item.price}")
            
#     def get_total(self):
#         total = 0
#         for item in self.cart:
#             total += item.price
#         return total
    

# my_company = run()