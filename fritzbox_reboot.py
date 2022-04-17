#==============================================
# Automatically reboot Fritz!Box routers
# Uses TR-046 protocol
# API documentation: 
# - https://avm.de/service/schnittstellen/
# - http://fritz.box:49000/tr64desc.xml
# - https://wiki.fhem.de/wiki/FRITZBOX#TR-064
# Author: dev-lu
#==============================================
from decouple import config
from requests.auth import HTTPDigestAuth
import requests

ip = '192.168.178.1'
port = '49000'
user = config('FRITZ_USER')
password = config('FRITZ_PASSWORD')
service_type= '/upnp/control/deviceconfig'
uri= 'urn:dslforum-org:service:DeviceConfig:1'
action= 'Reboot'
data = '<?xml version=\'1.0\' encoding=\'utf-8\'?><s:Envelope s:encodingStyle=\'http://schemas.xmlsoap.org/soap/encoding/\' xmlns:s=\'http://schemas.xmlsoap.org/soap/envelope/\'><s:Body><u:$action xmlns:u=' + uri + '></u:$action></s:Body></s:Envelope>'

headers = {
    'Content-Type': 'text/xml',
    'charset': 'utf-8',
    'SoapAction': uri + '#' + action
}


response = requests.post('http://' + ip + ':' + port + service_type, 
                        auth = HTTPDigestAuth(user, password),
                        headers=headers,
                        data=data)
# Print response if needed
# print(response)
