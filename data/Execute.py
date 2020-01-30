#!/usr/bin/env python3
# XiuzSec team
# Zettamus
class Main:
        def __init__(self):
                self.failed = 0
                self.hitung = 0
                self.success = 0
                self.head = 'https://mbasic.facebook.com{}'
        def comment_post(self,url,teks):
                data_post = []
                data = parser(req.get(url,
                    headers=kuki).content,'html.parser')
                nama = data.find('title').text
                for x in data('form'):
                        if 'a/comment.php?' in x['action']:
                                data_post.append(x['action'])
                                break
                for i in data('input'):
                        try:
                                if 'fb_dtsg' in i['name']:
                                        data_post.append(i['value'])
                                if 'jazoest' in i['name']:
                                        data_chat.append(i['value'])
                                        break
                        except: pass
                if len(data_post) == 3:
                        url = self.head.format(data_post[0])
                        form = {'fb_dtsg':data_post[1],
                                'jazoest':data_post[2],
                                'comment_text': teks}
                        auto = req.post(url,
                                data=form,
                                headers=kuki)
                        if auto.status_code == 200:
                                echo(f"[*] {nama[:50]}")
                        else:
                                echo(f'[!] {nama[:50]}')
                else:
                        echo(f'[!] {nama[:50]}')
        def Chat(self,name,url,msg,limit,id):   
                self.hitung = 0
                data_chat = []
                asu = parser(req.get(self.head.format(url),
                    headers=kuki).content,'html.parser')
                for x in asu('form'):
                        if '/messages/send/?' in x['action']:
                                data_chat.append(x['action'])
                for i in asu('input'):
                        try:
                                if 'fb_dtsg' in i['name']:
                                        data_chat.append(i['value'])
                                if 'jazoest' in i['name']:
                                        data_chat.append(i['value'])
                                        break
                        except: pass
                if len(data_chat) == 3:
                        kirim = self.head.format(data_chat[0])
                        if 'cid.c.' in str(url):
                                form = {'fb_dtsg':data_chat[1],
                                        'jazoest':data_chat[2],
                                        'ids['+str(id)+']':str(id),
                                        'body':msg,
                                        'send':'Kirim'}
                        if 'cid.g.' in str(url):
                                form = {'fb_dtsg':data_chat[1],
                                        'jazoest':data_chat[2],
                                        'tids':'cid.g.'+id,
                                        'body':msg,
                                        'send':'Kirim'}
                        for ulang in range(int(limit)):
                                send = req.post(kirim,
                                        data=form,
                                        headers=kuki)
                                if 'send_success' in str(send.text):
                                        self.hitung += 1
                                else:
                                        self.failed += 1
                                print(f"\r     {name}). success: {str(self.hitung)} failed: {str(self.failed)}",end='')
                else:
                        echo(str(data_chat))
                        self.failed += 1
        def Cancel(self,link):
                id = link.split('=')[1].split('&')[0]
                nama = parser(req.get(self.head.format('/profile.php?id='+id),headers=kuki).content,'html.parser').find('title').text.replace(' | Facebook','').replace('Masuk Facebook','Uknown')
                if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(nama):
                        echo("[!] Your account has been temporarily suspended for using this feature")
                        exit()
                batal = req.get(self.head.format(link),headers=kuki)
                if batal.status_code == 200:
                        self.hitung += 1
                echo(f"{str(self.hitung)}. {nama} => Cancelled ")
        def Post(self,link,msg):
                data_post = []
                asu = parser(req.get(link,
                    headers=kuki).content,
                    'html.parser')
                nama = asu.find('title').text
                print(f"\r     [*] Opening {nama} ",end='')
                for x in asu('form'):
                        if "/composer/mbasic/?" in x['action']:
                                data_post.append(x['action'])
                for i in asu('input'):
                      
                        try:
                                if 'fb_dtsg' in i['name']:
                                        data_post.append(i['value'])
                                if 'jazoest' in i['name']:
                                        data_post.append(i['value'])
                        except: pass
                if len(data_post) == 3:
                        url = self.head.format(data_post[0])
                        
                        form = {'fb_dtsg':data_post[1],
                                'jazoest':data_post[2],
                                'xc_message': msg,
                                'target':link.split('/')[4],
                                'c_src':'group',
                                'referrer':'group',
                                'view_post':'Kirim'}
                        kirim = req.get(url,data=form,headers=kuki)
                        
                        if kirim.status_code == 200:
                            print(" ..success")

        def Leave(self,link,grup):
                data = []
                _ = parser(req.get(link,headers=kuki).content,'html.parser')
                for x in _('form'):
                        if '/a/group/leave/?' in x['action']:
                                data.append(x['action'])
                for i in _('input'):
                        try:
                                if 'fb_dtsg' in i['name']:
                                        data.append(i['value'])
                                if 'jazoest' in i['name']:
                                        data.append(i['value'])
                                        break
                        except: pass
                if len(data) == 3:
                        url = self.head.format(data[0])
                        form = {'fb_dtsg':data[1],
                                'jazoest':data[2],
                                'group_id':grup,
                                'confirm':'Keluar dari Group'}
                        bs1 = req.post(url,data=form,headers=kuki)
                        bs2 = parser(bs1.content,'html.parser')
                        bs3 = bs2.find('title').text.replace(' | Facebook','').replace('Grup Publik','')
                        if 'Gabung ke Grup' in str(bs2):
                                echo(f'[*] success leave {bs3}')
                        else:
                                echo(f"[*] failed leave {bs3}")
                else:
                        echo(f"[*] failed leave {grup}")
        def Spam(self,url,pesan,lop):
                data = []
                count = 0
                _ = parser(req.get(url,
                    headers=kuki).content,'html.parser')
                for asu in _('form'):
                        if 'a/comment.php?' in asu['action']:
                                data.append(asu['action'])
                                break
                for x in _('input'):
                        try:
                                if 'fb_dtsg' in x['name']:
                                        data.append(x['value'])
                                if 'jazoest' in x['name']:
                                        data.append(x['value'])
                                        break
                        except: pass
                if len(data) == 3:
                        link = self.head.format(data[0])
                        form = {'fb_dtsg':data[1],
                                'jazoest':data[2],
                                'comment_text':pesan}
                        for ulang in range(int(lop)):
                                send = req.post(link,
                                        data=form,
                                        headers=kuki)
                                if send.status_code == 200:
                                        count += 1
                                print(f'\r        {str(count)}). sending',end='')
        def Join(self,url):
                data = []
                id = url.replace('?refid=46','').split('/')[-1]
                try:
                        _ = parser(req.get(url,headers=kuki).content,'html.parser')
                        gfid = _.find('form', action = lambda _: "gfid"in _).get('action')
                        for x in _('input'):
                                try:
                                        if 'fb_dtsg' in x['name']:
                                                data.append(x['value'])
                                        if 'jazoest' in x['name']:
                                                data.append(x['value'])
                                                break
                                except: pass
                        if len(data) == 2:
                                link = self.head.format(gfid)
                                form = {
                                        'fb_dtsg':data[0],
                                        'jazoest':data[1],
                                        'None':'Gabung ke Grup'
                                        }
                                ex = req.post(link,data=form,headers=kuki)
                                cek = req.get(url,headers=kuki).text
                                if 'Tindakan Diblokir' in str(ex.text):
                                        print()
                                        echo("[!] Your account has been temporarily suspended for using this feature")
                                        exit()
                                elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(ex.text):
                                        print()
                                        echo("[!] Your account has been temporarily suspended for using this feature")
                                        exit()
                                if 'Batalkan Permintaan' in str(cek):
                                        self.success += 1
                                print(f'\r     [*] success send requests : {str(self.success)}',end='')
                except IOError: pass
