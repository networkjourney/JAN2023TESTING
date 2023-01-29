#napalm

from napalm import get_network_driver
drvr123 = get_network_driver("ios")
ios123 = drvr123("172.16.27.40", "admin", "cisco")
ios123.open()
#ssh established
ios123.load_replace_candidate(r"C:\Users\sagar\Music\BACKUPS\config.txt")
diff123 = ios123.compare_config()
print(diff123)
#diff check result showcased
if len(diff123):
  answer123 = input("yes ? no:")
  #user to input yes or now
  #
  #if answer123 == "yes":
   #print("Perform the changes")
   #ios123.commit_config()
  # print("config is sccfly")
   #
  else:
    print("Cofnig Declined by users")
answer1234 = input("rollback yes ? no:") #comment
if answer1234 == "yes":
 print("rolling back")
 ios123.rollback()
 print("DONE")
ios123.close()

#PORT DESCRIPT
#QOS
#SNMP
#ACL
#NTP
#SYSLOG
#LINE VTY _> acl
#