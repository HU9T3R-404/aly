#-----------------(import modules)---------
import sys,os,time,random
#-----------------(clear terminal screen)---------
os.system('clear')
#-----------------(main code)---------
def loading_animation():
    animation = ['[■□□□□□□□□□]','[■■□□□□□□□□]','[■■■□□□□□□□]','[■■■■□□□□□□]','[■■■■■□□□□□]','[■■■■■■□□□□]','[■■■■■■■□□□]','[■■■■■■■■□□]','[■■■■■■■■■□]','[■■■■■■■■■■]']
    num_iterations = 2
    counter = 0
    for i in range(10):
        color_code = random.randint(91, 96)
        colored_animation = animation[i % len(animation)].replace('■', f'''\x1b[1;{color_code}m■\x1b[0m''')
        sys.stdout.write('\r- Script Is Running ' + colored_animation)
        sys.stdout.flush()
        time.sleep(0.1)
    counter += 1
    if counter >= num_iterations:
        pass

import os,json,hashlib,io,struct
os.system('clear')
#print('\n\n Checking for modules! ')
print(' ')
from requests import api
from urllib3 import connection
from urllib import request
from requests import sessions
from requests import models
from requests import utils
from requests import adapters
from requests import cookies
from requests import compat
from requests import hooks
from requests import exceptions
from requests import certs
from requests import structures
from requests import auth
from requests import packages
import os, requests, re, time, sys, random, json
from concurrent.futures import ThreadPoolExecutor as Thread
import marshal,zlib
import re,uuid,sys,random,time,os,subprocess,platform
try:
    from bs4 import BeautifulSoup as sp
    from fake_email import Email
    from concurrent.futures import ThreadPoolExecutor as Thread
    import requests
except:
    os.system('pip install bs4 fake_email futures requests ')
    from bs4 import BeautifulSoup as sp
    from fake_email import Email
    from concurrent.futures import ThreadPoolExecutor as Thread
    import requests
import urllib.request
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor



sys.stdout.write('\x1b]2; HUNT3R\x07')



'''-------#clour#------'''

whi = "\033[1;97m"
yal = "\033[1;93m"
red = "\033[1;91m"
gren = "\033[1;92m"
'''-------------------------'''
ok=0
mthd=[]
def lop(text):
    sys.stdout.write(f'\r\r\r\033[0m{text}             \r');sys.stdout.flush()
tm=[]
tm=[]
logo = f"""\033[37m                 
 
\033[1;92m dP""b8 8b    d8        db    88     Yb  dP 
\033[1;33mdP   `" 88b  d88       dPYb   88      YbdP  
\033[1;34mYb  "88 88YbdP88      dP__Yb  88  .o   8P   
 \033[1;91mYboodP 88 YY 88     dP    Yb 88ood8  dP    

\033[1;97m\033[33m{'-'*40}\033[37m"""
#print(logo)
def clr():
    os.system('clear')
    print(logo)




def menu():
    
    clr()
    for i in range(1, 3):
        print(f'[{i}] Method ')
    linex()

    mt = input('[?] Select: ')
    if mt == "1":
        mthd.append("1")
    else:
        mthd.append("2")
    linex()

    m = "2"
    if m == "1":
        tm.append("one")
    else:
        tm.append('two')
    Create()


def linex():
    print(f'\033[97m--------------------------------------------')

def gri():
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip_address

def rnd(a,b):
    return str(random.randint(a,b))



