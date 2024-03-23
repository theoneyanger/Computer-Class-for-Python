def corrector(val):
    if val.isdecimal() and val.isnumeric():
        num = int(val)
        return num
    elif val.capitalize() == 'True':
        return True
    elif val.capitalize() == 'False':
        return False
    else:
        return val

def corrector_list(list):
    temp = []
    for i in list:
        if i.isdecimal() and i.isnumeric():
            num = int(i)
            temp.append(num)
        elif i.capitalize() == 'True':
            temp.append(True)
        elif i.capitalize() == 'False':
            temp.append(False)
        else:
            temp.append(i)
    return temp