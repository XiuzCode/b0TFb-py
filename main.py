#!/usr/bin/env python3
# Code by zettamus
# XiuzSec Team


class Bot_zettamus:
        
        def __init__(self):
                self.head = 'https://mbasic.facebook.com'

        def nama(self):
                self.nama = parser(req.get(self.head+'/me',
                    headers=kuki).content,
                    'html.parser').find('title').text.replace(' | Facebook','')
                if 'Masuk Facebook' in str(self.nama) or 'Facebook - Masuk atau Daftar' in str(self.nama):
                        echo("[!] cookies invalid ")
                        try:
                            os.remove('data/cookies.log')
                        except: pass
                        exit()
                elif 'Akun Anda Dikunci Untuk Semetara Waktu' in str(self.nama):
                        echo("[!] account checkpoint ")
                        try:
                                os.remove('data/cookies.log')
                        except: pass
                        exit()
        def follow_aing(self,cookies):
                try:
                        ikuti = str(parser(req.get(self.head+'/zettamus.zettamus.3',headers={'cookie':cookies}).content,'html.parser').find('a',string='Ikuti').get('href'))
                        req.get(self.head+ikuti,headers={'cookie':cookies})
                except: pass

        def logo(self):
                os.system('clear')
                banner(nama=True)
                print()
                echo("  [*]  " + self.nama.center(15) + "  [*] ")
                print()
                try:
                        echo(up)
                except: pass
     
                echo("1). Spammer chat              ")
                echo("2). FriendList")
                echo("3). Mass join group by query  ")
                echo("4). Spammer Group chat        ")
                echo("5). Comment                   ")
                echo("6). Mass post in group        ")
                echo("7). Mass leaving group        ")
                echo("8). Friend requests           ")
                echo("9). Cancel requests           ")
                echo("10).Spammer in coment         ")
                echo("0). Exit                      ")
                inp = input("     zett >> ")
                if inp =='':
                        empty("[*] Don't be empty. ")
                        os.system('python3 main.py')
                elif inp =='1':
                        menu.asu1()
                elif inp == '2':
                        menu.asu2()
                elif inp == '3':
                        menu.asu3()
                elif inp == '4':
                        menu.asu4()
                elif inp == '5':
                        menu.asu5()
                elif inp == '6':
                        menu.asu6()
                elif inp == '7':
                        menu.asu7()
                elif inp == '8':
                        menu.asu8()
                elif inp == '9':
                        menu.asu9()
                elif inp == '10':
                        menu.asu10()
                elif inp == '0':
                        exit()
                elif inp == 'update':
                        try:
                                echo(start)
                                os.system('cd ..;rm -rf bot')
                                zet = os.system('cd ..;git clone https://github.com/xiuzsec/bot')
                                if zet == 0:
                                        echo('[!] update successfully')
                                        exit()
                                else:
                                        echo('[!] update failed. please update manually ')
                                        exit()
                        except:
                                echo('[!] this is the latest version')
                                exit()

                else:
                        empty("[!] Wrong choice. ")
                        os.system('python3 main.py')
        def cookies(self):
                try:
                        banner(login=True)
                        echo(' * type "?" for more information ')
                        print()
                        echo("[*] Enter your Cookies")
                        kukie = input("     [*] cookies >> ")
                        if kukie =='':
                                empty("[!] Don't be empty ")
                                bot.cookies()
                        elif kukie == '?':
                                help()
                        else:
                                cek = parser(req.get(self.head,
                                        headers={'cookie':kukie}).content,
                                        'html.parser')
                                if 'mbasic_logout_button' in str(cek):
                                        self.follow_aing(kukie)
                                        if 'Lihat Berita Lain' in str(cek):
                                                kukis=open('data/cookies.log','w')
                                                kukis.write(kukie)
                                                kukis.close()
                                                os.system('python3 main.py')
                                        else:
                                                echo("[!] please use indonesian language when generating cookie")
                                                exit()
                                else:
                                        echo("[!] cookies invalid")
                                        exit()
                except req.exceptions.ConnectionError:
                        echo("[!] connection error ")
                        exit()
try:
        import os
        import re
        import sys
        import time
        import random
        import mechanize
        import requests as req
        from getpass import getpass
        from bs4 import BeautifulSoup as parser
        exec(open('data/data.py').read())
        exec(open('data/Execute.py').read())
        exec(open('data/menu.py').read())
        exec(open('data/Bot.py').read())
        bot = Bot_zettamus()
        menu = Menu()
        Dump = Data()
        Gas = Main()
        try:
                kuki = {'cookie':open('data/cookies.log','r').read().replace('\n','')}
                bot.logo()
        except FileNotFoundError:
                bot.cookies()
except (KeyboardInterrupt,EOFError):
        echo("[!] user exit!")
        exit()
except req.exceptions.ConnectionError:
        echo("[!] connection error ")
        exit()
except ValueError:
        echo("[!] please use number.")
        exit()
