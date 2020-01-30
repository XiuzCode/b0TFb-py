#!/usr/bin/env python3
# Code by zettamus
# XiuzSec.

class Data:
        
        def __init__(self):
                self.head = 'https://mbasic.facebook.com{}'
                self.data = []
                self.id = []
                self.lan = []
                self.hitung = 0
                self.data_Chat = []
        def Grub_View(self,cari):
                data = parser(req.get(self.head.format('/groups/?seemore'),
                    headers=kuki).content,'html.parser')
                for x in data.find_all('a'):
                        if '/groups/' in x['href']:
                                if 'category' in x['href'] or 'create' in x['href']:
                                        continue
                                if cari in x.text:
                                        y = re.findall("/groups/(.*?)\?",x["href"])
                                        if len(y) != 0:
                                                self.id.append(y[0])
                                                echo(f"{str(len(self.id))}). {x.text}")
        def GetId(self,url):
                data = parser(req.get(self.head.format(url),
                    headers=kuki).content,'html.parser')
                if self.set in str(data):
                        for kon in data.find_all('a',string=self.set):
                                if '/a/notifications.php?' in str(kon):
                                        self.data.append(kon.get('href'))
                                        print(f"\r          {str(len(self.data))}). retrieved .. ",end='')
                if 'Lihat selengkapnya' in str(data):
                        self.GetId(data.find('a',
                            string='Lihat selengkapnya').get('href'))
                empty("\n[*] press enter to continue ")
                for user in self.data:
                        Gas.Req(user)
        def Dump_post(self,user):
                dump = parser(req.get(self.head.format(user),
                    headers=kuki).content,'html.parser')
                for sts in dump.find_all('a',href=True):
                        try:
                                if '/story.php?' in sts['href']:
                                        if sts.string == 'Berita Lengkap':
                                                self.data.append(sts['href'])     
                                if '/groups/' in sts['href']:
                                        if sts.string == 'Berita Lengkap':
                                                self.data.append(sts['href'])
                        except EOFError: pass
                print(f"\r         {str(len(self.data))}). retrieved .. ",end='')
                if len(self.data) > int(self.limit):
                        msg = input("\n     [*] comment >> ")
                        for x in self.data:
                                Gas.comment_post(self.head.format(x),msg)
                        echo("[!] Done ")
                        exit()
                if 'Lihat Berita Lain' in str(dump):
                        self.Dump_post(dump.find('a',
                            string = 'Lihat Berita Lain').get('href'))
                if 'Lihat Postingan Lainnya' in str(dump):
                        self.Dump_post(dump.find('a',string='Lihat Postingan Lainnya').get('href'))
                if len(self.data) == 0:
                        echo("[!] can't dump url post, maybe this not friend")
                        exit()
        def GetID(self,tipe,link,msg,limit):
                data = parser(req.get(self.head.format(link),
                    headers=kuki).content,'html.parser')
                if 'Konten Tidak Ditemukan' in str(data):
                        echo('[!] username wrong : '+link)
                        pass
                else:
                        nama = data.find('title').text.replace(' | Facebook','')
                        for i in data.find_all('a',href=True):
                                if '/mbasic/more/?owner_id=' in i['href']:
                                        user = i['href'].split('=')[1]
                                        Gas.Chat(nama,tipe+str(user),msg,limit,user)

        def List(self,link):
                li = open('list.txt','a')
                data = parser(req.get(self.head.format(link),
                    headers=kuki).content,'html.parser')
                if 'Halaman Tidak Ditemukkan' in str(data):
                        echo('[!] username wrong')
                        exit()
                else:
                        for i in data.find_all(style="vertical-align: middle"):
                                x = i.find('a')
                                if 'None' in str(x):
                                        continue
                                try:
                                        id = re.findall("/(.*?)?fref=",
                                                x["href"])[0].replace("?","").replace("profile.phpid=","").replace('&','')
                                        li.write(x.text+'|'+id+'\n')
                                        self.lan.append(id)
                                        print(f'\r        {str(len(self.lan))}). {id}       ',end='')
                                except IndexError: pass
                        li.close()
                        if 'Lihat Teman Lain' in str(data):
                                self.List(data.find('a',string='Lihat Teman Lain').get('href'))

        def Join(self,link):
                data = parser(req.get(link,headers=kuki).content,'html.parser')
                for x in data.find_all('a'):
                        if '/a/groups/join/?' in str(x):
                                pass
                        i = x.find('div')
                        if 'None' in str(i) or '+' in str(i):
                                continue
                        else:
                                self.hitung += 1
                                echo(f'{str(self.hitung)}). {i.text} ')
                                self.data.append('https://mbasic.facebook.com'+x['href'])
                if 'Lihat Hasil Selanjutnya' in str(data):
                        self.Join(data.find('a',
                            string='Lihat Hasil Selanjutnya').get('href'))
                if len(self.data) == 0:
                        echo("[*] no result found")
                        exit()
                else:
                        echo(f'{str(len(self.data))}). Retrieved ')
                        empty("[*] Press Enter to continue ")
                        for x in self.data:
                                Gas.Join(x)
                        echo("[*] Done ")
                        exit()
        def info(self,user,ids):
                data = parser(req.get(self.head.format(user),
                    headers=kuki).content,'html.parser')
                nama = data.find('title').text
                if "Error Facebook" in str(nama) or "Pesan Baru" in str(nama):
                        echo("[!] wrong id ")
                        exit()
                else:
                        echo("[*] "+nama)
                        pesan = input("         [*] Message : ")
                        limit = input("         [*] Limit : ")
                        Gas.Chat(nama,user,pesan,limit,ids)
        def sts(self,batas,pilih,tipe):
                if pilih == '1':
                        self.limit = batas
                        self.Dump_post(tipe)
                elif pilih == '2':
                        self.limit = batas
                        data = parser(req.get(self.head.format('/'+tipe),
                            headers=kuki).content,'html.parser')
                        self.nama = data.find('title').text.replace(' | Facebook','')
                        if 'Konten Tidak Ditemukan' in str(self.nama) or 'Halaman Tidak Ditemukan' in str(self.nama):
                                echo('[!] username wrong : '+tipe)
                                exit()
                        echo("[*] name : "+self.nama)
                        self.Dump_post('/'+tipe+'?v=timeline')
                elif pilih == '3':
                        echo("[*] Press Enter to see all group ")
                        query = input('     [*] query : ')
                        self.Grub_View(query)
                        if len(self.id) != 0:
                                user = int(input("     [*] Select : "))
                                user = self.id[user-1]
                                self.limit = input('     [*] limit : ')
                                self.Dump_post('/groups/'+user)
        def Req(self,pilih,set):
                self.pilih = pilih
                self.set = set
                if self.pilih == '1':
                        self.GetId('/friends/center/requests')
                elif self.pilih == '2':
                        self.GetId('/friends/center/requests')
        def auto_post(self,query):
                self.Grub_View(query)
                if len(self.id) != 0:
                        echo("[*] use comma (,) as separator. Example: 1,2,3,4")
                        pilih = input("     [*] Select number : ").split(',')
                        msg = input("     [*] messages : ")
                        
                        for x in pilih:
                                i = int(x)
                                id = self.id[i-1]
                                Gas.Post(self.head.format('/groups/'+str(id)),msg)
        def leave(self,query):
                self.Grub_View(query)
                if len(self.id) != 0:
                        echo("[*] use comma (,) as separator. Example: 1,2,3,4")
                        pilih = input("     [*] Select number : ").split(',')
                        echo(f"{str(len(pilih))}). selected ")
                        for x in pilih:
                                i = int(x)
                                id = self.id[i-1]
                                Gas.Leave(self.head.format('/group/leave/?group_id='+str(id)),id)
        def Cancel(self,link):
                get_user = parser(req.get(self.head.format(link),headers=kuki).content,'html.parser')
                if 'Batalkan Permintaan' in str(get_user):
                        for x in get_user.find_all('a',string='Batalkan Permintaan'):
                                self.data.append(x['href'])
                        print(f"\r         {str(len(self.data))}).retrieved .. ",end='')
                if 'Lihat selengkapnya' in str(get_user):
                        self.Cancel(get_user.find('a',string='Lihat selengkapnya').get('href'))
                if len(self.data) == 0:
                        echo("[!] no friend requests send ")
                        exit()
                print()
                empty("[*] press Enter to continue ")
                for i in self.data:
                        Gas.Cancel(i)

        def CekPost(self,post):
                _ = parser(req.get(post,headers=kuki).content,'html.parser').find('title').text
                if 'Halaman Tidak Ditemukan' in str(_):
                        empty("[!] post not found. please check your url post ")
                        self.ChekPost()
                else:
                        echo(f"[*] post : {_[:50]}")
                        msg = input('     [*] comment : ')
                        limit = input("     [*] limit : ")
                        Gas.Spam(post,msg,limit)
