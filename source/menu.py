cont = 'y'
while cont == 'y':
    choice = int(input("""1) Predict Share Price upto 5 years with Graph, Open Interest of Puts and Calls
    2) Get a description of Name/Sector/Industry/Current market price after inputting the Sector Serial No."""))

    if choice == 1:
        import SharePricePredictor
    elif choice == 2:
        import sharemarket

    cont = input("Do you want to continue (y/n): ")
