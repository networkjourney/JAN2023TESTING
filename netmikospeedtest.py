#SSH core module
from netmiko import ConnectHandler
user123 = open(r"C:\\Users\\sagar\\Music\\crednotepad.txt")
xyz = user123.read().splitlines()
username123 = xyz[0]
secret123 = xyz[1]
password123 = xyz[1]
multidevices123 = open(r"C:\\Users\\sagar\\Music\\multidevi.txt")
new_xyz = multidevices123.read().splitlines()
import time
start123 = time.time()
print(start123)
for abc123 in new_xyz:
    dict123 = {
        "device_type": "cisco_ios",
        "username": username123,
        "secret": secret123,
        "port": 22,
        "password": password123,
        "ip": abc123,
    }
    ssh123 = ConnectHandler(**dict123)
    print("$"*5 + " CONNECTED TO " + abc123 + "$"*5)
    xyz123 = ssh123.send_config_from_file(r"C:\\Users\\sagar\\Music\\nornir config push.txt")
    print(xyz123)
end123 = time.time()
print(end123)
elapsed_time = end123 - start123
print(elapsed_time)