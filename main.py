from admin import admin
from admin import user
class main_admin:
    def execute (self,choice):
        if choice==1:
         print('______ADD FOOD ITEM______')
         adminobj.addfood()
        if choice==2:
         print('______EDIT FOOD DETAILS______')
         adminobj.editfood()
        if choice==3:
         print('______VIEW ALL FOOD ITEMS______')
         adminobj.viewfood() 
        if choice==4:
         print('______REMOVE A FOOD ITEM______')
         adminobj.removefood() 
class main_user:
     def u_exe(self,choice):
       if choice==1:
         print('______register______')
         userobj.register()

       if choice==2:
         print('_____login______')
         userobj.login()
if __name__=='__main__':
  obj=main_admin()
  adminobj=admin()
  obj1=main_user()
  userobj=user()
  while True:
   print("1.Admin\n2.user")
  
   ch=int(input("Enter your choice  :  "))
   if ch==1:
        
        print('..................you are welcome to admin portal....................')
        
        ch1=int(input('1.ADD FOOD ITEMS\n2.EDIT FOOD ITEMS USING FOODID\n3.VIEW THE LIST OF ALL FOOD ITEMS\n4.REMOVE A FOOD ITEM FROM THE MENU USING FOODID'))
        obj.execute(ch1)
   if ch==2:
      print('..................hello user....................')
       
      ch2=int(input("Enter your choice  :  \n1.Register\n2.Log in to the application"))
      obj1.u_exe(ch2)
       