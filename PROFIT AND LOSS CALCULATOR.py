# creating the variables for getting the SP and CP from the user
CP = float(input("Enter the Cost Price: "))
SP = float(input("Enter the Selling Price: "))

if (SP > CP):
    profit = SP - CP
    profit = round(profit,2)
    print("Congrats!, you have just made a profit of rupees",profit)
else:
    loss = CP - SP
    loss = round(loss,2) 
    print("Alas! you have just made a loss of rupees",loss)