
default_medicine = ["Paracetamol 500mg, Lomus, 1200, 5, 45, 10", 
"Cetirizine 10mg, Quest, 800, 4, 35, 12", 
"Amoxicillin 500mg, Nepal Remedies, 500, 12, 110, 15", 
"Pantoprazole 40mg, Deurali-Janta, 600, 7, 60, 8", 
"ORS Sachet, Time Pharma, 300, 20, 180, 12"]

def show_medicine(medicine):
    return medicine

def main_menu():
    print("=" * 44)
    print(f"{'Jiban Bachau Medico' :>30}")
    print("=" * 44)

    print(f"{'1. Display Medicine'}")
    print(f"{'2. Sell Medicine'}")
    print(f"{'3. Restock Medicine'}")
    print(f"{'4. Save & Exit'}")

price = []

def sell_medicine(data, money):

    exit_med = True
    
    customer_name = input("Enter the name of customer: ").strip()
    while exit_med == True:
        med_name = input("Enter medicine name or ('done' to exit): ").strip()

        med_1 = data[0].split(",")


        #Accessing the data of Paracetamol
        Paracetamol_med = med_1[0].strip()
        Lomus = med_1[1].strip()
        qty_paracetamol = int(med_1[2].strip())
        price_tab = med_1[3].strip()
        price_strip = med_1[4].strip()
        tab_strip = med_1[5].strip()

        if med_name == "P":

            # try:
            tab_or_strip = input("You want to buy a 'tablet' or 'strip': ").strip()

            if tab_or_strip.lower() == "tablet":
                qty_tablet = int(input("Enter the quantyty: "))
                if qty_tablet >0 and qty_tablet <= int(qty_paracetamol):
                    qty_paracetamol-=qty_tablet

                    med_1[2] = str(qty_paracetamol)
                    data[0] = ", ".join(med_1)

                    amt = qty_tablet * 5
                    money.append(amt)
                    total = 0
                    i = 0
            
                    while i<len(money):
                        total+=money[i]
                        i+=1
                    exit_med = ask_yes_no()


                    
                elif qty_tablet <= 0:
                    print("Enter positive value!")

                elif qty_tablet > int(qty_paracetamol):
                    print(int(qty_paracetamol),"medicine is only available.")

                else:
                    print("Please enter valid number.")
            

            elif tab_or_strip.lower() == "strip":
                qty_strip = int(input("Enter the number of strip: "))

                if qty_strip > 0 and qty_strip <= int(qty_paracetamol)/10:
                    qty_paracetamol-= qty_strip * 10

                    med_1[2] = str(qty_paracetamol)
                    data[0] = ", ".join(med_1)

                    exit_med = ask_yes_no()

                elif qty_strip <= 0:
                    print("Enter positive value!")
                
                elif qty_strip > int(qty_paracetamol)/10:
                    print(int(qty_paracetamol)/10,"number of strip is only available.")
                
                else:
                    print("Please enter valid number.")



            return data, money

def ask_yes_no():
    while True:
        input_yes_or_no = input("Do you want to add more meds: 'yes' or 'no' ")

        if input_yes_or_no.lower() == "yes":
            return True
        
        elif input_yes_or_no.lower() == "no":
            return False

        else: 
            print("Please enter valid input!")





        


    


    
    

    
