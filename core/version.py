# Script reserved variables
# Do not change anything here
# otherwise you'll change the
# execution flow of the script
current_version = "0.1"
current_authors = "Yassin Taktak"
current_teams = "Security outflow"

def entry_about(name, version, description, author):
    try:
        print str(name)+" V "+str(version)+" By "+str(author)
        print description
    except Exception as e:
        print "failed to execute version.entry_about() : "+str(e)
def show_about():
    try:
        print "Webdoor "+str(current_version)+" By "+str(current_authors)
        print "Brought you by : "+str(current_teams)
        print "This project is for educational purpuses only, we are not responsible for any damage you make."
    except Exception as e:
        print "failed to execute version.show_about() : "+str(e)
def show_help():
    print '''
        + Console basic commands
        help - display help SCREEN
        exit - exit console
        clear - clear console
        color:<color>; - change console color (windows systems only)
        exec:<cmd>; - execute system command
        eval:<string>; - evaluate Python script
        search:<entry> - search for entries
        + Webdoor basic commands
        use:<module>/<auxiliary>/<handler>; - use module/auxiliary or handler name
        show:options; - show module/auxiliary or handler options
        show:about; - show information about the current module/auxiliary or handler
        show:sessions; - show a list of open sessions
        interact:<session> - interract with a session
        unuse - go to the initial screen
        set:<option>:value; - set module/auxiliary option
        unset:<option> - unset option
        run - generate backdoor/run handler-auxiliary
        + Auxiliary/Handler/Module basic commands
        back - exit auxiliary/handler/module console
        clean - clean console
        help - display module/auxiliary/handler help screen
    '''
