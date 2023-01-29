from napalm import get_network_driver
import json
drivers123 = get_network_driver("ios")
multipledevice = ["172.16.29.62", ]
for singledevice in multipledevice:
    ssh123 = drivers123(singledevice, "admin", "cisco")
    ssh123.open()
    #ssh estbld
    ssh123.load_merge_candidate(r"C:\Users\sagar\Music\replacecandidate2.txt")
    #file is sent
    diffcheck123 = ssh123.compare_config()
    print(diffcheck123)
    if len(diffcheck123) > 0:
        answer123 = input("do you want to commit changes? yes?no")
        if answer123 == "yes":
            print("config to be pushed")
            ssh123.commit_config()
            print("Done!")
        else:
            print("no change required as of now")
            ssh123.discard_config()

