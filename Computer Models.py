from Computers import *
def ask():
    for i in comp_list:
        print(i)
    choice = input("Select a computer model:\n")
    if choice == 'Aphrodite':
        print("Aphrodite: This computer is designed to handle a lot of devices and act like a Super-Hub")
        yn = input("Confirm choice (y/n) ?\n")
        if yn == 'y':
            file = input("Select save to associate this computer with (Mem_1.txt, Mem_2.txt, Mem_3.txt Case sensitive):\n")
            my_computer = Computer('Aphrodite',
                                   30,
                                   8,
                                   'PhoenixOS',
                                   150,
                                   10, 100,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif yn == 'n':
            ask()
    elif choice == 'Helix':
        print("Helix: This computer is specifically designed to perform complex operations in seconds")
        yn = input("Confirm choice (y/n) ?\n")
        if yn == 'y':
            file = input(
                "Select save to associate this computer with (Mem_1.txt, Mem_2.txt, Mem_3.txt Case sensitive):\n")
            my_computer = Computer('Helix',
                                   20,
                                   32,
                                   'PhoenixOS',
                                   350,
                                   2,
                                   100,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif yn == 'n':
            ask()
    elif choice == 'Titan':
        print("Titan: This computer, as it's name suggests,can store enormous amounts of data")
        yn = input("Confirm choice (y/n) ?\n")
        if yn == 'y':
            file = input("Select save to associate this computer with (Mem_1.txt, Mem_2.txt, Mem_3.txt Case sensitive):\n")
            my_computer = Computer('Titan',
                                   40,
                                   16,
                                   'AuroraOS',
                                   350,
                                   4,
                                   100,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif yn == 'n':
            ask()
    elif choice == 'Pulse':
        print("Pulse: Specifically made for scientific operations. It has it's own, unique OS")
        yn = input("Confirm choice (y/n) ?\n")
        if yn == 'y':
            file = input("Select save to associate this computer with (Mem_1.txt, Mem_2.txt, Mem_3.txt Case sensitive):\n")
            my_computer = Computer('Pulse',
                                   20,
                                   32,
                                   'PulseOS',
                                   350,
                                   12,
                                   100,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif yn == 'n':
            ask()
    elif choice == 'DF':
        print("DF: The most basic computer, jack of all trades")
        yn = input("Confirm choice (y/n) ?\n")
        if yn == 'y':
            file = input("Select save to associate this computer with (Mem_1.txt, Mem_2.txt, Mem_3.txt Case sensitive):\n")
            my_computer = Computer('Default',
                                   30,
                                   4,
                                   'AuroraOS',
                                   150,
                                   5,
                                   100,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif yn == 'n':
            ask()
    elif choice == '3n1gm4':
        print("A broken computer, with outdated peripherals and OS. Needs repair")
        yn = input("Confirm choice (y/n) ?\n")
        if yn == 'y':
            file = input("Select save to associate this computer with (Mem_1.txt, Mem_2.txt, Mem_3.txt Case sensitive):\n")
            my_computer = Computer('3n1gm4',
                                   10,
                                   4,
                                   'EnigmaOS',
                                   50,
                                   2,
                                   25,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif yn == 'n':
            ask()
    elif choice == 'OP':
        print("Pretty self explanatory")
        yn = input("Confirm choice (y/n) ?\n")
        if yn == 'y':
            file = input("Select save to associate this computer with (Mem_1.txt, Mem_2.txt, Mem_3.txt Case sensitive):\n")
            my_computer = Computer('OP',
                                   1000,
                                   4000,
                                   'OPOS',
                                   5000,
                                   22,
                                   100,
                                   file)
            print("Your computer is ready to go!")
            my_computer.full_setup()
        elif yn == 'n':
            ask()
comp_list = ['Aphrodite', 'Helix', 'Titan', 'Pulse', 'DF', '3n1gm4', 'OP']
print("Here are some ready computer models, just for you")
print("More are coming soon")
ask()
