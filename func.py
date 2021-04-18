# $language = "python"
# $interface = "1.0"

# Enter config
def configt():
    keyboard.type("\n")
    keyboard.type("enable\n")
    keyboard.type("config t\n")


configt()


# Access the Switch
def nme():
    keyboard.type("\nenable\n")
    keyboard.type("service-module g2/0 session\n")
    keyboard.type("no\n")


nme()


# go to config in the nme
def configtnme():
    keyboard.type("\n")
    keyboard.type("enable\n")
    keyboard.type("config t\n")


configtnme()


# Exits out and saves running configs
def end():
    keyboard.type("exit\nexit\n")
    keyboard.type("write mem\n")
    keyboard.type("exit\n")


end()


# Exits out of NME and saves running configs
def back():
    from time import sleep
    keyboard.type("end\nexit\n\n")
    keyboard.type(chr(30) + "xdisconnect\n\n")
    keyboard.type("write mem\n")
    sleep(5)


back()
