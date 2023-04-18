#introducing dictionary 
shoppingCart={}
#print inputs
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("A. Add product to the cart.")
print("B. Search the product.")
print("C. Delete the product from the cart.")
print("D. Quit.")
Options=0
while (Options!=4):
      

  Options =int(input("Enter your choice"))

  if Options ==1:
      input_user = int(input("Enter the number of items to be added in stationary shop "))
  
      v=0
 #introducing loop    
      while(v<input_user):
        
        if(input_user<3):
            B=input("Enter an item ")
            c=input("Enter the product name:")
            shoppingCart.update({B:c})
            print("Inserted")

        else:
          pass
          if(v==0):
           print("cart is full")
        v=v+1
  
  elif Options ==2:
      A=input("Enter the product name:- ")
      k=0
      for i in shoppingCart.keys():
         if(i==A):
           print(i,":",shoppingCart[i])
           k=1
         else:
           pass
      if(k==0):
        print("Product not found")

  elif Options ==3:
      A=input("Enter the product name:-")
      shoppingCart.pop(A)
      print("deleted")
    

  

  else:
    print ("no option found")




