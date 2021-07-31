import subprocess
import os
dw = subprocess.check_output(['netsh','wlan','show','network'])                           # using the check_output() for having the network term retrival
decoded_dw = dw.decode('ascii')                                                           # decode it to strings
print(decoded_dw)                                                                         # displaying the information                                                                                                 
ssid = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')    # input Wifi name  
passwd = input('Enter password')
output = subprocess.check_output(['sudo', 'nmcli', 'device', 'wifi', 'connect', ssid,'password', passwd])
