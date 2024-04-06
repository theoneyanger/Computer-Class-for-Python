from random import *
from Saver_Loader import *
class net:
    def __init__(self):
        self.ID = 'h̵̖͕̹͇̫̬̝̩̉͗̃̅͑̒̈́͛̈́̓̉̊̔ͅa̶̧̫͈̺̟͙̟̼̭̞͗̀͗̃̏̓̕ḥ̶̢̢͎͚̘̮̄̉͗̓͆͝ą̴͔͉͈̏́̋̓͐̐̚͝' # yea I know cybersecurity, how can you tell?
        self.chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.chars += [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.connected = False
        self.data = load("NET_Data.txt", '/')


    def request(self): # request an ID
        print("Creating ID...")
        for i in range(11):
            self.ID += choice(self.chars)
        print(f"Your unique ID is {self.ID}. It will be valid until you:\n"
              f"1.Request a new ID\n"
              f"2.Close the device\n"
              f"3.Disconnect")
        return self.ID

    def connect(self, skip_ID): # connect to the NET, when 'skip_ID' is True, the ID is not required
        if skip_ID == True:
            self.connected = True
        else:
            inp = input("Enter your unique ID:\n")
            if inp == self.ID:
                print("Your device has successfully connected to the NET!")
                self.connected = True
            else:
                print("ID doesn't match")

    def disconnect(self): # disconnect from the NET
        choice = input("Confirm disconnection (y/n) :\n")
        if choice.lower() == 'y':
            print("Disconnecting device...")
            self.connected = False
        else:
            print("Disconnection cancelled")

    def send(self): # send data to the NET
        if self.connected == False:
            print("Your device is not connected to the NET yet")
        else:
            dt = corrector(input("Enter data to store on the NET:\n"))
            self.data.append(dt)
            print(f"Your data has been entered at position {self.data.index(dt)}")
            save('NET_Data.txt', self.data, '/')

    def retrieve(self): # get data from the NET
        if self.connected == False:
            print("Your device is not connected to the NET yet")
        else:
            choice = int(input("Select position of data to be retrieved:\n"))
            try:
                print(f"Your desired data has been found: {self.data[int(choice - 1)]}")
            except:
                print(f"Could not find any data at position {choice}")

