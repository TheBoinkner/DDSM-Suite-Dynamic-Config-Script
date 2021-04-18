# $language = "python"
# $interface = "1.0"

# EIGRP
eigrp = "52"

# WSM VLAN Numbers
wvlan = ["10", "20", "30", "40", "50"]

# WSM VLAN IPs
wdefgate = ["192.168.0.1", "192.168.0.3", "192.168.0.5", "192.168.0.7", "192.168.0.9"]

# WSM VLAN Subnet (referenced as "s(slash notation)" ie (s32 = 255.255.255.255))
wsub = []

# WSM VLAN Names
wname = []

# WSM Sub Interfaces
wint = []

# LSM VLAN Numbers
lvlan = ["30", "35", "40", "45"]

# LSM VLAN IPs
ldefgate = []

# LSM VLAN Subnet
lsub = []

# LSM VLAN Names
lname = ["USERS", "VIP_USERS", "VOICE", "VIP_VOICE"]

# LSM Sub interfaces
lint = ""

# KG ip (IP and subnet)
kg = ""

# Vsat Ip
vsat = ""

# Sub Interface port
port = "g2/0."

# trunking
trunk = ""

# port range
portrange = ""

# ------------------------------------(do not touch from this line down)------------------------------------------------
# ------------------------------------------------Functions-------------------------------------------------------------


def calc(defgate):
    new_list = []
    for x in defgate:
        parts = x.split(".")
        parts[3] = str(int(parts[3]) - 1)
        new_list.append(".".join(parts))
    return new_list


weigrpip = list(calc(wdefgate))
leigrpip = list(calc(ldefgate))


# -------------------------------------------PERMANENT VARIABLES--------------------------------------------------------
# Subnet Masks (Allows you to call upon a subnet via a modified slash notation)
s24, s25, s26, s27, s28, s29, s30, s31, s32 = "255.255.255.0", "255.255.255.128", "255.255.255.192", \
                                              "255.255.255.224", "225.255.255.240", "255.255.255.248", \
                                              "255.255.255.252", "255.255.255.254", "255.255.255.255 "
