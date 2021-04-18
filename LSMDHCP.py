# $language = "python"
# $interface = "1.0"
from DDSMGlobal import ldefgate, leigrpip
dhcp_name = ["users", "voice"]


def configt():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("Router(config)#")


def dhcp():
    for x, y, z in zip(dhcp_name, ldefgate, leigrpip):
        crt.Screen.Send("ip dhcp pool" + x + "\n")
        crt.Screen.WaitForString("#")
        crt.Screen.Send("default-router" + y + "\n")
        crt.Screen.WaitForString("#")
        crt.Screen.Send("network" + z + "\n")
        crt.Screen.WaitForString("#")


dhcp()


def end():
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("write mem \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("exit \n")


end()
