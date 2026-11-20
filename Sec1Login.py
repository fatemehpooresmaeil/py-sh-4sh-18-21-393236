






while True:
    user=input("username:")
    password=input("password:")

    while True:
        if user == "" or user ==" " or user =="  ":
            print("username khod ra vared konid")
            break

        if user.isalnum()==True:
            if user.isalpha()==True:
                print("user mored taeed hast")
                break


        if password == "" or password ==" " or password =="  ":
            print("password khod ra vared konid")
            break

        if password.isascii()==True:
            if password.isdigit()==True:

                if password== "1111":
                    print("password mored taeed mibashad")
                    break
                

