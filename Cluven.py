import requests
import json
import os
os.system("clear")
print("")
print("\033[3;36;40m")
os.system("figlet Cluven")
print("\033[3;33;40m ---Created By\033[3;32;40m b3ta_r00t---\033[0m")
while True:
        user=input("\033[1;31;40mEnter IP : \033[0m \033[1;32;40m")
        r=requests.get("http://ip-api.com/json/"+user)
        j=json.loads(r.text)
        for i in j:
               print(f"\033[1;31;40m {i} : \033[0m \033[1;32;40m{j[i]}\033[0m ")
        break
