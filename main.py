
from inventorySystem import(show_medicine,
                            default_medicine,
                            main_menu)



exit = False

while exit == False:

    main_menu()
    
    input_1 = int(input("Enter a number: "))
    if input_1 == 1:
        meds = show_medicine(default_medicine)
        for i in meds:
            print(i)
        exit = True
        