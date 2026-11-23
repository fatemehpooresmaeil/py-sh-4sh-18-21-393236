





from math import ceil

while True:

    print("welcome to cafe restooran rangarang")
    menu_cafe_restooran_rangarang=input("1.cafee shop 2.restooran 3.ghelyan 4.exit:")

    while True:
        match menu_cafe_restooran_rangarang:
            case "1":
                menu_cafe_rangarang=input("1.mooka 300000 2.caramel_makiato 400000 3.macha 350000 4.exit")

                match menu_cafe_rangarang:
                    case "1":
                        tedad_mooka=int(input("tedad_mook:"))
                        mablagh_mooka=300000*tedad_mooka*1.1
                        print (ceil(mablagh_mooka))
                        break

                    case "2":
                        tedad_caramel_makiato=int(input("tedad_caramel_makiato:"))
                        mablagh_caramel_makiato=tedad_caramel_makiato*400000*1.1
                        print(mablagh_caramel_makiato)
                        break

                    case "3":
                        tedad_macha=int(input("tedad_macha:"))
                        mablagh_macha=tedad_macha*350000*1.1
                        print(ceil(mablagh_macha))
                        break

                    case "4":
                        break


            case "2":
                menu_restooran_rangarang=input("1.kabab 800000 2.joojeh 900000 3.mahi 950000 4.exit")

                match menu_restooran_rangarang:
                    case "1":
                        tedad_kabab=int(input("tedad_kabab:"))
                        mablagh_kabab=tedad_kabab*800000*1.1
                        print(ceil(mablagh_kabab))
                        break

                    case "2":
                        tedad_joojeh=int(input("tedad_joojeh:"))
                        mablagh_joojeh=tedad_joojeh*900000*1.1
                        print(ceil(mablagh_joojeh))    
                        break

                    case "3":
                        tedad_mahi=int(input("tedad_mahi:"))
                        mablagh_mahi=tedad_mahi*950000*1.1
                        print(ceil(mablagh_mahi))
                        break

                    case "4":
                        break


            case "3":
                menu_ghelyan_rangarang=input("1.do_sib 800000 2.love 850000 3.blueberry 900000 4.exit")
                match menu_ghelyan_rangarang:
                    case "1":
                        tedad_do_sib=int(input("tedad_do_sib:"))
                        mablagh_do_sib=tedad_do_sib*800000*1.1
                        print(ceil(mablagh_do_sib))
                        break

                    case "2":
                        tedad_love=int(input("tedad_love:"))
                        mablagh_love=tedad_love*850000*1.1
                        print(ceil(mablagh_love))
                        break

                    case "3":
                        tedad_blueberry=int(input("tedad_blueberry"))
                        mablagh_blueberry=tedad_blueberry*900000*1.1
                        print(ceil(mablagh_blueberry))
                        break

                    case "4":
                        break


            case "4":
                print("mamnoon az inke ma ro entekhab kardid.")
                break

                





