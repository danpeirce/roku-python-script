import http.client
import urllib.request, urllib.parse, urllib.error
import msvcrt
import sys

def ecp_invoke(op, path):
    conn = http.client.HTTPConnection(ROKU_IP, 8060)
    conn.request(op, path)
    r = conn.getresponse()
    res = r.read() if r.status==200 else '%d[%s]=' % (r.status, r.reason)
    conn.close()
    return res

ROKU_IP = '192.168.0.25'
get_app_list = lambda: ecp_invoke('GET', '/query/apps')
keypress = lambda key: ecp_invoke('POST', '/keypress/' + key)
keydown = lambda key: ecp_invoke('POST', '/keydown/' + key)
keyup = lambda key: ecp_invoke('POST', '/keyup/' + key)
launch = lambda appID: ecp_invoke('POST', '/launch/' + appID)
send_input = lambda dict: ecp_invoke('POST', '/input?' + '&'.join(map('='.join, list(dict.items()))))

try:
    while True:
        pressedKey = msvcrt.getch()
        if pressedKey == b'i': 
            keypress('Up')
            print('\u2191')  #  print up arrow
        if pressedKey == b'l': 
            keypress('Right')
            print('\u2B95')  #  print Right arrow
        if pressedKey == b'j': 
            keypress('Left')
            print('\u2190')  #  print Left arrow     
        if pressedKey == b'k': 
            keypress('Select')
            print('Select')
        if pressedKey == b',': 
            keypress('Down')
            print('\u2193')  #  print Down arrow
        if pressedKey == b'h': 
            keypress('Home')
            print('Home')
        if pressedKey == b'b': 
            keypress('Back')
            print('Back')
        if pressedKey == b'n': 
            launch('12')
            print('Launch Netflix')
        if pressedKey == b'p': 
            launch('13')
            print('Launch Prime Video')
        if pressedKey == b'y': 
            launch('837')
            print('Launch Youtube')
        if pressedKey == b'z': 
            sys.exit()

except KeyboardInterrupt:
    pass
