



from math import ceil

while True:
    print("welcome to cofe restooran bahar")
    menu_cofe_restooran_bahar=input("1.cofe 2.restooran 3.exit:")

    while True:
        match menu_cofe_restooran_bahar:
            case "1":
                menu_cofe_bahar=input("1.hot chocolate 300000 2.macha 350000 3.afoogato 360000 4.esperso 400000 5.late 420000 6.exit")

                match menu_cofe_bahar:
                    case "1":
                        tedad_hot_chocolate=int(input("tedad_hot_chocolate:"))
                        meablagh_hot_chocolate=tedad_hot_chocolate*300000*1.1
                        print(ceil(meablagh_hot_chocolate))
                        break


                    case "2":
                        tedad_macha=int(input("tedad_macha:"))
                        meablagh_macha=tedad_macha*350000*1.1
                        print(ceil(meablagh_macha))
                        break

                    case "3":
                        tedad_afoogato=int(input("tedad_afoogato:"))
                        meablagh_afoogato=tedad_afoogato*360000*1.1
                        print(ceil(meablagh_afoogato))
                        break

                    case "4":
                        tedad_esperso=int(input("tedad_esperso:"))
                        meablagh_esperso=tedad_esperso*400000*1.1
                        print(ceil(meablagh_esperso))
                        break

                    case "5":
                        tedad_late=int(input("tedad_late:"))
                        meablagh_late=tedad_late*420000*1.1
                        print(ceil(meablagh_late))
                        break

                    case "6":
                        break


            case "2":
                menu_restooran_bahar=input("1.pizza 1900000 2.pasta 1500000 3.sandwich 1200000 4.burger 1000000 5.salad 900000 6.exit")
                match menu_restooran_bahar:
                    case "1":
                        tedad_pizza=int(input("tedad_pizza:"))
                        meablagh_pizza=tedad_pizza*1900000*1.1
                        print(ceil(meablagh_pizza))
                        break

                    case "2":
                        tedad_pasta=int(input("tedad_pasta:"))
                        meablagh_pasta=tedad_pasta*1500000*1.1
                        print(ceil(meablagh_pasta))
                        break

                    case "3":
                        tedad_sandwich=int(input("tedad_sandwich:"))
                        meablagh_sanwich=tedad_sandwich*1200000*1.1
                        print(ceil(meablagh_sanwich))
                        break

                    case "4":
                        tedad_burger=int(input("tedad_burger:"))
                        meablagh_burger=tedad_burger*1000000*1.1
                        print(ceil(meablagh_burger))
                        break

                    case "5":
                        tedad_salad=int(input("tedad_salad:"))
                        meablagh_salad=tedad_salad*900000*1.1
                        print(ceil(meablagh_salad))
                        break

                    case "6":
                        break


            case "3":
                print("mamnoon az inke ma ro entekhab kardid.")
                break

            




                    
                
                
                
                
                
                
                
                

                