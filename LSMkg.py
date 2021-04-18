# $language = "python"
# $interface = "1.0"
from DDSMGlobal import kg


def configt():
    crt.Screen.Synchronous = True
    crt.Screen.Send("\n")
    crt.Screen.Send("enable \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("config t \n")
    crt.Screen.WaitForString("Router(config)#")


def kg():
    crt.Screen.Send("int g0/0 \n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("ip add " + kg + "\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("no shut \n")
    crt.Screen.WaitForString("#")


kg()


def end():
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("exit \n")
    crt.Screen.WaitForString("Router")
    crt.Screen.Send("write mem \n")
    crt.Screen.WaitForString("Router#")
    crt.Screen.Send("exit \n")


end()

