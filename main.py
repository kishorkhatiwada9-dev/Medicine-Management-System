
from inventory import(show_medicine,
                            default_medicine,
                            main_menu,
                            sell_medicine)



exit = False

# meds_1 = "inventory.txt"
# print(meds_1)

while exit == False:

    main_menu()
    
    input_1 = int(input("Enter a number: "))

    if input_1 == 1:
        meds = show_medicine(default_medicine)
        for i in meds:
            print(i)
        

    elif input_1 == 2:
        meds = sell_medicine(default_medicine)
        
        
        
        