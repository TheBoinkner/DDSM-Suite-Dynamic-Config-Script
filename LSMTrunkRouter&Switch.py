# $language = "python"
# $interface = "1.0"


def configt():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("Router(config)#")


def switch():
    crt.Screen.Send("int g0/1" + "\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("switchport trunk encapsulation dot1q" + "\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("switchport mode trunk" + "\n")
    crt.Screen.WaitForString("#")


switch()


def router():
    crt.Screen.Send("int g0/26" + "\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("switchport trunk encapsulation dot1q" + "\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("switchport mode trunk" + "\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("switchport trunk allow vlan 5,30,35,40,45,")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("no shut")


router()


def end():
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("write mem \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("exit \n")


end()
