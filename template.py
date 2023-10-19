menu = """
1 - OSPF ingeven
2 - STATIC ingeven
3 - Template aanmaken
4 - Script stoppen
"""
while_bool = True
my_static = ""
my_ospf = ""

# Functie voor het opvragen van de statische route
def create_static():
    try:
        print("Er word een default route aangemaakt")
        next_hop = str(input("Geef hier de next hop in voor de default route: "))
    except ValueError:
        print("Fout invoer")
    finally:
        return next_hop


# Functie voor het opvragen van de OSPF netwerken
def create_ospf():
    try:
        aantal_networks = int(input("Hoeveel netwerken wil je toevoegen aan OSPF?: "))
        networks_overview = []
        # while loop voor het herhalen van hoeveel keer ze een netwerk willen toevoegen
        while aantal_networks > 0:
            network_adress = (input("Gelieve een netwerkadres in te geven: "))
            network_mask = (input("Gelive een netmask in te geven: "))
            networks_overview.append(dict({network_adress.strip(): network_mask.strip()}))
            aantal_networks -= 1
    except ValueError:
        print("Foute invoer")

    finally:
            return networks_overview

# Functie voor de final template, alle commando's weergeven
def create_template(a, b):
    try:
        # print static template Cisco
        print("Static template voor Cisco\n" + "============================\n" + f"ip route 0.0.0.0 0.0.0.0 {a}\n")
        # print static template Huawei
        print("Static template voor Huawei\n" + "============================\n" + f"ip route-static 0.0.0.0 0.0.0.0 {a}\n")

        # print OSPF template Cisco
        print("OSPF template voor Cisco\n" + "============================\n")
        print("router ospf 1\n")
        for citem in b:
            print(f"network {citem.keys()} {citem.values()} area 0\n")

        # print OSPF template Huawei
        print("OSPF template voor Huawei\n" + "============================\n")
        print("ospf 1\n")
        for hitem in b:
            print(f"area 0 {hitem.keys()} {hitem.values()}")


    except ValueError:
        print("Geen values")

# Logica voor het weergeven van de menu en de juiste functie op te roepen

while while_bool:
    print(menu)
    keuze = str(input("Geef een keuze door een cijfer in te vullen: "))
    if keuze == "1":
        my_static = create_static()
        while len(my_static.strip()) == 0:
            my_static = create_static()
    elif keuze == "2":
        my_ospf = create_ospf()
    elif keuze == "3":
        create_template(my_static, my_ospf)
    elif keuze == "4":
        print("Het programma wordt afgesloten!")
        while_bool = False
    else:
        print("!" * 30)
        print("Foute invoer, probeer opnieuw")
        print("!" * 30)

