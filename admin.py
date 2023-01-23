
class admin:

     def __init__ (self):
      self.fooditem={}
      self.FoodID=101
     def addfood(self):
        FoodID=self.FoodID
        self.FoodID+=1
        name=input('enter food name : ')
        quantity=input('enter quantity : ')
        price=int(input('enter price : '))
        discount=int(input('enter discount : '))
        stock=input('enter the quantity  : ')
        self.fooditem[FoodID]=[name,quantity,price,discount,stock]
        print('food added successfully....')
        print(self.fooditem)

     def editfood(self):
        food_id=int(input('enter food id  which u want to update'))
        for i,k in self.fooditem.items():
            if i==food_id:
                food_name = input("Enter updated food name : ")
                f_qty = (input("Enter updated food quantity : "))
                f_price = input("Enter updated food price : ")
                f_dis = input("Enter updated food discount : ")
                f_stock = (input("Enter updated food stock : "))
                 
                k[0]=food_name
                k[1]=f_qty
                k[2]=f_price
                k[3]=f_dis
                k[4]=f_stock
                print(self.fooditem)
                print('updated successfully')
                return
        print('pls check foodid and try again')

     def viewfood(self):
         for i,j in self.fooditem.items():
            print(f'food id : {i}\nName : {j[0]}\nQuantity : {j[1]} pieces\nPrice : {j[2]}rs\nDiscount : {j[3]}%\nStock : {j[4]} pieces available')

     def removefood(self):
        food_id=int(input('enter food id  which u want to delete'))
        for i,k in self.fooditem.items():
            if i==food_id:
               del self.fooditem[i]
               print('food item remove successfully')
               return
        print('check your ID and try again')
   
     def get(self):
      for i,j in self.fooditem.items():        
             return f'Food ID: {i},{j[0]},{j[1]},{j[2]}'
           



class user(admin):
    def __init__(self):
      self.user_data = {}
      self.order_history = []

    def register(self):
          user_id = len(self.user_data) + 1
        
          full_name=input("Enter the full name :    ")
          phone_no=input("Enter the mobile no  :   ")
          email=input("Enter the email  :   ")
          add=input("Enter the address  :   ")
          password=input("Enter the password  :   ")

         
          self.user_data[user_id] = {'full_name': full_name, 'phone_number': phone_no, 'email': email, 'address': add, 'password': password}
          print(f"User {full_name} has been registered with ID: {user_id}.")

         

    def login(self):
         Email=input("Enter the email  :   ")
         Password=input("Enter the password  :   ")
         for i, j in self.user_data.items():
            if j['email'] == Email and j['password'] == Password:
                    print(f"Welcome {j['full_name']}! You are now logged in.")
        
                    print("1. Place new order")
                    print("2. Order history")
                    print("3. Update profile")
                    print("4. Log out")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        admin.get(self)
                    elif choice == 2:
                        self.view_history()
                    elif choice == 3:
                        self.update_profile()
                    elif choice == 4:
                        print("Logged out successfully")
                  
                        
               
         else:
            print("Invalid email or password")


      