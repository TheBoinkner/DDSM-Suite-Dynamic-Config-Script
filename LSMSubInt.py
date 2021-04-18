# $language = "python"
# $interface = "1.0"
from DDSMGlobal import lvlan, ldefgate, port


def configt():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("Router(config)#")


def main():
    for [x, y] in [lvlan, ldefgate]:
        crt.Screen.Send("int " + port + x + "\n")
        crt.Screen.WaitForString("Router(config-subif)#")
        crt.Screen.Send("encapsulation dot1q " + x + "\n")
        crt.Screen.WaitForString("Router(config-subif)#")
        crt.Screen.Send("ip add " + y + "\n")
        crt.Screen.WaitForString("Router(config-subif)#")


main()


def end():
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("write mem \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("exit \n")


end()
