






while True:
    name=input("name:")
    if name=="" or name==" " or name=="  ":
        print("name ra vared konid:")
        break

    if name.isalpha()==True:
        if name.istitle()==True:
            print("name sabt shod")
            break

        if name.islower() ==True:
            print("harf aval ra bozorg va baghieh horoof ra koochak bezanid")
            continue


while True:
    phone = input("phone:")
    if phone=="" or phone==" " or phone=="  ":
        print("shomare ra vared konid:")
        continue

    
    if phone.startswith("021")==True and len(phone)==11 and phone.isdigit()==True:
        print("shomare sabt shod")
        break

    else:
        print("shomareh eshtebah ast")
        continue


while True:
    address=input("address:")
    if address=="" or address==" " or address=="  ":
        print("address ro vared konid:")
        continue

    if address.isalnum()==True:
        print("address sabt shod")
        break

    else:
        print("address ra be soorat sahih vared konid")
        continue 


while True:
    email=input("email:")
    if email=="" or email==" " or email=="  ":
        print("email ro vared konid:")
        continue

    if email.endswith("@gmail.com")==True:
        print("email sabt shod")
        break

    else:
        print("email ra be soorat sahih vared konid")
        continue


while True:
    code_posti=input("code_posti:")
    if code_posti=="" or code_posti==" " or code_posti=="  ":
        print("code_posti ro vared konid:")
        continue

    if code_posti.isdigit()==True:
        print("code_posti sabt shod")
        break

    else:
        print("code_posti ra be soorat sahih vared konid")
        continue


while True:
    code_melli=input("code_melli:")
    if code_melli=="" or code_melli==" " or code_melli=="  ":
        print("ccode_melli ro vared konid:")
        continue

    if code_melli.isdigit()==True and len(code_melli)==10:
        print("code_melli sabt shod")
        break

    else:
        print("code_melli ra be soorat sahih vared konid")
        continue





   
     





