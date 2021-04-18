configt()


def main():
    keyboard.type("int g0/1/" + trunk + "\n")
    keyboard.type("switchport mode trunk \n")
    keyboard.type("int range g1/0/" + portrange + "\n")
    keyboard.type("switchport mode access \n")
    keyboard.type("switchport access vlan 30 \n")
    keyboard.type("switchport voice vlan 40 \n")


main()


end()
