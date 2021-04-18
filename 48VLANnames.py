
configt()


def main():
    for x, y in zip(DDSMGlobal.lvlan, DDSMGlobal.lname):
        keyboard.type("vlan " + x + "\n")
        keyboard.type("name " + y + "\n")


main()


end()
