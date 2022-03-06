import subprocess
proc = subprocess.check_output("ipconfig /all" ).decode('oem')
try:
    macE = proc.split('\n')
    macE = macE[14].replace(" ", "").split(":")
    macE = macE [1]
    if(len(macE)==18):
        mac = macE
    else:
        macSfio1 = proc.split('\n')
        macSfio1 = macSfio1[23].replace(" ", "").split(":")
        macSfio1 = macSfio1 [1]
        if(len(macSfio1)==18):
            mac = macSfio1
        else:
            macSfio2 = proc.split('\n')
            macSfio2 = macSfio2[32].replace(" ", "").split(":")
            macSfio2 = macSfio2 [1]
            if(len(macSfio2)==18):
                mac = macSfio2
            else:
                macWifi = proc.split('\n')
                macWifi = macWifi[40].replace(" ", "").split(":")
                macWifi = macWifi[1]
                if(len(macWifi)==18):
                    mac = macWifi
except:
    print('nenhum mac encontrado')

print(mac)


