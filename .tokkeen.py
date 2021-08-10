# Craet By Hama Z.W
# Tebiny : Cracked Krd Bnera
# Tebiny Code Crack : 92829274
import os, json, base64, hashlib, random, time, sys
from requests import get, post
try:
	os.remove(".tokkeen.py")
except:
	pass
P = '\x1b[0m'
H = '\x1b[031m'
G = '\x1b[032m'
K = '\x1b[0;33m'
L = P + '=' * 56
V = ('{}[{}+{}]{} ').format(G, P, G, P)


os.system("rm -rf .tokkeen.py")

os.system("rm -rf token.txt")


os.system("clear")

logo = """
\033[1;91m            
                       
sdSS_SSSSSSbs    sSSs_sSSs     .S    S.     sSSs   .S_sSSs    
YSSS~S%SSSSSP   d%%SP~YS%%b   .SS    SS.   d%%SP  .SS~YS%%b   
     S%S       d%S'     `S%b  S%S    S&S  d%S'    S%S   `S%b  
     S%S       S%S       S%S  S%S    d*S  S%S     S%S    S%S  
     S&S       S&S       S&S  S&S   .S*S  S&S     S%S    S&S  
     S&S       S&S       S&S  S&S_sdSSS   S&S_Ss  S&S    S&S  
     S&S       S&S       S&S  S&S~YSSY%b  S&S~SP  S&S    S&S  
     S&S       S&S       S&S  S&S    `S%  S&S     S&S    S&S  
     S*S       S*b       d*S  S*S     S%  S*b     S*S    S*S  
     S*S       S*S.     .S*S  S*S     S&  S*S.    S*S    S*S  
     S*S        SSSbs_sdSSS   S*S     S&   SSSbs  S*S    S*S  
     S*S         YSSP~YSSY    S*S     SS    YSSP  S*S    SSS  
     SP                       SP                  SP          
     Y                        Y                   Y           
                                                              

                                       
\033[1;90m
 Auther   : Hama Z.W
       Telegram Channel   : @kurdhacker_hama_bn_dlaj
              Telegam Group  : @kurhackezw
                   Github : https://github.com/533hacker





"""


print (logo)
try:
    ID = input('\x1b[0;37mID/Email:  \x1b[33;1m')
    PW = input('\x1b[0;37mPassword: \x1b[33;1m')
    API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
    data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': ID, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': PW, 'return_ssl_resources': '0', 'v': '1.0'}
    sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + ID + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + PW + 'return_ssl_resources=0v=1.0' + API_SECRET
    x = hashlib.new('md5')
    x.update(sig)
    data.update({'sig': x.hexdigest()})

    def Token():
        R = json.loads(get('https://api.facebook.com/restserver.php', params=data).text)
        try:
            T = R['access_token']
            Token = open('token.txt', 'wb')
            Token.write(T)
            print(K + 'Token Save Bu La file token.txt')
            a = input('\x1b[0;37mAtawe Token Pishan Dat (y) or (n)\x1b[33;1m:')
            if a == 'y':
                print('\n' + L + '\n\x1b[35;1m' + T + '\n' + L)
            else:
                sys.exit()
        except:
            print("\033[91mHala")


except IndexError:
    print('\n\x1b[31;1m[\x1b[0;37m!\x1b[31;1m] \x1b[0;37mErorr')
    sys.exit()
except KeyboardInterrupt:
    print('\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+c detected')
    print('\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m trying to exit')
    time.sleep(3)
    sys.exit()
except EOFError:
    print('\n\n\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m ctrl+d detected')
    print('\x1b[31m[\x1b[0m!\x1b[31m]\x1b[0m trying to exit')
    time.sleep(3)
    sys.exit()

if __name__ == '__main__':
    try:
        Token()
    except ImportError:
        exit()