def random_ua():
    def random_version():
        return f"{random.randint(201, 301)}.0.0.{random.randint(2, 51)}.{random.randint(101, 1000)}"

    def random_density():
        return f"{random.uniform(2.0, 4.0):.2f}"

    def random_device():
        devices = [
            'samsung', 'huawei', 'xiaomi', 'oneplus', 'oppo', 'vivo', 'nokia', 'lg', 'sony', 'htc',
            'motorola', 'lenovo', 'asus', 'zte', 'realme', 'blackberry', 'meizu', 'alcatel', 'coolpad', 'google'
        ]
        return random.choice(devices)

    def random_model():
        models = [
            'SM-S367VL', 'SM-N960U', 'SM-G611L', 'SM-G996N', 'SM-G870W', 
            'SM-G950F', 'SM-T116NQ', 'SM-G955N', 'SM-G389F', 'SM-G981B',
            'Pixel 4', 'Pixel 5', 'Pixel 6', 'Pixel 7', 'Moto G Power',
            'Moto E6', 'Moto G Stylus', 'Lenovo K10', 'Asus ROG Phone', 'ZenFone 7',
            'OnePlus 8', 'OnePlus 9', 'OnePlus Nord', 'Xiaomi Mi 11', 'Xiaomi Redmi Note 10',
            'Oppo Reno 5', 'Vivo Y20', 'Vivo V21', 'Huawei P30', 'Huawei Mate 40'
        ]
        return random.choice(models)

    def random_locale():
        locales = [
            'en_US', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'pt_BR', 'zh_CN', 'ja_JP', 'ko_KR',
            'ru_RU', 'ar_AE', 'tr_TR', 'hi_IN', 'th_TH', 'vi_VN', 'nl_NL', 'sv_SE', 'pl_PL'
        ]
        return random.choice(locales)

    def random_carrier():
        carriers = [
            'Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Vodafone', 'Orange', 'Telekom', 'Movistar',
            'Claro', 'Telcel', 'Bell', 'Rogers', 'Telstra', 'Optus', 'SingTel', 'M1', 'StarHub'
        ]
        return random.choice(carriers)

    fban_template = (
        "[FBAN/FB4B;FBAV/{version};FBBV/{version_code};"
        "FBDM/{{density={density},width={width},height={height}}};"
        "FBLC/{locale};FBRV/{random_num};FBCR/{carrier};"
        "FBMF/{manufacturer};FBBD/{brand};FBPN/com.facebook.katana;"
        "FBDV/{device_model};FBSV/{os_version};FBOP/20;FBCA/armeabi-v7a:armeabi;]"
    )

    version = random_version()
    version_code = random.randint(100000001, 200000001)
    density = random_density()
    width = random.randint(721, 1441)
    height = random.randint(1281, 2561)
    locale = random_locale()
    random_num = random.randint(100000001, 999999999)
    carrier = random_carrier()
    manufacturer = random_device()
    brand = manufacturer
    device_model = random_model()
    os_version = random.randint(9, 14)

    fban_user_agent = fban_template.format(
        version=version,
        version_code=version_code,
        density=density,
        width=width,
        height=height,
        locale=locale,
        random_num=random_num,
        carrier=carrier,
        manufacturer=manufacturer,
        brand=brand,
        device_model=device_model,
        os_version=os_version
    )

    return fban_user_agent
def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx


       

