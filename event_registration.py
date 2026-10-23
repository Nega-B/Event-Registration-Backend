def register():
    name= input("Enter your Name:")
    email= input("Enter your email:")
    department= input("Enter your Deptartment:")
    if '@' in email and '.' in email:
      print("Registration successful")
      print("Name :",name )
      print("Email :",email)
      print("Department :",dept)
    else:
      print("Invalid email !")  
register()    
