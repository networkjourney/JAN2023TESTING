from pyntc import ntc_device as NTC123
multidevice = ["172.16.27.78"]
for singledevice in multidevice:
    ios123 = NTC123(host=singledevice, username="admin", password="cisco", device_type='f5_tmos_icontrol')
    ios123.open()
    output123 = ios123.file_copy("f5.bin")
    ios123.install_os("f5.bin")
    ios123.reboot(confirm=True, timer=5)