class Create:
    def __init__(self):
        clr()
        for i in range(76000):
            self.start()
    def process(self,pas,m):
        global ok
        ip=str(gri())
        session=requests.Session()
        num="+923"+rnd(10,49)+rnd(1111111,9999999)
        self.ua= random_ua()
        lop(" Num: "+num)
        self.m = ['Husnain|Khan','Hunter|Return']
        if m =="1":
            response1 = session.get('https://web.facebook.com/r.php')
            captcha_persist_data = re.search('name="captcha_persist_data" value="(.*?)"', str(response1.text)).group(1)
            reg_instance = re.search('name="reg_instance" value="(.*?)"', str(response1.text)).group(1)
            haste_session = re.search('"haste_session":"(.*?)"', str(response1.text)).group(1)
            hsi = re.search('"hsi":"(.*?)"', str(response1.text)).group(1)
            spin_t = re.search('"__spin_t":(.*?),', str(response1.text)).group(1)
            spin_r = re.search('"__spin_r":(.*?),', str(response1.text)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(response1.text)).group(1)
            lsd = re.search('name="lsd" value="(.*?)"', str(response1.text)).group(1)
            ri = re.search('name="ri" value="(.*?)"', str(response1.text)).group(1)
            data = {'jazoest': jazoest,'lsd': lsd,'firstname': random.choice(self.m).split("|")[0],'lastname': random.choice(self.m).split("|")[1],'reg_email__': num,'reg_email_confirmation__':num,'reg_passwd__': pas,'birthday_day': str(random.randint(1,28)),'birthday_month': str(random.randint(1,11)),'birthday_year': str(random.randint(1978,2002)),'birthday_age': '','did_use_age': 'false','sex': '2','preferred_pronoun': '','custom_gender': '','referrer': '','asked_to_login': '0','use_custom_gender': '','terms': 'on','ns': '0','ri': ri,'action_dialog_shown': '','ignore': 'captcha','locale': 'en_GB','reg_instance': reg_instance,'captcha_persist_data': captcha_persist_data,'captcha_response': '','__user': '0','__a': '1','__req': '8','__hs': haste_session,'dpr': '2','__ccg': 'GOOD','__rev': spin_r,'__s': '0fk0jz:jng6tr:a3pmr9','__hsi': hsi,'__dyn': '','__csr': '','__spin_r': spin_r,'__spin_b': 'trunk','__spin_t': spin_t}
            self.h3dx = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': self.ua,'viewport-width': '980','x-asbd-id': '129477','x-fb-lsd': lsd}
            req = session.post('https://www.facebook.com/ajax/register.php',data=data,headers=self.h3dx).text
        else:
            response1=session.get("https://m.facebook.com/reg")
            lsd=re.search('name="lsd" value="(.*?)"',str(response1.text)).group(1)
            jazo=re.search('name="jazoest" value="(.*?)"',str(response1.text)).group(1)
            inta=re.search('name="reg_instance" value="(.*?)"',str(response1.text)).group(1)
            impres=re.search('name="reg_impression_id" value="(.*?)"',str(response1.text)).group(1)
            tok = re.search('privacy_mutation_token=(.*?)"',str(response1.text)).group(1)
            headers = {
            'authority': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '3',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/reg/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X6833B"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.ua,
            'viewport-width': '360',
            'x-asbd-id': '129477',
            'x-fb-lsd': lsd,
            }
            params = {
            'privacy_mutation_token': tok,
            'app_id': '103',
            'multi_step_form': '1',
            'skip_suma': '0',
            'shouldForceMTouch': '1',
            }
            data = {
            'ccp': '2',
            'reg_instance': inta,
            'submission_request': 'true',
            'helper': '',
            'reg_impression_id': impres,
            'ns': '1',
            'zero_header_af_client': '',
            'app_id': '103',
            'logger_id': str(uuid.uuid4()),
            'field_names[0]': 'firstname',
            'firstname': random.choice(self.m).split("|")[0],
            'lastname': random.choice(self.m).split("|")[1],
            'field_names[1]': 'birthday_wrapper',
            'birthday_day': rnd(5,26),
            'birthday_month': rnd(1,12),
            'birthday_year': rnd(1977,2002),
            'age_step_input': '',
            'did_use_age': 'false',
            'field_names[2]': 'reg_email__',
            'reg_email__': num,
            'field_names[3]': 'sex',
            'sex': '1',
            'preferred_pronoun': '',
            'custom_gender': '',
            'field_names[4]': 'reg_passwd__',
            'name_suggest_elig': 'false',
            'was_shown_name_suggestions': 'false',
            'did_use_suggested_name': 'false',
            'use_custom_gender': 'false',
            'guid': '',
            'pre_form_step': '',
            'reg_passwd__': pas,
            'submit': 'Sign Up',
            'jazoest': jazo,
            'lsd': lsd,
            '__dyn': '',
            '__csr': '',
            '__req': 'f',
            '__a': '',
            '__user': '0',
            }
            koki = (";").join([ "%s=%s" % (key, value) for key, value in response1.cookies.get_dict().items() ])
            koki+=';m_pixel_ratio=2.625;wd=412x756'
            response = session.post('https://m.facebook.com/reg/submit/', params=params, cookies={"cookie":koki}, headers=headers, data=data)

        response=session.get("https://mbasic.facebook.com")       
        if "checkpoint" in response.text:
            lop(" Account is Failed ")
            return "chk"
        if not "c_user" in dict(session.cookies):         
            lop(" Failed To Create")
            return 0
       # print("[\033[91m√\033[37m] \033[32mAccount is Live ")
        headers = {
        'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-PK, en;q=0.9, en-US;q=0.8, en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '21',
        'upgrade-insecure-requests': '1',
        'user-agent':self.ua,
        }
        for i in  re.findall('href="(.*?)"',response.text.replace("amp;","")):
          if "changeemail" in i:
            url=i
        response = session.get("https://mbasic.facebook.com"+url, headers=headers)
        w = tm[0]
        if "two" ==w:
            from fake_email import Email
            mmail=Email().Mail()
            em=mmail['mail']
        else:
            pos = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
            em = pos['email']
        headers = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-PK, en;q=0.9, en-US;q=0.8, en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent':self.ua,
        }
        data = {
            'fb_dtsg': find(response.text,"fb_dtsg"),
            'jazoest': find(response1.text,"jazoest"),
            'old_email': num,
            'reg_instance': find(response1.text,"reg_instance"),
            'new': em,
            'next': '',
            'submit': 'Add'
        }
       #### print("[+] Adding  Email")
        url = "https://m.facebook.com"+re.findall('action="(.*?)"',response.text.replace("amp;",""))[0]
        response = session.post(url, headers=headers, data=data)
        r=session.get("https://mbasic.facebook.com")
       # print("\033[37m[\033[91m+\033[37m] Added Email : "+em)
        time.sleep(15)
        w = tm[0]
        if "two" ==w:
            h=Email(mmail["session"]).inbox()
            if h:
                j = h['topic'].split('-')[1];hh = j.split(' ')[0]
                cd = hh
        else:
            req = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{em}/messages').json()
            cd = re.search(r'FB-([^ ]+)',str(req)).group(1)
        try:cd
        except:return 0
      #  print('[\033[91m+\033[37m] Code   '+cd)
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-ch-ua-platform-version': '11.0.0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':self.ua,
        }
        data = {'c': cd,'fb_dtsg': find(r.text,"fb_dtsg"),'jazoest': find(r.text,"jazoest"),'submit[confirm]': 'Confirm'}
        fn = re.search('method="post" action="(.*?)"', str(r.text)).group(1)
        url = 'https://mbasic.facebook.com'+fn
        response = session.post(url, headers=headers, data=data)
        if "checkpoint" in response.text:
            lop("[×] Account is Failed ")
            return "chk"
        else:
            return session
    def getcok(self,koki):
        Cook = ("c_user=" + koki["c_user"] + ";""xs=" + koki["xs"] + ";""sb=" + koki["sb"] + ";""fr=" + koki["fr"] + ";""datr=" + koki["datr"] + ";""dpr=2" + ";""locale=en_PK" + ";""wd=950x1835" + ";""m_page_voice=" + koki['c_user'] + ";")
        return Cook

    def get(self):
      return random.choice(["-","/","|","\\"])
    def start(self):
     try:
       global ok
       import sys
       pas = "HUNT3R" + str(random.randint(10000, 111111))
       m = mthd[0]
       ggg=self.process(pas,m)

       if ggg=="chk":
         pass
       elif ggg==0:pass
       else:
          koki = (";").join([ "%s=%s" % (key, value) for key, value in ggg.cookies.get_dict().items() ])
          koki+=';m_pixel_ratio=2.625;wd=412x756'
          dc=dict(ggg.cookies)
          coki = self.getcok(dc)
          uid=re.findall("c_user=(.*?);",coki)[0]
          check = requests.get('https://mbasic.facebook.com',cookies={'cookie':koki}).text
          if "checkpoint" not in str(check):
              ###&&&&&&&print(40*"-")
              print("\033[92m[G M ALY-OK] "+uid+' | '+pas)
             # print(koki)
            #  print('\033[91m--------------------------------------------------')
              #####print(40*'\033[37m-')
              ok+=1
              open("/sdcard/HUNT3R-CRT-OK.txt","a").write(uid+"|"+pas+"|"+koki+"\n")
            ###  profile(koki)
              ##bio(koki)
              ##subscribe(koki)
              ##otComment(koki)
              ####creatingProfilePage(uid,pas,koki)
          else:pass
     except Exception as e:
         ###print(e)
         if not "urllib" or "perma" in str(e):pass
         time.sleep(2)
     except requests.exceptions.ConnectionError:
         time.sleep(3)
