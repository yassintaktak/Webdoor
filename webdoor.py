#!/usr/bin/python
import sys, os
import urllib2, urllib
import re
import random, math
# Local imports #
sys.path.append(os.path.dirname(__file__) + "/Banners")
sys.path.append(os.path.dirname(__file__) + "/core")
sys.path.append(os.path.dirname(__file__) + "/modules")
sys.path.append(os.path.dirname(__file__) + "/auxiliaries")
sys.path.append(os.path.dirname(__file__) + "/handler")

# auxiliaries
sys.path.append(os.path.dirname(__file__) + "/auxiliaries/phpencoder")
# Script
import motd
import version
import smodules
import sauxiliaries
import shandler
import options
import generator
import handlero
import enc
# Code Core #
#
# __          ________ ____  _____   ____   ____  _____
# \ \        / /  ____|  _ \|  __ \ / __ \ / __ \|  __ \
#  \ \  /\  / /| |__  | |_) | |  | | |  | | |  | | |__) |
#   \ \/  \/ / |  __| |  _ <| |  | | |  | | |  | |  _  /
#    \  /\  /  | |____| |_) | |__| | |__| | |__| | | \ \
#     \/  \/   |______|____/|_____/ \____/ \____/|_|  \_\
#
#    Webdoor Web backdoor generator
#    By Yessine Taktak - Security outflow
#    Webdoor is for educational purpuses only, we (the team)
#    are not responsible for any low-breaking usage or any
#    damage you make.
#    This script is under LGPL licence, and it's completely
#    opensource, feel free to edit/improve/manage this tool
#    in any way you want.
#
#    Thanks to : Anonjoker
#    GREETINGS FROM TUNISIA.
# Code variables
current_command = "webdoor >>"
pre_startup = "\n"
usage_type = ""
chosen_result = ""
# Code functions
def Fail(function, message):
    try:
        print "Failed to execute "+str(function)+" : "+str(message)
    except:
        pass
def Banner():
    try:
        index = int(str(random.random()*len(motd.banners)).split(".")[0])
        print motd.banners[index]
        print "     { Version "+str(version.current_version)+" }"
        print "     { By "+str(version.current_authors)+" - "+str(version.current_teams)+" }"
        print "     { "+str(len(smodules.available_modules))+" Available module(s) }"
        print "     { "+str(len(sauxiliaries.available_auxiliaries))+" Available auxiliary(ies) }"
        print "     { "+str(len(shandler.available_handlers))+" Available handler(s) }"
    except Exception as e:
        Fail("Banner()", e)
