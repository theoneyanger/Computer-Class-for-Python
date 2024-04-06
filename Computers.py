from time import *
from ELP import * # writes into 'Logs.txt' whenever user opens or closes the program
from Calculator import * # for operations
from Saver_Loader import * # saves/loads data into files
from Val_Corrector import * # corrects values e.g. '4' -> 4
from datetime import datetime
from NET import net # NET functions for sharing data across programs
class Computer:
    """ Simulate a computer. Following features included:
    Conversion of text to commands using Horizon
    Memory storage
    Device connection/disconnection
    Calculations
    Diversity between each OS
    And more!"""
    def __init__(self, name, mem_size, ram_size, OS, processor_speed, dev, filename):
        self.hub = net() # connection to the net (data exchange between programs)
        self.name = name # the name of the computer
        self.file = filename # file for the memory to be stored at
        self.memory_size = mem_size # the maximum memory capacity
        self.ram_size = ram_size #useful for determining load speed
        self.horizon_enabled = False
        self.OS = OS # the OS
        self.heat = 20.0
        self.speed = processor_speed # the rest is up to you to figure out
        self.wait = 0
        if int(self.speed) <= 50:
            self.wait = 10
        elif self.speed >= 100 and self.speed <= 150:
            self.wait = 8
        elif self.speed >= 150 and self.speed <= 300:
            self.wait = 5
        elif self.wait >= 300 and self.wait <= 350:
            self.wait = 3
        self.wait -= self.ram_size / 2
        if self.wait <= 0:
            self.wait = 0.1


        self.max_dev = dev
        self.dev = 0
        self.ports = {}
        for i in range(self.max_dev + 1):
            self.ports.update({i: 'None'})
        self.battery = 100
        self.powered = False
        self.ctrl = False
        if self.battery > 100:
            self.battery = 100
        self.memory = []
        self.max_ram = self.ram_size + 12
        self.max_rom = self.memory_size + 2200
        self.max_proc = self.speed + 100

        if self.OS == 'AuroraOS':
            self.symbol = '!'
            self.ai_name = 'Synth'
        elif self.OS == 'PhoenixOS':
            self.symbol = '>'
            self.ai_name = 'Sentinel'
        elif self.OS == 'PixelOS':
            self.ai_name = 'Omega'
            self.symbol = '*'
        elif self.OS == 'PulseOS':
            self.symbol = '?'
            self.ai_name = 'Cipher'
        elif self.OS == 'QuantumOS':
            self.symbol = '>>'
            self.ai_name = 'Nexus'
        elif self.OS == 'SolarisOS':
            self.symbol = '//'
            self.ai_name = 'Echo'
        elif self.OS == 'NovaOS':
            self.symbol = '#'
            self.ai_name = 'Aegis'
        elif self.OS == 'HorizonOS':
            self.symbol = '$'
            self.ai_name = 'Matrix'
        elif self.OS == 'ChronosOS':
            self.symbol = ';'
            self.ai_name = 'Genesis'
        elif self.OS == 'GalaxyOS':
            self.symbol = '~'
            self.ai_name = 'Oracle'
        elif self.OS == 'EnigmaOS':
            self.symbol = '%'
            self.ai_name = 'Enigma'
        else:
            self.symbol = '/'
            self.ai_name = 'AI'

    def ask(self): # enter a command
        self.heat += 0.7
        if self.OS == 'AuroraOS':
            self.symbol = '!'
            self.ai_name = 'Synth'
        elif self.OS == 'PhoenixOS':
            self.symbol = '>'
            self.ai_name = 'Sentinel'
        elif self.OS == 'PixelOS':
            self.ai_name = 'Omega'
            self.symbol = '*'
        elif self.OS == 'PulseOS':
            self.symbol = '?'
            self.ai_name = 'Cipher'
        elif self.OS == 'QuantumOS':
            self.symbol = '>>'
            self.ai_name = 'Nexus'
        elif self.OS == 'SolarisOS':
            self.symbol = '//'
            self.ai_name = 'Echo'
        elif self.OS == 'NovaOS':
            self.symbol = '#'
            self.ai_name = 'Aegis'
        elif self.OS == 'HorizonOS':
            self.symbol = '$'
            self.ai_name = 'Matrix'
        elif self.OS == 'ChronosOS':
            self.symbol = ';'
            self.ai_name = 'Genesis'
        elif self.OS == 'GalaxyOS':
            self.symbol = '~'
            self.ai_name = 'Oracle'
        elif self.OS == 'EnigmaOS':
            self.symbol = '%'
            self.ai_name = 'Enigma'
        else:
            self.symbol = '/'
            self.ai_name = 'AI'

            print(f"Battery status: {self.battery}%\n"
                  f"Computer temperature: {self.heat}°C")
            if self.heat > 30:
                print(f"MESSAGE FROM {self.name}: Urgent cooldown required. Bypassing controls...")
                self.cool()
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        if self.ctrl == False:
            print(f"MESSAGE FROM {self.name}: Access not granted.")
        else:
            # start of Horizon algorithm START
            # it basically detects keywords
            if self.horizon_enabled == True:
                text = input(f"MESSAGE FROM {self.ai_name}: What would you like to do?\n")
                if ('show' in text.lower() or 'view'  in text.lower()) and 'commands' in text.lower():
                    self.help()

                elif 'connect' in text.lower() and 'net' in text.lower():
                    self.hub.connect(False)

                elif 'request' in text.lower() and 'id' in text.lower():
                    self.hub.request()

                elif 'send' in text.lower() and 'data' in text.lower() and 'net' in text.lower():
                    self.hub.send()

                elif ('retrieve' in text.lower() or 'get' in text.lower()) and 'data' in text.lower() and 'net' in text.lower():
                    self.hub.retrieve()

                elif 'recharge' in text.lower():
                    self.recharge()

                elif ('shut' in text.lower() or 'close' in text.lower()) and 'computer' in text.lower():
                    self.close()

                elif 'connect' in text.lower() and 'device' in text.lower():
                    self.connect_dev()

                elif 'disconnect' in text.lower() and 'net' in text.lower():
                    self.disconnect()

                elif 'view' in text.lower() and 'devices' in text.lower():
                    self.devices()

                elif ('disconnect' in text.lower() or 'eject' in text.lower()) and 'device' in text.lower():
                    self.eject_device()

                elif 'system' in text.lower() and 'check' in text.lower():
                    self.check_self()

                elif ('update' in text.lower() or 'change' in text.lower()) and ('os' in text.lower() or 'operating system' in text.lower()):
                    self.update()

                elif 'perform' in text.lower() and ('calculations' in text.lower() or 'operations' in text.lower()):
                    self.operations()

                elif ('view' in text.lower() or 'show' in text.lower()) and 'memory' in text.lower():
                    self.mem()

                elif 'add' in text.lower() and 'memory' in text.lower():
                    self.mem_add()

                elif 'remove' in text.lower() and 'memory' in text.lower():
                    self.mem_del()

                elif ('clear' in text.lower() or 'delete' in text.lower()) and 'memory' in text.lower():
                    self.mem_clear()

                elif ('show' in text.lower() or 'view' in text.lower()) and 'time' in text.lower():
                    self.time()

                elif ('replace' in text.lower() or 'change' in text.lower()) and 'part' in text.lower() and 'computer' in text.lower():
                    self.replace()

                elif 'cool' in text.lower() and 'computer' in text.lower():
                    self.cool()

                elif 'load' in text.lower() and 'memory' in text.lower() and 'file' in text.lower():
                    self.mem_load()



                elif ('deactivate' in text.lower() or 'close' in text.lower() or 'shut' in text.lower()) and ('copilot' in text.lower() or 'you' in text.lower() or 'yourself' in text.lower() or 'copilot' in text.lower()):
                    choice = input("You really want to deactivate me...?")
                    if choice.lower() == 'y':
                        choice = input("You can't be serious...")
                        if choice.lower() == 'y':
                            print("OK, I guess. It's not like I'm sentient or anything")
                            sleep(3)
                            self.horizon_enabled = False
                            self.ask()
                        else:
                            print("I knew you'd change your mind!")
                            self.ask()
                    else:
                        print("Phew! I was worried there")
                        if self.ctrl == True:
                            self.ask()

                else:
                    print("Could not understand command")
                    self.ask()

                # end of Horizon algorithm END

            print(f"Use '{self.symbol}help' for list of commands")
            comm = input(f"Select action for {self.name}:\n")
            if comm == str(self.symbol) + 'help':
                self.help()
            elif comm == str(self.symbol) + 'recharge':
                self.recharge()
            elif comm == str(self.symbol) + 'close':
                self.close()
            elif comm == str(self.symbol) + 'connect_device':
                self.connect_dev()
            elif comm == str(self.symbol) + 'system_check':
                self.check_self()
            elif comm == str(self.symbol) + 'update':
                self.update()
            elif comm == str(self.symbol) + 'help':
                self.help()
            elif comm == str(self.symbol) + 'eject_device':
                self.eject_device()
            elif comm == str(self.symbol) + 'operations':
                self.operations()
            elif comm == str(self.symbol) + 'insta_charge':
                self.insta_charge()
            elif comm == str(self.symbol) + 'mem_add':
                self.mem_add()
            elif comm == str(self.symbol) + 'mem':
                self.mem()
            elif comm == str(self.symbol) + 'mem_del':
                self.mem_del()
            elif comm == str(self.symbol) + 'mem_clear':
                self.mem_clear()
            elif comm == str(self.symbol) + 'time':
                self.time()
            elif comm == str(self.symbol) + 'devices':
                self.devices()
            elif comm == str(self.symbol) + 'request':
                self.request()
            elif comm == str(self.symbol) + 'connect':
                self.connect()
            elif comm == str(self.symbol) + 'send':
                self.send()
            elif comm == str(self.symbol) + 'get':
                self.retrieve()
            elif comm == str(self.symbol) + 'copilot_activate':
                self.Horizon()
            elif comm == str(self.symbol) + 'disconnect':
                self.disconnect()
            elif comm == str(self.symbol) + 'fast_connect':
                self.fast_connect()
            elif comm == str(self.symbol) + 'cool':
                self.cool()
            elif comm == str(self.symbol) + 'mem_load':
                self.mem_load()
            elif comm == str(self.symbol) + 'replace':
                self.replace()
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

    def Horizon(self): # enable the AI
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"{self.ai_name.title()} is made so it can understand normal text and translate it into commands")
        choice = input("Enable Copilot?(y/n)\n")
        if choice.lower() == 'y':
            print(f"Enabling {self.ai_name.title()}...")
            sleep(self.wait + 3)
            self.battery -= 10
            self.horizon_enabled = True
        if self.ctrl == True:
            self.ask()

    def replace(self): # change a tool in the computer
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        choice = input(f"MESSAGE FROM {self.name}: Select part to replace:\n1.RAM\n2.ROM\n3.Processor")
        if choice.lower() == 'ram' or int(choice) == 1:
            val = int(input("Select new value for RAM:\n"))
            if int(val) < self.max_ram:
                print(f"RAM updated from {self.ram_size} to {val}")
                self.ram_size = val
                if self.ctrl == True:
                    self.ask()
            else:
                print(f"Cannot assign ram value higher than {self.max_ram}")
                if self.ctrl == True:
                    self.ask()

        elif choice.lower() == 'rom' or int(choice) == 2:
            val = input("Select new value for ROM:\n")
            if int(val) < self.max_rom:
                print(f"ROM updated from {self.memory_size} to {val}")
                self.memory_size = val
                if self.ctrl == True:
                    self.ask()
            else:
                print(f"Cannot assign rom value higher than {self.max_rom}")
                if self.ctrl == True:
                    self.ask()

        elif choice.lower() == 'processor' or int(choice) == 3:
            val = input("Select new value for the processor speed:\n")
            if int(val) < self.max_proc:
                print(f"Processor speed updated from {self.speed} to {val}")
                self.speed = val
                if self.ctrl == True:
                    self.ask()
            else:
                print(f"Cannot assign processor speed higher than {self.max_proc}")
                if self.ctrl == True:
                    self.ask()
        else:
            print(f"Could not identify tool {choice} in computer")
            if self.ctrl == True:
                self.ask()

    def mem_load(self): # load memory from the save file
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Loading memory from {self.file}...")
        load(self.file, '-')
        print(f"Memory loaded: {self.memory}")
        if self.ctrl == True:
            self.ask()

    def cool(self): # reduce temperature
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Current computer temperature: {self.heat}°C")
        choice = input("Cool down computer? (y/n)\n")
        if choice.lower() == 'y':
            while self.heat > 20:
                self.heat -= 1
                print(round(self.heat))
                sleep(1)
            print("Computer temperature cooled down to 20°C")
            if self.ctrl == True:
                self.ask()
        else:
            if self.ctrl == True:
                self.ask()

    def request(self): # request an ID for connection to the NET
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        self.hub.request()
        self.battery -= 1
        if self.ctrl == True:
            self.ask()

    def send(self): # send data to the NET
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        self.hub.send()
        self.battery -= 3
        if self.ctrl == True:
            self.ask()

    def connect(self): # connect to the NET
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        self.hub.connect(False)
        self.battery -= 8
        if self.ctrl == True:
            self.ask()

    def fast_connect(self): # secret command, does not require an ID
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        self.hub.connect(True)
        if self.ctrl == True:
            self.ask()

    def disconnect(self): # disconnect from the NET
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        self.hub.disconnect()
        self.battery -= 4
        if self.ctrl == True:
            self.ask()


    def retrieve(self): # get data from the NET
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        self.hub.retrieve()
        self.battery -= 3
        if self.ctrl == True:
            self.ask()

    def mem_clear(self): # clear all memory
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Deleting memory...")
        sleep(self.wait)
        self.memory.clear()
        self.battery -= 1
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
        self.battery -= 1
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

    def mem_add(self): # add value to memory
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        if len(self.memory) == self.memory_size:
            print("Memory has reached maximum capacity. Cannot add value to memory")
            self.ask()
        val = input(f"MESSAGE FROM {self.name}: Enter value to add to memory:\n")
        self.memory.append(corrector(val))
        print(f"Memory {val} added. Remaining storage {self.memory_size - len(self.memory)}")
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
            print(f"Result: {add(a, b)}")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        elif choice.lower() == 'subtraction':
            self.battery -= 2
            sleep(self.wait)
            print(f"Result: {sub(a, b)}")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        elif choice.lower() == 'multiplication':
            self.battery -= 2
            sleep(self.wait)
            print(f"Result: {mult(a, b)}")
            if self.ctrl == True:
                if self.ctrl == True:
                    self.ask()
        elif choice.lower() == 'division':
            self.battery -= 2
            sleep(self.wait)
            print(f"Result: {div(a, b)}")
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
        cop = f'Activate your copilot{self.ai_name.title()}'
        commands = {str(self.symbol) + 'recharge': "Recharge the computer's battery",
                 str(self.symbol) + 'close': "Shut down the computer",
                 str(self.symbol) + 'connect_device': "Connect a peripheral to the computer",
                 str(self.symbol) + 'system_check': "Get a report on the computer's status",
                 str(self.symbol) + 'help': "Show list of commands",
                 str(self.symbol) + 'eject_device': "Eject a peripheral off the computer",
                 str(self.symbol) + 'update': "Update the current OS",
                 str(self.symbol) + 'operations': "Perform simple operations",
                 str(self.symbol) + 'mem_add': "Add value to memory",
                 str(self.symbol) + 'mem': "View memory",
                 str(self.symbol) + 'mem_del': "Remove item from memory",
                 str(self.symbol) + 'mem_clear': "Delete all of memory",
                 str(self.symbol) + 'time': "Show current time",
                 str(self.symbol) + 'devices': "Show devices connected",
                 str(self.symbol) + 'request': "Request an ID for connection to th NET",
                 str(self.symbol) + 'connect': "Connect to the NET",
                 str(self.symbol) + 'send': "Send data to the NET",
                 str(self.symbol) + 'get': 'Retrieve data from the NET',
                 str(self.symbol) + 'copilot_activate': cop,
                 str(self.symbol) + 'disconnect': "Disconnect your device from the NET",
                 str(self.symbol) + 'cool': "Cool down the computer",
                 str(self.symbol) + 'mem_load': "Load memory from the save file",
                 str(self.symbol) + 'replace': "Replace a tool in the computer",
                }
        for i in commands:
            print(f"{i}: {commands[i]}\n")
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
        if choice.lower() == 'yes' or choice.lower() == 'y':
            while self.battery < 100:
                self.battery += 1
                print(f"Current battery status: {self.battery}")
                sleep(1)
            if self.ctrl == True:
                if self.ctrl == True:
                    print("Recharge complete")
                    self.ask()
        elif choice.lower() == 'no' or choice.lower() == 'n':
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
        sleep(5)
        exited(self.name)
        exit()
    def full_setup(self): # quicker set up
        self.boot()
        self.control()

    def connect_dev(self): # connect a device
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        if self.dev == self.max_dev:
            print(f"MESSAGE FROM {self.name}: Maximum connected peripherals reached.")
            if self.ctrl == True:
                self.ask()
        else:
            for i in self.ports:
                print(f"Port {i}: {self.ports[i]}\n")
            dev = input("Select device to connect:\n")
            port = int(input(f"Select port to connect {dev} to:\n"))

            if self.ports[port] != 'None':
                print(f"Port {port} already occupied")
                if self.ctrl == True:
                    self.ask()
            self.dev += 1
            self.ports.update({port: dev})
            print(f"{dev} connected successfully to {self.name} at port {port}")
            self.battery -= 3
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
        if self.dev == 0:
            print(f"No device connected to {self.name}")
            if self.ctrl == True:
                self.ask()
        for i in self.ports:
            print(f"Port {i}: {self.ports[i]}\n")
        port = int(input("Select port to eject device from:\n"))
        dev = self.ports[port]
        if self.ports[port] == 'None':
            print(f"No device connected to port {port}")
            if self.ctrl == True:
                self.ask()
        print("Ejecting device...")
        sleep(self.wait)
        self.dev -= 1
        self.ports[port] = 'None'
        self.battery -= 2
        print(f"{dev} device ejected successfully from port {port}")
        if self.ctrl == True:
            self.ask()

    def devices(self):
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Showing devices...")
        for i in self.ports:
            print(f"{i}: {self.ports[i]}")
        if self.ctrl == True:
            self.ask()

    def update(self): # change the OS
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        OSes = ['SolarisOS',
                'HorizonOS',
                'NovaOS',
                'AuroraOS',
                'GalaxyOS',
                'ChronosOS',
                'QuantumOS',
                'PhoenixOS']
        SecretOSes = ['PixelOS', # secret, non visible OSes
                      'PulseOS',
                      'EnigmaOS']
        if self.powered == False:
            print(f"{self.name} is not powered")
            sleep(3)
            exit()
        print(f"MESSAGE FROM {self.name}: Current OS in use: {self.OS}")
        for i in OSes:
            print(i)
        choice = input(f"Select OS to use:")
        if choice in OSes or choice in SecretOSes:
            if choice != self.OS:
                print("Rebooting...")
                sleep(self.wait + 3)
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
              f"RAM size: {self.ram_size} KB\n"
              f"ROM Size: {self.memory_size} KB\n"
              f"OS name: {self.OS}\n"
              f"Processor speed: {self.speed} hz\n"
              f"Current battery percentage: {self.battery}. "
              f"Estimated time for full recharge: {100 - self.battery} seconds\n"
              f"Connected devices: {self.dev}\n"
              f"Maximum devices {self.name} can handle: {self.max_dev}\n"
              f"Current temperature: {round(self.heat)}°C\n")
        self.battery -= 2
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

if __name__ == '__main__':
    my_computer = Computer('Pulse',
                           2000,
                           32,
                           'PulseOS',
                           350,
                           12,
                           'Mem_2.txt')

    my_computer.full_setup()