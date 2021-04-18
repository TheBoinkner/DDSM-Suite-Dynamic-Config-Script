# $language = "python"
# $interface = "1.0"
import DDSMGlobal
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
time.sleep()


def main():
    for x, y in zip(DDSMGlobal.lvlan, DDSMGlobal.lname):
        keyboard.type("vlan " + x + "\n")
        keyboard.type("name " + y + "\n")


main()
