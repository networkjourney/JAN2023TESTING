from netmiko import ConnectHandler
#dictionary
import logging
logging.basicConfig(filename='netmiko_global_ospf.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

openfile = open(r"C:\Users\sagar\Music\multidevi.txt")
multidevice123 = openfile.read().splitlines()
print(multidevice123)
for singledevice123 in multidevice123:
    devicedata123 = {
        "ip": singledevice123,
        'username': "admin",
        "password": "cisco",
        "device_type": "cisco_ios",
    }

    ssh123 = ConnectHandler(**devicedata123)     #ssh is stablshd
    print("Connected to " + singledevice123)
    #configs to be made
    config123 = ssh123.send_config_set(["no router ospf 100","no router ospf 100",])
    print(config123)
    out123 = ssh123.send_command("show ip ospf neigh gi0/0 detail | i up")
    print(out123)
    clear123 = ssh123.send_command_timing("clear ip ospf process")
    print(clear123)
    if "Reset" in clear123:
        input123 = input("yes or not:")
        if "yes" in input123:
            ssh123.write_channel(input123)
            ssh123.write_channel("\n")
            out123 = ssh123.send_command("show ip ospf neigh gi0/0 detail | i up")
            print(out123)
        if "no" in input123:
            print("Biz hrs, user declines the ospf reset process")
    else:
        print("OSPF IS NOT CONFIGURED AT ALL")


