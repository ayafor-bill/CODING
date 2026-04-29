class Restaurant : 
    def __init__(self, name, food_type):
        self.name = name
        self.food_type = food_type
        self.number_served = 0
        
    def describe_restua(self):
        print(f"{self.name} serves {self.food_type} food")
        
    def restau_state(self):
        print(f"{self.name} is now open and has served {self.number_served} customers")
    
    def set_number_served(self, order_placed):
        if(order_placed > self.number_served):
            print(f"{order_placed} customers have been served")
        
### Creating Instances ###
restaurant = Restaurant('Chef Pai', 'Colonary')
restaurant.describe_restua()
restaurant.restau_state()
restaurant.set_number_served(3)

