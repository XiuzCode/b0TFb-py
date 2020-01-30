class Menu:
        def __init__(self):
                self.data = []
        def asu1(self):
                print('\n')
                echo("1). Mass chat ")
                echo("2). Mass chat online user ")
                echo("0). Exit ")
                asu = input("     zett >> ")
                if asu =='':
                        empty("[!] Don't be empty. ")
                        self.asu1()
                elif asu =='1':
                        echo("[!] use comma (,) as separator ")
                        user = input("     [*] Username : ").split(',')
                        echo(f"[*] {str(len(user))} selected ")
                        pesan = input("     [*] message : ")
                        banyak = input("     [*] limit : ")
                        for x in user:
                                Dump.GetID('/messages/read/?tid=cid.c.','/'+x,pesan,banyak)
                elif asu =='2':
                        getid = parser(req.get('https://mbasic.facebook.com/buddylist.php',
                            headers=kuki).content,'html.parser')
                        for x in getid.find_all('a',href=True):
                                if "/messages/read/?fbid" in str(x):
                                        self.data.append(x['href'].split('=')[1].replace('&click_type',''))
                        echo(f"[*] {str(len(self.data))} selected ")
                        pesan = input("     [*] message : ")
                        banyak = input("     [*] limit : ")
                        for i in self.data:
                                nama = parser(req.get('https://mbasic.facebook.com/profile.php?id='+i).content,'html.parser').find('title').text.replace(' | Facebook','').replace('Masuk Facebook','Uknown')
                                Gas.Chat(nama,'/messages/read/?tid=cid.c.'+str(i),pesan,banyak,i)
                elif asu =='0':
                        exit()
                else:
                        empty("[!] Wrong choice. ")
                        logo()
        def asu2(self):
                user = input("     [*] Username : ")
                echo("[*] Start grabbing ID ..  ")
                Dump.List('/'+user+'/friends?')
        def asu3(self):
                query = input("     [*] query : ")
                Dump.Join('https://mbasic.facebook.com/search/groups/?q='+query)
        def asu4(self):
                idg = input("     [*] id group : ") 
                Dump.info('/messages/read/?tid=cid.g.'+idg,idg)
        def asu5(self):
                print('\n')
                echo("1). in timeline")
                echo("2). in friend")
                echo("3). in group ")
                echo("0). Exit")
                asu = input("     zett >> ")
                if asu =='':
                        empty("[!] Don't be empty. ")
                        bot.logo()
                elif asu =='1':
                        limit = input("     [*] limit : ")
                        Dump.sts(limit,asu,'/home.php')
                        Gas.comment()
                elif asu =='2':
                        user = input("     [*] Username : ")
                        limit = input("     [*] limit : ")
                        Dump.sts(limit,asu,user)
                elif asu == '3':
                        Dump.sts('None',asu,'/groups/')
                elif asu =='0':
                        exit()
                else:
                        empty("[!] Wrong choice. ")
                        bot.logo()
        def asu6(self):
                print('\n')
                echo('[*] Press Enter to see all group ')
                cari = input("     [*] query : ")
                Dump.auto_post(cari)
        def asu7(self):
                print('\n')
                echo('[*] Press Enter to see all group ')
                user = input("     [*] query : ")
                Dump.leave(user)
        def asu8(self):
                print('\n')
                echo("1). accept")
                echo("2). reject ")
                echo("0). exit ")
                asu = input("     zett >> ")
                if asu == '':
                        empty("[!] Don't be empty. ")
                        os.system('python3 main.py')        
                elif asu =='1':
                        self.pilih = 1
                        Dump.Req(asu,'Konfirmasi')
                elif asu == '2':
                        Dump.Req(asu,'Hapus Permintaan')
                elif asu =='0':
                        exit()
                else:
                        empty("[!] Wrong choice. ")
                        bot.logo()
        def asu9(self):
                print('\n')
                echo("[*] Fetching ID ..  ")
                Dump.Cancel('/friends/center/requests/outgoing')
        def asu10(self):
                print('\n')
                asu = input("     [*] url post >> ")
                Dump.CekPost(asu)
