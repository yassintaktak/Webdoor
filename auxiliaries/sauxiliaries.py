# Modules configuration file
# You can add your auxiliary here
available_auxiliaries = {
    "php_enc" : {
        "Name" : "PHP Encoder",
        "Version" : "0.1",
        "cfg_path" : "/phpencoder",
        "Description" : "PHP backdoor encoder",
        "Author" : "Yessine Taktak",
        "DefOptions" : ["Filepath", "", "1", "Backdoor's path"],
        "Options" : {
            "rows" : ["Option", "Value", "Required", "Description"],
            "columns" : ["Filepath", "", "1", "Backdoor's path"]
        },
        "DB_options" : {
            "Filepath" : {
                "i" : 1,
                "r" : 2
            }
        },
        "Help" : '''
            Weak, but efficient.
        '''
    }
}
