from Computers import Computer

comp_list = ['Aphrodite',
             'Helix',
             'Titan',
             'Pulse',
             'Quantum',
             'Stellar',
             'Core',
             'Infinity',
             'HyperFlex',
             'Solar',]
def ask():
    for i in comp_list:
        print(i)
    choice = input("Select computer to use:\n")
    if choice.title() in comp_list:
        if choice.lower() == 'aphrodite':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Aphrodite',
                                   3050,
                                   8,
                                   'PhoenixOS',
                                   150,
                                   10,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'helix':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Helix',
                                   2024,
                                   32,
                                   'PhoenixOS',
                                   350,
                                   2,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'titan':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Titan',
                                   8000,
                                   16,
                                   'AuroraOS',
                                   350,
                                   4,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'pulse':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Pulse',
                                   2000,
                                   32,
                                   'PulseOS',
                                   350,
                                   12,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'quantum':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Quantum',
                                   1000,
                                   3500,
                                   'QuantumOS',
                                   3500,
                                   4,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'stellar':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Stellar',
                                   100,
                                   5500,
                                   'GalaxyOS',
                                   3700,
                                   7,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'core':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Core',
                                   550,
                                   5300,
                                   'ChronosOS',
                                   3300,
                                   1,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'infinity':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Infinity',
                                   750,
                                   7000,
                                   'NovaOS',
                                   5500,
                                   4,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'hyperflex':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('HyperFlex',
                                   670,
                                   8000,
                                   'PixelOS',
                                   6000,
                                   4,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif choice.lower() == 'solar':
            file = input("Select save to associate this computer with (1, 2, 3):\n")
            if int(file) < 4 and int(file) > 0:
                file = f'Mem_{file}.txt'
            my_computer = Computer('Solar',
                                   570,
                                   7800,
                                   'SolarisOS',
                                   5600,
                                   3,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
print("Here are some ready computer models, just for you")
print("More are coming soon ;)")
ask()