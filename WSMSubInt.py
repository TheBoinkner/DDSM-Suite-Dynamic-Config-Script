# $language = "python"
# $interface = "1.0"

import DDSMGlobal


def configt():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("Router(config)#")


configt()


def main():
    for [x, y] in [DDSMGlobal.wvlan, DDSMGlobal.wdefgate]:
        crt.Screen.Send("int " + DDSMGlobal.port + x + "\n")
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
