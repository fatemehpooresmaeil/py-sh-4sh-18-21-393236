








from math import ceil

while True:
    print("welcome to Digistyle")
    menu_lebas_kafsh_Digistyle=input("1.lebas 2.kafsh 3.exit")

    while True:
        match menu_lebas_kafsh_Digistyle:
            case "1":
                menu_lebas_Digistyle=input("1.tshirt 1000000 2.pirahan 3000000 3.jean 4000000 4.kapshan 5000000 5.palto 6000000 6.exit")

                match menu_lebas_Digistyle:
                    case "1":
                        tedad_tshirt=int(input("tedad_tshirt:"))
                        mablagh_tshirt=tedad_tshirt*1000000*1.1
                        print(ceil(mablagh_tshirt))
                        break

                    case "2":
                        tedad_pirahan=int(input("tedad_pirahan:"))
                        mablagh_pirahan=tedad_pirahan*3000000*1.1
                        print(ceil(mablagh_pirahan))
                        break

                    case "3":
                        tedad_jean=int(input("tedad_jean:"))
                        mablagh_jean=tedad_jean*4000000*1.1
                        print(ceil(mablagh_jean))
                        break

                    case "4":
                        tedad_kapshan=int(input("tedad_kapshan:"))
                        mablagh_kapshan=tedad_kapshan*5000000*1.1
                        print(ceil(mablagh_kapshan))
                        break

                    case "5":
                        tedad_palto=int(input("tedad_palto:"))
                        mablagh_palto=tedad_palto*6000000*1.1
                        print(ceil(mablagh_palto))
                        break

                    case "6":
                        break


            case "2":
                menu_kafsh_Digistyle=input("1.katooni 3500000 2.boot 6000000 3.sandal 3000000 4.kalej 3800000 5.exit")

                match menu_kafsh_Digistyle:
                    case "1":
                        tedad_katooni=int(input("tedad_katooni:"))
                        mablagh_katooni=tedad_katooni*3500000*1.1
                        print(ceil(mablagh_katooni))
                        break

                    case "2":
                        tedad_boot=int(input("tedad_boot:"))
                        mablagh_boot=tedad_boot*6000000*1.1
                        print(ceil(mablagh_boot))
                        break

                    case "3":
                        tedad_sandal=int(input("tedad_sandal:"))
                        mablagh_sandal=tedad_sandal*3000000*1.1
                        print(ceil(mablagh_sandal))
                        break

                    case "4":
                        tedad_kalej=int(input("tedad_kalej:"))
                        mablagh_kalej=tedad_kalej*3800000*1.1
                        print(ceil(mablagh_kalej))
                        break

                    case "5":
                        break

            case "3":
                print("montazere didare mojadadetoon hastim.")
                break

            

                    




                



    
        

