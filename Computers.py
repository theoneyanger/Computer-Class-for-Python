from time import *
from ELP import *
from Calculator import *
from Saver_Loader import *
from Val_Corrector import *
from datetime import datetime
class Computer:
    def __init__(self, name, mem_size, ram_size, OS, processor_speed, dev, battery, filename):
        self.name = name
        self.file = filename
        self.memory_size = mem_size
        self.ram_size = ram_size
        self.OS = OS
        self.speed = processor_speed
        self.wait = 0
        if self.speed <= 50:
            self.wait = 10
        elif self.speed >= 100 and self.speed <= 150:
            self.wait = 8
        elif self.speed >= 150 and self.speed <= 300:
            self.wait = 5
        elif self.wait >= 300 and self.wait <= 350:
            self.wait = 3
        self.wait -= self.ram_size / 2
        if self.wait <= 0:
            self.wait = 1

        self.max_dev = dev
        self.dev = 0
        self.battery = battery
        self.powered = False
        self.ctrl = False
        if self.battery > 100:
            self.battery = 100
        self.memory = []



    def ask(self): # enter a command
        if len(self.memory) == self.memory_size:
            print(f"MESSAGE FROM {self.name}: Memory has reached maximum capacity")
        elif self.battery == 0:
            print(f"MESSAGE FROM {self.name}: Closing down for energy saving...")
            self.close()
        elif self.battery <= 30:
            print(f"MESSAGE FROM {self.name}: Battery percentage below 30. Recharge suggested")
            if self.battery <= 50:
                print(f"MESSAGE FROM {self.name}: Battery percentage below 50. Recharge suggested")
            elif self.battery <= 20:
                print(f"MESSAGE FROM {self.name}: Battery percentage below 20. Recharge suggested")
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        if self.ctrl == False:
            print(f"MESSAGE FROM {self.name}: Access not granted.")
        else:
            print("Use '//help' for list of commands")
            comm = input(f"Select action for {self.name}:\n")
            comms = ['//recharge', '//close', '//connect_device', '//system_check', '//help']
            if comm == '//help':
                self.help()
            elif comm == '//recharge':
                self.recharge()
            elif comm == '//close':
                self.close()
            elif comm == '//connect_device':
                self.connect_dev()
            elif comm == '//system_check':
                self.check_self()
            elif comm == '//update':
                self.update()
            elif comm == '//help':
                self.help()
            elif comm == '//eject_device':
                self.eject_device()
            elif comm == '//operations':
                self.operations()
            elif comm == '//insta_charge':
                self.insta_charge()
            elif comm == '//mem_add':
                self.mem_add()
            elif comm == '//mem':
                self.mem()
            elif comm == '//mem_del':
                self.mem_del()
            elif comm == '//mem_clear':
                self.mem_clear()
            elif comm == '//time':
                self.time()
            else:
                print(f"Could not find command {comm}")
                if self.ctrl == True:
                    self.ask()





    def boot(self): # boot up
        print(f"{self.name} is booting up...")
        self.memory = load(self.file, '-')
        sleep(self.wait)
        print(f"{self.name} has booted up.")
        logged(self.name)
        self.powered = True

    def mem_clear(self): # clear all memory
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Deleting memory...")
        sleep(self.wait)
        self.memory.clear()
        print("Memory cleared")
        if self.ctrl == True:
            self.ask()
    def time(self): # view current time
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        time = datetime.now()
        time = time.strftime("%H:%M:%S")
        print(f"MESSAGE FROM {self.name}: Current time is {time}")
        if self.ctrl == True:
            self.ask()

    def mem(self): # view memory
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Memory:\n")
        for i in self.memory:
            print(f"{i}\n")
        if self.ctrl == True:
            self.ask()

    def mem_del(self): # remove value from memory
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        for i in self.memory:
            print(i)
        choice = input(f"MESSAGE FROM {self.name}: Select value to remove:\n")
        if choice in self.memory:
            self.memory.remove(choice)
            print(f"Value {choice} removed. Remaining storage {self.memory_size - len(self.memory)}")
            if self.ctrl == True:
                self.ask()
        else:
            print("An error occurred. Recording error in Logs.txt...")
            error(self.OS, "ValNotInList")
            if self.ctrl == True:
                self.ask()
    def mem_add(self): # add valueto memory
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        if len(self.memory) == self.memory_size:
            print("Memory has reached maximum capacity. Cannot add value to memory")
            self.ask()
        val = input(f"MESSAGE FROM {self.name}: Enter value to add to memory:\n")
        self.memory.append(corrector(val))
        print(f"Memory {val} added. Remaning storage {self.memory_size - len(self.memory)}")
        if self.ctrl == True:
            self.ask()
    def insta_charge(self): # hidden command for instant charge
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        self.battery = 100
        if self.ctrl == True:
            self.ask()


    def operations(self): # perform simple operations
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        a = int(input(f"MESSAGE FROM {self.name}: Enter first number:\n"))
        b = int(input("Enter second number:\n"))
        choice = input("Addition\nSubtraction\nMultiplication\nDivision\nSelect operation:\n")
        if choice.lower() == 'addition':
            self.battery -= 2
            sleep(self.wait)
            print(f"Result:{add(a, b)}")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        elif choice.lower() == 'subtraction':
            self.battery -= 2
            sleep(self.wait)
            print(f"Result:{sub(a, b)}")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        elif choice.lower() == 'multiplication':
            self.battery -= 2
            sleep(self.wait)
            print(f"Result:{mult(a, b)}")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        elif choice.lower() == 'division':
            self.battery -= 2
            sleep(self.wait)
            print(f"Result:{div(a, b)}")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        else:
            print("Operation not found")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()


    def help(self): # display commands available
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Printing list of commands...")
        comms = {'//recharge': "Recharge the computer's battery",
                 '//close': "Shut down the computer",
                 '//connect_device': "Connect a peripheral to the computer",
                 '//system_check': "Get a report on the computer's status",
                 '//help': "Show list of commands",
                 '//eject_device': "Eject a peripheral off the computer",
                 '//update': "Update the current OS",
                 '//operations': "Perform simple operations",
                 '//mem_add': "Add value to memory",
                 '//mem': "View memory",
                 '//mem_del': "Remove item from memory",
                 '//mem_clear': "Delete all of memory",
                 '//time': "Show current time",}
        for i in comms:
            print(f"{i}: {comms[i]}\n")
        if self.ctrl == True:
            if self.ctrl == True:
                self.ask()

    def recharge(self): # recharge the computer
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Current battery percentage: {self.battery}")
        choice = input("Confirm recharge?")
        print("Recharging...")
        if choice.lower() == 'yes':
            while self.battery < 100:
                self.battery += 1
                print(f"Current battery status: {self.battery}")
                sleep(1)
            if self.ctrl == True:
                if self.ctrl == True:
                    print("Recharge complete")
                    self.ask()
        elif choice.lower() == 'no':
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        else:
            print("Invalid input")
            if self.ctrl == True:
                self.ask()

    def close(self): # shut down the computer
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"{self.name} is shutting down...")
        save(self.file, self.memory, '-')
        exited(self.name)
        exit()
    def full_setup(self):
        self.boot()
        self.control()

    def connect_dev(self): # connect a device
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        devices = [
            "Keyboard",
            "Mouse",
            "Printer",
            "Monitor",
            "External hard drive",
            "USB",
            "Webcam",
            "Microphone",
            "Speakers",
            "Phone",
            "Tablet",
            "USB hub",
        ]
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        if self.dev == self.max_dev:
            print(f"MESSAGE FROM {self.name}: Maximum connected peripherals reached.")
            if self.ctrl == True:
                self.ask()
        else:
            dev = input("Select device to connect:\n")
            if dev in devices:
                self.dev += 1
                print(f"{dev} connected successfully to {self.name}")
                self.battery -= 1
                if self.ctrl == True:
                    self.ask()
            else:
                print(f"Could not connect {dev} device.")
                if self.ctrl == True:
                    self.ask()
    def eject_device(self): # eject a device
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        devices = [
            "Keyboard",
            "Mouse",
            "Printer",
            "Monitor",
            "External hard drive",
            "USB",
            "Webcam",
            "Microphone",
            "Speakers",
            "Phone",
            "Tablet",
            "USB hub",
        ]
        if self.dev == 0:
            print(f"No device connected to {self.name}")
            if self.ctrl == True:
                self.ask()
        dev = input("Select device to eject:\n")
        if dev in devices:
            print(f"Ejecting {dev} device...")
            sleep(self.wait)
            self.dev -= 1
            self.battery -= 2
            print(f"{dev} device ejected successfully")
            if self.ctrl == True:
                self.ask()

    def update(self): # change the OS
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        OSes = ['SolarisOS',
                'HyperOS',
                'NexusOS',
                'CerberOS',
                'HorizonOS',
                'NovaOS',
                'MacOS',
                'AuroraOS',
                'GalaxyOS',
                'ChronosOS',
                'QuantumOS',
                'PhoenixOS']
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Current OS in use: {self.OS}")
        for i in OSes:
            print(i)
        choice = input(f"Select OS to use:")
        if choice in OSes:
            if choice != self.OS:
                print("Rebooting...")
                sleep(self.wait)
                self.OS = choice
                print(f"OS updated to {self.OS}")
                self.battery -= 5
                if self.ctrl == True:
                    self.ask()
            elif choice == self.OS:
                print(f"OS {choice} already in use")
                if self.ctrl == True:
                    self.ask()
        else:
            print(f"OS {choice} not found")
            if self.ctrl == True:
                self.ask()



    def check_self(self): # displays system status
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}:\n"
              f"Computer name: {self.name}\n"
              f"RAM size: {self.ram_size}\n"
              f"ROM Size: {self.memory_size} GB\n"
              f"OS name: {self.OS}\n"
              f"Processor speed: {self.speed} Mhz\n"
              f"Current battery percentage: {self.battery}. "
              f"Estimated time for full recharge: {100 - self.battery} seconds\n"
              f"Connected devices: {self.dev}\n"
              f"Maximum devices {self.name} can handle: {self.max_dev}\n")
        self.battery -= 1
        if self.ctrl == True:
            self.ask()

    def control(self): # gain access to commands
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        # make sure this is always the last one of all methods
        print(f"GRANTING ACCESS TO {self.name}...")
        sleep(self.wait)
        print(f"ACCESS GRANTED")
        print(f"MESSAGE FROM {self.name}: Opening control terminal...")
        sleep(self.wait)
        print("Terminal unlocked")
        self.battery -= 5
        self.ctrl = True
        if self.ctrl == True:
            self.ask()



# Computer('Titan', 40, 16, 'AuroraOS', 350, 4, 100, file) an example