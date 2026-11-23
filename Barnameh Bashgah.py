





from math import ceil

while True:

    print("welcome to bartar gym")

    barname_bartar_gym=input("1.sans_banovan 2.sans_aghayan 3.exit:")

    while True:
        match barname_bartar_gym:
            case "1":
                barname_sans_banovan_bartar_gym=input("1.yooga 3000000 2.pilates 3200000 3.trx 3500000 4.exit")

                match barname_sans_banovan_bartar_gym:
                    case "1":
                        tedad_yooga=int(input("tedad_yooga:"))
                        mablagh_yooga=tedad_yooga*3000000
                        print(ceil(mablagh_yooga))
                        break

                    case "2":
                        tedad_pilates=int(input("tedad_pilates:"))
                        mablagh_pilates=tedad_pilates*3200000
                        print(ceil(mablagh_pilates))
                        break

                    case "3":
                        tedad_trx=int(input("tedad_trx:"))
                        mablagh_trx=tedad_trx*3500000
                        print(ceil(mablagh_trx))
                        break

                    case "4":
                        break


            case "2":
                barname_sans_aghayan_bartar_gym=input("1.badansazi 2500000 2.karate 3500000 3.tekvando 4000000 4.exit")

                match barname_sans_aghayan_bartar_gym:
                    case "1":
                        tedad_badansazi=int(input("tedad_badansazi:"))
                        mablagh_badansazi=tedad_badansazi*2500000
                        print(ceil(mablagh_badansazi))
                        break

                    case "2":
                        tedad_karate=int(input("tedad_karate:"))
                        mablagh_karate=tedad_karate*3500000
                        print(ceil(mablagh_karate))
                        break

                    case "3":
                        tedad_tekvando=int(input("tedad_tekvando:"))
                        mablagh_tekvando=tedad_tekvando*4000000
                        print(ceil(mablagh_tekvando))
                        break

                    case "4":
                        break


            case "3":
                print("mamnoon az entekhab bartar")
                break

            



