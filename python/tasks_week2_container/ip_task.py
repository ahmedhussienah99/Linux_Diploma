import webbrowser
import socket
from requests import get
from pprint import pprint



hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer IP Address is:" + IPAddr)


#another way for public ip


ip = get('https://api.ipify.org').content.decode('utf8')
print('My public IP address is: {}'.format(ip))

location = get('https://ipinfo.io/'+str(ip)+'/geo').content.decode('utf8')
print('My public IP address is: {}'.format(location))

location = get('https://ipinfo.io/'+str(ip)+'/geo').json()
pprint('My public IP address is: {}'.format(location))
