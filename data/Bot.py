# cek update

try:
        versi = '0.2'
        cek = req.get('https://raw.githubusercontent.com/XiuzSec/bot/master/README.md').text
        if versi in str(cek):
                up = ' * new version is available. type "update" to update'
                start = '[!] updating ..'
                
except: pass

def banner(login=False,nama=False):
        os.system('clear')
        logo=['''
        _______    _______   _______
       |   _   \  |   _   | |       |
       |.  1   /  |.  |   | |.|   | |
       |.  _   \  |.  |   | `-|.  |-'
       |:  1    \ |:  1   |   |:  |
       |::.. .  / |::.. . |   |::.| V0.1 Beta
       `-------'  `-------'   `---'  ''','''
        ______         _
        | ___ \       | |  
        | |_/ /  ___  | |_ 
        | ___ \ / _ \ | __|
        | |_/ /| (_) || |_ 
        \____/  \___/  \__|
                  V0.1 Beta''','''
       __________            __
        \______  \   ____  _/  |_
        |    |  _/  /  _ \ \   __\ 
        |    |   \ (  <_> ) |  |
        |______  /  \____/  |__|
               \/ V0.1 Beta''']
        print(random.choice(logo))
        if login:
                echo("  [*] Toolkit for Facebook [*]")
                #echo("  [*]  Author : zettamus   [*]")
                echo("  [*]        XiuzSec       [*]")
                print()
        elif nama:
            bot.nama()
def help():
        print('\n\n\n')
        tik("       ------------------information-------------------")
        print()
        tik("         [*] Author       : zettamus")
        tik("         [*] Desc         : Tools bot for facebook")
        tik("         [*] Team         : XiuzSec.")
        tik("         [*] Find me on")
        tik("             - Whatsapp   : 081242873775")
        tik("             - Telegram   : t.me/zettamus")
        tik("             - Facebook   : fb.me/zettamus.zettamus.3")
        tik("             - Github     : Github.com/zettamus")
        tik("         [*] Tutorial use this tool:")
        tik("             - https://youtube.com")
        print()
        tik("         For question, please contact me.")
        tik("       ------------------------------------------------")
        getpass("       Press Enter to main menu ")
        bot.cookies()
def echo(kata):
        print("     "+kata)
def empty(kata):
        getpass("     "+kata)
def tik(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random() * 0.001)
