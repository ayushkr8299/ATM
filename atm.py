pin="d36a"
pin_input=input("enter the pin : ")

i=1
while i <= 2 :
    if pin_input == pin:
        success()
        
    else:
        print("retry again")
        pin_input=input(f"enter the {i+1} pin : ")
        print("  your pin blocked \n   limit is exceded")

    i = i+1

def succecc():
    print("succeccfully authenticaicon" )
    

