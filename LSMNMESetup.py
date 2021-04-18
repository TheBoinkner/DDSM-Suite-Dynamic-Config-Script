# $language = "python"
# $interface = "1.0"


def configt():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("Router(config)#")


def main():
    crt.Screen.Send("int g2/0 \n")
    crt.Screen.WaitForString("Router(config-if)#")
    crt.Screen.Send("ip add 1.1.1.1 255.255.255.0 \n")
    crt.Screen.WaitForString("Router(config-if)#")
    crt.Screen.Send("no shut \n")
    crt.Screen.WaitForString("Router(config-if)#")
    crt.Screen.Send("line 131 \n")
    crt.Screen.WaitForString("Router(config-line)#")
    crt.Screen.Send("transport input all \n")
    crt.Screen.WaitForString("Router(config-line)#")
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router(config)#")
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("write mem \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("exit \n")


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
