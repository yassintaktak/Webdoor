# Modules configuration file
# You can add your handler here
available_handlers = {
    "php_connect" : {
        "Name" : "PHP OWN3R Handler",
        "Version" : "0.1",
        "cfg_path" : "/phpc",
        "Description" : "PHP OWN3R connection handler",
        "Author" : "Yessine Taktak",
        "DefOptions" : ["BackdoorURL", "", "1", "Backdoor's URL", "Password", "", "0", "Backdoor's password", "SSL", "False", "0", "Using HTTPS/SSL"],
        "Options" : {
            "rows" : ["Option", "Value", "Required", "Description"],
            "columns" : ["BackdoorURL", "", "1", "Backdoor's URL", "Password", "", "0", "Backdoor's password", "SSL", "False", "0", "Using HTTPS/SSL"]
        },
        "DB_options" : {
            "BackdoorURL" : {
                "i" : 1,
                "r" : 2
            },
            "Password" : {
                "i" : 5,
                "r" : 6
            },
            "SSL" : {
                "i" : 9,
                "r" : 10
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

   PHP OWN3R HANDLER
        '''
    },
    "sphp_connect" : {
        "Name" : "PHP S1L3NT Handler",
        "Version" : "0.1",
        "cfg_path" : "/sphp",
        "Description" : "PHP S1L3NT connection handler",
        "Author" : "Yessine Taktak",
        "DefOptions" : ["BackdoorURL", "", "1", "Backdoor's URL", "SSL", "False", "0", "Using HTTPS/SSL"],
        "Options" : {
            "rows" : ["Option", "Value", "Required", "Description"],
            "columns" : ["BackdoorURL", "", "1", "Backdoor's URL", "SSL", "False", "0", "Using HTTPS/SSL"]
        },
        "DB_options" : {
            "BackdoorURL" : {
                "i" : 1,
                "r" : 2
            },
            "SSL" : {
                "i" : 5,
                "r" : 6
            }
        },
        "Help" : '''

    PHP S1L3NT HANDLER
        '''
    }
}
