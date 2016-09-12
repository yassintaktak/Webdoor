def encrypt(files):
    try:
        script = open(files).read()
        script = script.replace("<?php", "")
        script = script.replace("?>", "")
        script = script.encode("base64")
        script = '$ALksqJEUYURjnDHDY="'+script+'";'
        finalscript = "<?php "+str(script)+"eval(base64_decode($ALksqJEUYURjnDHDY)); ?>"
        with open("Encrypted/bd.php", "w") as f:
            f.write(finalscript)
            f.close()
        print "[+] Script saved to 'Encrypted/bd.php'."
    except Exception as e:
        print "failed to execute enc.encrypt() : "+str(e)
