from Val_Corrector import *
def save(file, data, symbol):
    with open(file, 'r+') as f:
        for i in data:
            f.write(str(i) + symbol)
def load(file, symbol):
    with open(file, 'r+') as f:
        data = f.read()
        temp = data.split(str(symbol))
        for i in temp:
            if i == '':
                temp.remove(i)
    return corrector_list(temp)
