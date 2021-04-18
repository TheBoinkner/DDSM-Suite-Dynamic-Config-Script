# $language = "python"
# $interface = "1.0"
def nme():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("service-module g2/0 session \n")
    crt.Screen.WaitForString("Would you like to enter the initial configuration dialog? [yes/no]: ")
    crt.Screen.Send("no \n")
    crt.Screen.WaitForString("Switch>")


nme()


def configtnme():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("(config)#")


configtnme()


def main():
    crt.Screen.Send("int" + "g0/26" + "\n")
    crt.Screen.WaitForString("(config-if)")
    crt.Screen.Send("switchport trunk encapsulation dot1q" + "\n")
    crt.Screen.WaitForString("(config-if)")
    crt.Screen.Send("switchport mode trunk" + "\n")
    crt.Screen.WaitForString("(config-if)")


main()


def kg():
    crt.Screen.Send("int g0/1")
    crt.Screen.WaitForString("(config-if)")   
    crt.Screen.Send("switchport mode access")
    crt.Screen.WaitForString("(config-if)")
    crt.Screen.Send("switchport access vlan 5")
    crt.Screen.WaitForString("(config-if)")


kg()


def back():
    crt.Screen.Send("exit \n")
    crt.Screen.Send("exit \n \n")
    crt.Screen.Send(chr(30) + "x disconnect \n")
    crt.Screen.WaitForString("[confirm]")
    crt.Screen.Send("\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("write mem \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("exit \n")


back()
