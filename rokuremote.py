import http.client
import urllib.request, urllib.parse, urllib.error
import msvcrt

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
        if pressedKey == 'i': 
            keypress('Up')
            print('\033[F\u2191')  # move to start of previous line print up arrow
        if pressedKey == 'l': 
            keypress('Right')
            print('\033[F\u2B95')  # move to start of previous line print Right arrow
        if pressedKey == "j": 
            keypress('Left')
            print('\033[F\u2190')  # move to start of previous line print Left arrow     
        if pressedKey == "k": 
            keypress('Select')
        if pressedKey == ",": 
            keypress('Down')
        if pressedKey == "h": 
            keypress('Home')
        if pressedKey == "b": 
            keypress('Back')
        if pressedKey == 'z': 
            sys.exit()

except KeyboardInterrupt:
    pass
