# KennedyAnn White
cont = 0
Atc_price= 65
Silk_price = 85
TS_price = 70
WG_price = 45
FL_price = 150
Trim_price = 20
DC_price = 25
DT_price = 15
ST_price = 30
TD_price = 50
print("Thank you for choosing KayKay's Hair Services. Please select a number from our Menu below!")
while cont != 10:
    Subtotal = 0
    Extra = 0
    Final_price = 0
    Tip = 0
    print("\n\nMenu of 5 styles")
    print(f'101. Around the way curl ${Atc_price}'
          f'\n102. Silk Press \t ${Silk_price}'
          f'\n103. Two-strand Twists \t ${TS_price}'
          f'\n104. Wash and Go \t ${WG_price}'
          f'\n105. Crochet Faux Locs \t ${FL_price}'
          f'\n10. Quit')
    cont = int(input("\n\nChoose your style  "))
    while cont != 101 and cont != 102 and cont != 103 and cont != 104 and cont != 105 and cont != 10:
            cont= int(input("Please enter a valid number."))
    if  cont == 101:
                cont2 = 0
                choice1 = False
                choice2 = False
                choice3 = False
                print(f'You have chosen \"Around the way curl\". ')
                Style = "Around the Way Curl"
                Subtotal += Atc_price
                while cont2 != 20:
                    cont2 = int(input(f'\nWould you like to choose an add-on?   '
                          f'\n\n201. Trim (Two-strand Twist or Silk press ONLY) (${Trim_price})'
                          f'\n202. Deep conditioning mask (${DC_price})'
                          f'\n203. Detangling (${DT_price})'
                          f'\n204. Steam treatment (Around the way curl or Wash and Go ONLY) (${ST_price})'
                          f'\n205. Take down service (Crochet Faux Locs ONLY) (${TD_price})'
                          f'\n20. Done'
                          f'\n      '))
                    while cont2 != 201 and cont2 != 202 and cont2 != 203 and cont2 != 204 and cont2 != 205 and cont2 != 20:
                        cont2= int(input("Please enter a valid number."))
                    if  cont2 == 201:
                            print("This service is for Two-strand Twists or Silk press. Please choose another option.")
                    elif cont2 == 202:
                            print(f'\"Deep conditioning mask\" has been added to your total.')
                            a = "Deep conditioning mask"
                            choice1 = True
                            Extra += DC_price
                    elif cont2 == 203:
                            print(f'\"Detangling\" has been added to your total.')
                            b = "Detangling"
                            choice2 = True
                            Extra += DT_price
                    elif cont2 == 204:
                            print(f'\"Steam treatment\" has been added to your total.')
                            c = "Steam treatment"
                            choice3 = True
                            Extra += ST_price
                    elif cont2 == 205:
                            print("This service is for Crochet Faux Locs. Please choose another option.")
                        

                print(f'Your subtotal is ${Subtotal}.')
                ti = float(input("Tip amount:  "))
                Tip += ti
                print(f'**********Your receipt**********')
                print(f'Style: {Style} (${Atc_price})')
                if choice1 == True:
                    print(f'Extra: {a} (${DC_price})')
                if choice2 == True:
                    print(f'Extra: {b} (${DT_price})')
                if choice3 == True:
                    print(f'Extra: {c} (${ST_price})')
                if choice1 != True and choice2 != True and choice3 != True:
                    print(f'Extra: None ($0)')
                print(f'Tip: ${Tip}')
                Final_price = Subtotal + Tip + Extra
                print(f'Total: ${Final_price}')

    elif  cont == 102:
                cont2 = 0
                choice1 = False
                choice2 = False
                choice3 = False
                print(f'You have chosen \"Silk Press\". ')
                Style = "Silk Press"
                Subtotal += Silk_price
                while cont2 != 20:
                    cont2 = int(input(f'\nWould you like to choose an add-on?   '
                          f'\n\n201. Trim (Two-strand Twist or Silk press ONLY) (${Trim_price})'
                          f'\n202. Deep conditioning mask (${DC_price})'
                          f'\n203. Detangling (${DT_price})'
                          f'\n204. Steam treatment (Around the way curl or Wash and Go ONLY) (${ST_price})'
                          f'\n205. Take down service (Crochet Faux Locs ONLY) (${TD_price})'
                          f'\n20. Done'
                          f'\n      '))
                    if  cont2 == 201:
                        print(f'\"Trim\" has been added to your total.')
                        a = "Trim"
                        choice1 = True
                        Extra += Trim_price
                    elif cont2 == 202:
                        print(f'\"Deep conditioning mask\" has been added to your total.')
                        b = "Deep conditioning mask"
                        choice2 = True
                        Extra += DC_price
                    elif cont2 == 203:
                        print(f'\"Detangling\" has been added to your total.')
                        c = "Detangling"
                        choice3 = True
                        Extra += DT_price
                    elif cont2 == 204:
                        print(f' This service is for Around the way curl or Wash and Go. Please choose another option.')
                    elif cont2 == 205:
                        print("This service is for Crochet Faux Locs. Please choose another option.")
                            

                print(f'Your subtotal is ${Subtotal}.')
                ti = float(input("Tip amount:  "))
                Tip += ti
                print(f'**********Your receipt**********')
                print(f'Style: {Style} (${Silk_price})')
                if choice1 == True:
                    print(f'Extra: {a} (${Trim_price})')
                if choice2 == True:
                    print(f'Extra: {b} (${DC_price})')
                if choice3 == True:
                    print(f'Extra: {c} (${DT_price})')
                if choice1 != True and choice2 != True and choice3 != True:
                    print(f'Extra: None ($0)')
                print(f'Tip: ${Tip}')
                Final_price = Subtotal + Tip + Extra
                print(f'Total: ${Final_price}')

    elif  cont == 103:
                cont2 = 0
                choice1 = False
                choice2 = False
                choice3 = False
                print(f'You have chosen \"Two-strand Twists\". ')
                Style = "Two-strand Twists"
                Subtotal += TS_price
                while cont2 != 20:
                    cont2 = int(input(f'\nWould you like to choose an add-on?   '
                          f'\n\n201. Trim (Two-strand Twist or Silk press ONLY) (${Trim_price})'
                          f'\n202. Deep conditioning mask (${DC_price})'
                          f'\n203. Detangling (${DT_price})'
                          f'\n204. Steam treatment (Around the way curl or Wash and Go ONLY) (${ST_price})'
                          f'\n205. Take down service (Crochet Faux Locs ONLY) (${TD_price})'
                          f'\n20. Done'
                          f'\n      '))
                    if  cont2 == 201:
                        print(f'\"Trim\" has been added to your total.')
                        a = "Trim"
                        choice1 = True
                        Extra += Trim_price
                    elif cont2 == 202:
                        print(f'\"Deep conditioning mask\" has been added to your total.')
                        b = "Deep conditioning mask"
                        choice2 = True
                        Extra += DC_price
                    elif cont2 == 203:
                        print(f'\"Detangling\" has been added to your total.')
                        c = "Detangling"
                        choice3 = True
                        Extra += DT_price
                    elif cont2 == 204:
                        print(f' This service is for Around the way curl or Wash and Go. Please choose another option.')
                    elif cont2 == 205:
                        print("This service is for Crochet Faux Locs. Please choose another option.")
                    
                print(f'Your subtotal is ${Subtotal}.')
                ti = float(input("Tip amount:  "))
                Tip += ti
                print(f'**********Your receipt**********')
                print(f'Style: {Style} (${TS_price})')
                if choice1 == True:
                    print(f'Extra: {a} (${Trim_price})')
                if choice2 == True:
                    print(f'Extra: {b} (${DC_price})')
                if choice3 == True:
                    print(f'Extra: {c} (${DT_price})')
                if choice1 != True and choice2 != True and choice3 != True:
                    print(f'Extra: None ($0)')
                print(f'Tip: ${Tip}')
                Final_price = Subtotal + Tip + Extra
                print(f'Total: ${Final_price}')

    elif  cont == 104:
                cont2 = 0
                choice1 = False
                choice2 = False
                choice3 = False
                print(f'You have chosen \"Wash and Gol\". ')
                Style = "Wash and Go"
                Subtotal += WG_price
                while cont2 != 20:
                    cont2 = int(input(f'\nWould you like to choose an add-on?   '
                          f'\n\n201. Trim (Two-strand Twist or Silk press ONLY) (${Trim_price})'
                          f'\n202. Deep conditioning mask (${DC_price})'
                          f'\n203. Detangling (${DT_price})'
                          f'\n204. Steam treatment (Around the way curl or Wash and Go ONLY) (${ST_price})'
                          f'\n205. Take down service (Crochet Faux Locs ONLY) (${TD_price})'
                          f'\n20. Done'
                          f'\n      '))
                    if  cont2 == 201:
                            print("This service is for Two-strand Twists or Silk press. Please choose another option.")
                    elif cont2 == 202:
                            print(f'\"Deep conditioning mask\" has been added to your total.')
                            a = "Deep conditioning mask"
                            choice1 = True
                            Extra += DC_price
                    elif cont2 == 203:
                            print(f'\"Detangling\" has been added to your total.')
                            b = "Detangling"
                            choice2 = True
                            Extra += DT_price
                    elif cont2 == 204:
                            print(f'\"Steam treatment\" has been added to your total.')
                            c = "Steam treatment"
                            choice3 = True
                            Extra += ST_price
                    elif cont2 == 205:
                            print("This service is for Crochet Faux Locs. Please choose another option.")
                        

                print(f'Your subtotal is ${Subtotal}.')
                ti = float(input("Tip amount:  "))
                Tip += ti
                print(f'**********Your receipt**********')
                print(f'Style: {Style} (${WG_price})')
                if choice1 == True:
                    print(f'Extra: {a} (${DC_price})')
                if choice2 == True:
                    print(f'Extra: {b} (${DT_price})')
                if choice3 == True:
                    print(f'Extra: {c} (${ST_price})')
                if choice1 != True and choice2 != True and choice3 != True:
                    print(f'Extra: None ($0)')
                print(f'Tip: ${Tip}')
                Final_price = Subtotal + Tip + Extra
                print(f'Total: ${Final_price}')
                
    elif  cont == 105:
                cont2 = 0
                choice1 = False
                choice2 = False
                choice3 = False
                print(f'You have chosen \"Crochet Faux Locs\". ')
                Style = "Crochet Faux Locs"
                Subtotal += FL_price
                while cont2 != 20:
                    cont2 = int(input(f'\nWould you like to choose an add-on?   '
                          f'\n\n201. Trim (Two-strand Twist or Silk press ONLY) (${Trim_price})'
                          f'\n202. Deep conditioning mask (${DC_price})'
                          f'\n203. Detangling (${DT_price})'
                          f'\n204. Steam treatment (Around the way curl or Wash and Go ONLY) (${ST_price})'
                          f'\n205. Take down service (Crochet Faux Locs ONLY) (${TD_price})'
                          f'\n20. Done'
                          f'\n      '))
                    if  cont2 == 201:
                        print("This service is for Two-strand Twists or Silk press. Please choose another option.")
                    elif cont2 == 202:
                        print(f'\"Deep conditioning mask\" has been added to your total.')
                        a = "Deep conditioning mask"
                        choice1 = True
                        Extra += DC_price
                    elif cont2 == 203:
                        print(f'\"Detangling\" has been added to your total.')
                        b = "Detangling"
                        choice2 = True
                        Extra += DT_price
                    elif cont2 == 204:
                        print(f' This service is for Around the way curl or Wash and Go. Please choose another option.')
                    elif cont2 == 205:
                        c = "Take down"
                        choice3 = True
                        Extra += TD_price
                    
                print(f'Your subtotal is ${Subtotal}.')
                ti = float(input("Tip amount:  "))
                Tip += ti
                print(f'**********Your receipt**********')
                print(f'Style: {Style} (${FL_price})')
                if choice1 == True:
                    print(f'Extra: {a} (${Trim_price})')
                if choice2 == True:
                    print(f'Extra: {b} (${DC_price})')
                if choice3 == True:
                    print(f'Extra: {c} (${TD_price})')
                if choice1 != True and choice2 != True and choice3 != True:
                    print(f'Extra: None ($0)')
                print(f'Tip: ${Tip}')
                Final_price = Subtotal + Tip + Extra
                print(f'Total: ${Final_price}')
    elif cont == 10:
        print("Goodbye!")
