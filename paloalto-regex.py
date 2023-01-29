from netmiko import ConnectHandler
import datetime
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

    #config push
    multicli = ["show run"]
    for singlecli in multicli:
        push123 = ssh123.send_command(singlecli)
        print(push123)
        #datetime
        from datetime import datetime
        x = datetime.now()
        # print(x)
        customizedate123 = str(x.year) + "-" + str(x.month) + "_" + str(x.day) + "_" + str(x.hour) + "_" + str(x.minute)
        print(customizedate123)
    #take push report to notepad
        createnewnotepad123 = open(r"C:\Users\sagar\Music\BACKUPS\output_" + singledevice + "-" + newprompt123 + "_" + customizedate123 + ".txt", "a" )
        writecontent123 = createnewnotepad123.write(push123)
        createnewnotepad123.close()
    ssh123.disconnect()