def parseCommand(command):
    try:
        global current_command, usage_type, chosen_result
        if(command == "help"):
            if(usage_type == ""):
                version.show_help()
            else:
                if(usage_type == "module"):
                    module = smodules.available_modules[chosen_result]
                    print module["Help"]
                elif(usage_type == "auxiliary"):
                    auxiliary = sauxiliaries.available_auxiliaries[chosen_result]
                    print auxiliary["Help"]
                elif(usage_type == "handler"):
                    handler = shandler.available_handlers[chosen_result]
                    print handler["Help"]
        elif(command == "exit"):
            sys.exit(0)
        elif(command == "clear"):
            os.system('cls' if os.name == 'nt' else 'clear')
        elif(command == "unuse"):
            if usage_type == "module" :
                smodules.available_modules[chosen_result]["Options"]["columns"] = smodules.available_modules[chosen_result]["DefOptions"]
            elif usage_type == "auxiliary" :
                sauxiliaries.available_auxiliaries[chosen_result]["Options"]["columns"] = sauxiliaries.available_auxiliaries[chosen_result]["DefOptions"]
            elif usage_type == "handler" :
                shandler.available_handlers[chosen_result]["Options"]["columns"] = shandler.available_handlers[chosen_result]["DefOptions"]
            usage_type = ""
            chosen_result = ""
            current_command = "webdoor >>"
        elif(command == "run"):
            if(usage_type == "module"):
                generator.generate(smodules.available_modules[chosen_result])
                pass
            elif(usage_type == "handler"):
                handlero.handle(shandler.available_handlers[chosen_result])
                pass
            elif(usage_type == "auxiliary"):
                if(chosen_result == "php_enc"):
                    enc.encrypt(sauxiliaries.available_auxiliaries["php_enc"]["Options"]["columns"][1])
                pass
        else:
            if(len(command.split(":")) == 2):
                commande = re.findall("(.*?):(.*?);", command)
            else:
                commande = re.findall("(.*?):(.*?):(.*?);", command)
            if(len(commande) > 0):
                cmd = commande[0][0]
                value = commande[0][1]
                if(len(command.split(":")) == 3):
                    svalue = commande[0][2]
                if(cmd == "color"):
                    if(os.name == 'nt'):
                        os.system("color "+str(value))
                    else:
                        print "[-] The color command is for windows systems only."
                elif(cmd == "exec"):
                    os.system(value)
                elif(cmd == "eval"):
                    print eval(value)
                elif(cmd == "use"):
                    chosen = 0
                    for module in smodules.available_modules:
                        if(module == value):
                            usage_type = "module"
                            current_command = "webdoor["+str(value)+"] >>"
                            chosen_result = value
                            chosen = 1
                            break
                    if(chosen == 0):
                        for auxiliary in sauxiliaries.available_auxiliaries:
                            if(auxiliary == value):
                                usage_type = "auxiliary"
                                current_command = "webdoor["+str(value)+"] >>"
                                chosen_result = value
                                chosen = 1
                                break
                    if(chosen == 0):
                        for handler in shandler.available_handlers:
                            if(handler == value):
                                usage_type = "handler"
                                current_command = "webdoor["+str(value)+"] >>"
                                chosen_result = value
                                chosen = 1
                                break
                    if(chosen == 0):
                        print "[-] There's no entry called '"+str(value)+"'"
                elif(cmd == "search"):
                    print "Entry name               Entry type"
                    for entry in smodules.available_modules:
                        if(value in entry or value in smodules.available_modules[entry]["Name"] or value in smodules.available_modules[entry]["Description"] or value in smodules.available_modules[entry]["Author"]):
                            print entry+"               Module"
                    for entry in sauxiliaries.available_auxiliaries:
                        if(value in entry or value in sauxiliaries.available_auxiliaries[entry]["Name"] or value in sauxiliaries.available_auxiliaries[entry]["Description"] or value in sauxiliaries.available_auxiliaries[entry]["Author"]):
                            print entry+"               Auxiliary"
                    for entry in shandler.available_handlers:
                        if(value in entry or value in shandler.available_handlers[entry]["Name"] or value in shandler.available_handlers[entry]["Description"] or value in shandler.available_handlers[entry]["Author"]):
                            print entry+"               Handler"
                elif(cmd == "interact"):
                    if(len(handlero.sessions) > int(value)):
                        handlero.interact(value)
                elif(cmd == "show"):
                    if(value == "about" and usage_type == ""):
                        version.show_about()
                    elif(value == "sessions"):
                        sessions = []
                        i = 0
                        for session in handlero.sessions:
                            sessions.append(str(i))
                            sessions.append(session.options("host"))
                            i += 1
                        options.table(["Session ID", "Session "], sessions)
                    elif(value == "about" and usage_type != ""):
                        if(usage_type == "module"):
                            module = smodules.available_modules[chosen_result]
                            version.entry_about(module["Name"], module["Version"], module["Description"], module["Author"])
                        elif(usage_type == "auxiliary"):
                            auxiliary = sauxiliaries.available_auxiliaries[chosen_result]
                            version.entry_about(auxiliary["Name"], auxiliary["Version"], auxiliary["Description"], auxiliary["Author"])
                        elif(usage_type == "handler"):
                            handler = shandler.available_handlers[chosen_result]
                            version.entry_about(handler["Name"], handler["Version"], handler["Description"], handler["Author"])
                    elif(value == "options" and usage_type != ""):
                        if(usage_type == "module"):
                            module = smodules.available_modules[chosen_result]
                            options.table(module["Options"]["rows"], module["Options"]["columns"])
                        elif(usage_type == "auxiliary"):
                            auxiliary = sauxiliaries.available_auxiliaries[chosen_result]
                            options.table(auxiliary["Options"]["rows"], auxiliary["Options"]["columns"])
                        elif(usage_type == "handler"):
                            handler = shandler.available_handlers[chosen_result]
                            options.table(handler["Options"]["rows"], handler["Options"]["columns"])
                    elif(value == "modules"):
                        modules = []
                        for module in smodules.available_modules:
                            modules.append(module)
                            modules.append(smodules.available_modules[module]["Name"])
                        options.table(["Entry", "Name"], modules)
                        modules = []
                    elif(value == "xmodules"):
                        print "Entry             Name             Description"
                        for module in smodules.available_modules:
                            print module+"             "+smodules.available_modules[module]["Name"]+"             "+smodules.available_modules[module]["Description"]
                    elif(value == "auxiliaries"):
                        auxiliaries = []
                        for auxiliary in sauxiliaries.available_auxiliaries:
                            auxiliaries.append(auxiliary)
                            auxiliaries.append(sauxiliaries.available_auxiliaries[auxiliary]["Name"])
                        options.table(["Entry", "Name"], auxiliaries)
                        auxiliaries = []
                    elif(value == "xauxiliaries"):
                        print "Entry             Name             Description"
                        for auxiliary in sauxiliaries.available_auxiliaries:
                            print auxiliary+"             "+sauxiliaries.available_auxiliaries[auxiliary]["Name"]+"             "+sauxiliaries.available_auxiliaries[auxiliary]["Description"]
                    elif(value == "handlers"):
                        handlers = []
                        for handler in shandler.available_handlers:
                            handlers.append(handler)
                            handlers.append(shandler.available_handlers[handler]["Name"])
                        options.table(["Entry", "Name"], handlers)
                        handlers = []
                    elif(value == "xhandlers"):
                        print "Entry             Name             Description"
                        for handler in shandler.available_handlers:
                            print handler+"             "+shandler.available_handlers[handler]["Name"]+"             "+shandler.available_handlers[handler]["Description"]
                elif(cmd == "set"):
                        if(usage_type == "module"):
                            module = smodules.available_modules[chosen_result]
                            optionse = module["DB_options"]
                            for option in optionse:
                                if(option == value):
                                    db_index = module["DB_options"][value]
                                    module["Options"]["columns"][db_index["i"]] = svalue
                                    break
                        elif(usage_type == "auxiliary"):
                            auxiliary = sauxiliaries.available_auxiliaries[chosen_result]
                            optionse = auxiliary["DB_options"]
                            for option in optionse:
                                if(option == value):
                                    db_index = auxiliary["DB_options"][value]
                                    auxiliary["Options"]["columns"][db_index["i"]] = svalue
                                    break
                        elif(usage_type == "handler"):
                            handler = shandler.available_handlers[chosen_result]
                            optionse = handler["DB_options"]
                            for option in optionse:
                                if(option == value):
                                    db_index = handler["DB_options"][value]
                                    handler["Options"]["columns"][db_index["i"]] = svalue
                                    break
                elif(cmd == "unset"):
                    if(usage_type == "module"):
                        module = smodules.available_modules[chosen_result]
                        optionse = module["DB_options"]
                        for option in optionse:
                            if(option == value):
                                db_index = module["DB_options"][value]
                                module["Options"]["columns"][db_index["i"]] = ""
                                break
                    elif(usage_type == "auxiliary"):
                        auxiliary = sauxiliaries.available_auxiliaries[chosen_result]
                        optionse = auxiliary["DB_options"]
                        for option in optionse:
                            if(option == value):
                                db_index = auxiliary["DB_options"][value]
                                auxiliary["Options"]["columns"][db_index["i"]] = ""
                                break
                    elif(usage_type == "handler"):
                        handler = shandler.available_handlers[chosen_result]
                        optionse = handler["DB_options"]
                        for option in optionse:
                            if(option == value):
                                db_index = handler["DB_options"][value]
                                handler["Options"]["columns"][db_index["i"]] = ""
                                break
                else:
                    print "[-] There's no command called '"+str(command)+"'"

            else:
                print "[-] There's no command called '"+str(command)+"'"
    except Exception as e:
        Fail("parseCommand()", e)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    Banner()
    if(len(sys.argv) < 2):
        while True:
            command = raw_input(pre_startup+current_command)
            parseCommand(command)
            pre_startup = ""
    else:
        try:
            code = open(sys.argv[1]).readlines()
            for line in code:
                line = line.rstrip()
                parseCommand(line)
                pre_startup = ""
        except:
            print "[-] No file specified, quiting."
            sys.exit(0)
