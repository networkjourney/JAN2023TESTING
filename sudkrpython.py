from netmiko import ConnectHandler
import time
from netmiko.ssh_exception import NetmikoAuthenticationException, NetMikoTimeoutException, SSHException
new_list_multiple_list123 = open(r"C:\\Users\\Public\\Downloads\\list_of_devices.txt")
ip_add = new_list_multiple_list123.read().split("\n")
for i in ip_add:
    a = 1
    while a <= 5:
        try:
            device_info = {
                'device_type': 'cisco_ios',
                'ip': i,
                'username': input("enter the  username: "),
                'password': input("enter the password: "),
                'secret': 'cisco'
            }
            time.sleep(5)
            ssh_session = ConnectHandler(**device_info)
            ssh_session.enable()
            out123 = ssh_session.find_prompt()
            print(out123)
            if ">" or "#" in out123:
                print(" login is successful " + i)
                break
            else:
                pass
        except NetmikoAuthenticationException:
            print("trying again")
        a = a + 1
        print(a)
