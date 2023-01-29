from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='netmiko_ospf_script.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
multidevice = open(r"C:\Users\sagar\Music\multidevi.txt", "r")
readmultidevice123 = multidevice.read().splitlines()
print(readmultidevice123)
for singledevice in readmultidevice123:
    devicedictionary = {
        "ip": singledevice,
        "username": "admin",
        "password": "cisco",
        "device_type": "cisco_ios",
        "secret": "cisco@123",
    }
    ssh123 = ConnectHandler(**devicedictionary) #*arg = set
    #ssh established
    prompt123 = ssh123.find_prompt()
    newprompt123 = prompt123.strip("#")
    print(newprompt123)
    #config pushyes
    push123 = ssh123.send_config_set(["no router ospf 100", "network 172.16.27.0 0.0.0.255 area 0"])
    clear123 = ssh123.send_command_timing("clear ip osp process")
    print(clear123)
    if "Reset" in clear123:
        print("ospf is active")
        input123 = input("yes | no:")
        if "yes" in input123:
            print("user agreed to clear the process")
            ssh123.write_channel(input123 + "\n")
            uptime123 = ssh123.send_command("sh ip ospf neighbor gi0/0 detail  | i up")
            print(uptime123)
        else:
            print("this is biz hrs, we cannot reset now")
    else:
        print("ospf is not configured at all")