def approval():
    
    try:
        lol = str(os.getuid()) * 8
        url = zlib.decompress(
            b'x\x9c\xcb())(\xb6\xd2\xd7O\xcf,\xc9(M\xd2K\xce\xcf\xd5\xf7\x08\xb5\x0c1\x0e\xd2510\x012\xfd\x80L\xfd\xa4\x9c\xfc$\xfd\xdc\xc4\xcc<\xa8\x80^IE\t\x00\x1f\xce\x12u'
        ).decode()

        if not check_internet_connection():
            exit('Error: Internet Connection!')

        content = fetch_content(url)
        if content is None:
            exit('[×] Connection Error!')

        if "Server Off" in content:
            print("Tool Off")
            exit()
        elif "Free Trial" in content or lol in content:
            menu()
        else:
            
            print(f"[=] Your Key: {lol}")
            print('[=] Your Key Is Not Approv \n[=] Copy This Key & Sent To admin');linex()
            print('[=] \033[92mTool  Auto Create  fb....\033[37m')
            linex()
          ###  name = input('Your name: ')
            input('[=] Press Enter... ')
            tks = f"sir I want to get approved \nPlease Approve My Key\nKey: {lol}"
            tks = requests.utils.quote(tks)
            os.system(f'am start https://wa.me/+923464563392?text={tks}')
            approval()

    except requests.exceptions.ConnectionError:
        print("[!] No Internet Connection")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")

def check_internet_connection():
    try:
        requests.get('https://github.com')
        return True
    except requests.exceptions.RequestException:
        return False

def fetch_content(url):
    try:
        result = subprocess.run(["curl", url], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return None

approval()
