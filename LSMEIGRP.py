# $language = "python"
# $interface = "1.0"
from DDSMGlobal import eigrp


def configt():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("Router(config)#")


def main(eigrpip):
    for x in eigrpip:
        crt.Screen.Send("router eigrp " + eigrp + "\n")
        crt.Screen.WaitForString("Router(config-router)#")
        crt.Screen.Send("network " + x + "\n")
        crt.Screen.WaitForString("Router(config-router)#")
        crt.Screen.Send("no auto-summary \n")


main(DDSMGlobal.leigrpip)


def end():
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("write mem \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("exit \n")


end()

