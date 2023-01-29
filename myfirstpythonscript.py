#netmiko
from netmiko import ConnectHandler
import logging
import
logging.basicConfig(filename='ospfTS.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
opendevicelist = open(r"C:\Users\sagar\Music\multidevi.txt")
readdevicelist = opendevicelist.read().splitlines()
print(readdevicelist)
opencredfile = open(r"C:\Users\sagar\Music\crednotepad.txt")
readcred = opencredfile.read().splitlines()
#print(readcred)
user1 = readcred[0]
print(user1)
pass1 = readcred[1]
print(pass1)
secr1 = readcred[2]
print(secr1)
for singledcv in readdevicelist:
    deviceinfo123 = {
        "ip": singledcv,
        "username": user1,
        "password": pass1,
        'port': 22,
        "secret": secr1,
        "device_type": "cisco_ios"
    }
    ssh123 = ConnectHandler(**deviceinfo123)
    print("^"*5 + " Connecting to " + singledcv)
    ospf123 = ssh123.send_config_set(["no router ospf 100"])
    print(ospf123)
    preupt123 = ssh123.send_command("show ip ospf nei gi0/0 det | i up", textfsm=True)
    print(preupt123)
    clear123 = ssh123.send_command_timing("clear ip ospf process")
    print(clear123)
    if "Reset" in clear123:
        useranswer123 = input("enter yes ? no  to reset process:")
        if "yes" in useranswer123:
            print("resetting")
            x = ssh123.write_channel("yes" + "\n")
            postup123 = ssh123.send_command("show ip ospf nei gi0/0 det | i up")
            print(postup123)
        else:
            print("user declines, this is biz hrs, will do it in off-hrs")
    else:
        print("OSPF is not configured")

