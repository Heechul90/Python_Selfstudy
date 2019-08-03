### House_Password




def house_password(pw):
    if len(pw) < 10:
        return False
    elif pw.upper() == pw:
        return False
    elif pw.lower() == pw:
        return False

    return any(c.isdigit() for c in pw)  # 숫자인지 판단, 하나 이상이면 True


house_password('asdfDDasdfasdfa12312e')