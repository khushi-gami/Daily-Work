from abc import ABC ,abstractmethod
print("---- Python OOP Project : Restaurant Management System ----")

print()

# -----------------------------------  MenuItem Class ------------------------------------------
class MenuItem(ABC):
    def __init__(self,name,item_id,price):
        self.name = name
        self.item_id = item_id
        self.__price = price
        self.__is_available = True
        
    def get_price(self):
        return self.__price
    
    def get_is_available(self):
        return self.__is_available
    
    def set_is_available(self,is_available):
        self.__is_available = is_available
        
    @ abstractmethod
    def display(self):
        pass
        
# ----------------------------------- FoodItem Class ---------------------------------------

class FoodItem(MenuItem):
    def __init__(self,name,item_id,price,spice_level,is_vegetarian):
        super().__init__(name,item_id,price)
        self.spice_level = spice_level
        self.is_vegetarian = is_vegetarian

    def display(self):
        print()
        print("----  Food Item Details ----")
        print(f"Name : {self.name}")
        print(f"Item ID : {self.item_id}")
        print(f"Price : {self.get_price()}")
        print(f"Spice Level : {self.spice_level}")
        print(f"Vegetarian : {self.is_vegetarian}")
        
        if self.get_is_available():
            print("Status : Available.")
        else:
            print("Status : Not Available.")
            
        print()


# -----------------------------------  Colddrink Class --------------------------------------
class Colddrink(MenuItem):
    def __init__(self,name,item_id,price,volume_ml,is_alcoholic):
        super().__init__(name,item_id,price)
        self.volume_ml = volume_ml
        self.is_alcoholic = is_alcoholic

    def display(self):
        print()
        print("----  Cold Drink Details ----")
        print(f"Name : {self.name}")
        print(f"Item ID : {self.item_id}")
        print(f"Price : {self.get_price()}")
        print(f"Volume (ml) : {self.volume_ml}")
        print(f"Is Alcoholic (yes/no) : {self.is_alcoholic}")
 
        if self.get_is_available():
            print("Status : Available.")
        else:
            print("Status : Not Available.")
            
        print()

# For show details..
food = None
drink = None
total_bill = 0


while True:

    print("---- Choose an Operation ----")
    print("1. Add a Food Item")
    print("2. Add a Cold drink")
    print("3. Place an Order")
    print("4. Cancel an Order")
    print("5. Show Menu Details")
    print("6. Exit")

    print()

    # Take Choice option from user..
    choice = int(input("Enter your choice (1 to 6) : "))

    print()

# ----------------------------------- Get Food Details ------------------------------------
    if choice == 1:
        
        print("Food Item -----")

        food = FoodItem(
            input("Enter Item Name : "),
            input("Enter Item ID : "),
            float(input("Enter Price : ")),
            input("Enter Spice Level : "),
            input("Is Vegetarian (yes/no) : ")
            )

        print()
        
        # print food item details..
        print(f"Food Item created with name : {food.name}, ID : {food.item_id}, Price : {food.get_price()}, Spice Level : {food.spice_level}, Is Vegetarian : {food.is_vegetarian}.")

        print()
        
# ----------------------------------- Get Cold Drink Details ------------------------------------
    elif choice == 2:
            
        print("Cold Drink ----")

        drink = Colddrink(
            input("Enter Item Name : "),
            input("Enter Item ID : "),
            float(input("Enter Price : ")),
            int(input("Enter Volume (ml) : ")),
            input("Is Alcoholic (yes/no) : ")
            )

        print()
       
        # print cold drink details..
        print(f"Cold Drink created with name : {drink.name}, ID : {drink.item_id}, Price : {drink.get_price()},  Volume : {drink.volume_ml}ml, Alcoholic : {drink.is_alcoholic}. ")

        print()

# ----------------------------------- For Place Order ------------------------------------
    elif choice == 3 :
                
        order_item_id = input("Enter Item ID to order : ")
        
        print()
        
        if food is None  and  drink is None:
            print("No any item is added..")
            
            print()
            
        elif food is not None and order_item_id == food.item_id:
            
            if food.get_is_available():
                print(f"Order placed for {food.name} ({food.item_id}).")
                
                total_bill += food.get_price()
                
                print(f"Added to bill. Running total : {total_bill}.")
                food.set_is_available(False)
                
                print()
            else:
                print("This Food item is already ordered.")
                print()
        
        elif drink is not None and order_item_id == drink.item_id:
            
            if drink.get_is_available():
                print(f"Order placed for {drink.name} ({drink.item_id})")
                
                total_bill += drink.get_price()
                
                print(f"Added to bill. Running total : {total_bill}.")
                drink.set_is_available(False)
                
                print()
            else:
                print("This Drink is already ordered.")
                print()
                
        else:
            print("This Item ID does not Exist..!!")
            
            print()
              
    elif choice == 4 :

        cancel_order_item_id = input("Enter Item ID to cancel order : ")
        
        print()
        
        if food is None  and  drink is None:
            print("No any item is added..")
            
            print()
            
        elif food is not None and cancel_order_item_id == food.item_id:
            
            if not food.get_is_available():
                print(f"Order cancelled for {food.name} ({food.item_id}).")
                
                total_bill -= food.get_price()
                
                print(f"Removed from bill. Running total : {total_bill}.")
                food.set_is_available(True)
                
                print()
            else:
                print("This Food item is not currently ordered.")
                print()
        
        elif drink is not None and cancel_order_item_id == drink.item_id:
            
            if not drink.get_is_available():
                print(f"Order cancelled for {drink.name} ({drink.item_id})")
                
                total_bill -= drink.get_price()
                
                print(f"Removed from bill. Running total : {total_bill}")
                drink.set_is_available(True)
                
                print()
            else:
                print("This Drink is not currently ordered.")
                print()
                
        else:
            print("This Item ID does not Exist..!!")
            
            print()       
    
    elif choice == 5 :
                
        print("Choose menu type to show :")
        print("1. Food Item")
        print("2. Cold Drink")
        
        print()
        
        show_details_choice = int(input("Enter your choice : "))
        
        print()
        
        if show_details_choice == 1:
            
            if food is None :
               print("Food item is not added !")
               print()
            else:
                food.display()
                
        elif show_details_choice == 2:
            
            if drink is None :
                print("Cold Drink is not added !")
                print()
            else:
                drink.display()
        else:
            print("Invalid choice Entered..!!")

    elif choice == 6:

        print("Exiting the Programme. Visit Again...")

        print()

        print("Goodbye!")
     
        break
    
    else:
        # when user entered invalid choice..
        print("Invalid Choice Entered !")

        print()
 
    print("--- Choose another Operation ---")

    print()
