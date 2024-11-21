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

print("Roku Remote Control")

try:
    while True:
        pressedKey = msvcrt.getch()
        if pressedKey == b'i': 
            keypress('Up')
            print('\u2191')  #  print up arrow
        elif pressedKey == b'l': 
            keypress('Right')
            print('\u2192')  #  print Right arrow
        elif pressedKey == b'j': 
            keypress('Left')
            print('\u2190')  #  print Left arrow     
        elif pressedKey == b'k': 
            keypress('Select')
            print('Select')
        elif pressedKey == b'e': 
            keypress('Enter')
            print('Enter')            
        elif pressedKey == b',': 
            keypress('Down')
            print('\u2193')  #  print Down arrow
        elif pressedKey == b'h': 
            keypress('Home')
            print('Home')
        elif pressedKey == b'b': 
            keypress('Back')
            print('Back')
        elif pressedKey == b'n': 
            launch('12')
            print('Launch Netflix')
        elif pressedKey == b'p': 
            launch('13')
            print('Launch Prime Video')
        elif pressedKey == b'y': 
            launch('837')
            print('Launch Youtube')
        elif pressedKey == b'c': 
            launch('614780')
            print('Launch CBC Gem')
        elif pressedKey == b's': 
            launch('22297')
            print('Launch Spotify')
        elif pressedKey == b'w': 
            launch('84056')
            print('Launch The Weather Network')
        elif pressedKey == b'g': 
            launch('259870')
            print('Launch Global TV')
        elif pressedKey == b'z': 
            sys.exit()

except KeyboardInterrupt:
    pass
