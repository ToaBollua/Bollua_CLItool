import random

banner1 = """\033[92m ___  ____ _    _    _  _ ____     ____ _    _ ___ ____ ____ _   
 |==] [__] |___ |___ |__| |--| ___ |___ |___ |  |  [__] [__] |___\n"""
 
banner2 =  """\033[92m                  
   __       _  _            __   _    _             _
  /  )     // //           /  )_//   | ) _/_       //
 /--<  __ // // . . __.   /    / ,---|/  /  __ __ // 
/___/_(_)</_</_(_/_(_/|__(__/ /___\_/ \_<__(_)(_)</_\n"""

banner3 = """\033[92m
Bollua_CLItool...\n"""

banner4 = """\033[92m
__                           __                         
|/  |      / /                /    /    / /              /
|___| ___ ( (       ___      (    (    ( (___  ___  ___ ( 
|   )|   )| | |   )|   )     |   )|   )| |    |   )|   )| 
|__/ |__/ | | |__/ |__/|     |__/ |__/ | |__  |__/ |__/ | 
                         ---                              
\n"""

banner5 = """\033[92m
.---.       .-.  .-.                       .--. .-.   .-. .-.             .-.  
: .; :      : :  : :                      : .--': :   : :.' `.            : :  
:   .' .--. : :  : :  .-..-. .--.         : :   : :   : :`. .' .--.  .--. : :  
: .; :' .; :: :_ : :_ : :; :' .; ;        : :__ : :__ : : : : ' .; :' .; :: :_ 
:___.'`.__.'`.__;`.__;`.__.'`.__,_; _____ `.__.':___.':_; :_; `.__.'`.__.'`.__;
                                   :_____:                                     
                                                                               
\n"""        

banner6 = """\033[92m
 ____        _ _                 ____ _     ___ _              _ 
| __ )  ___ | | |_   _  __ _    / ___| |   |_ _| |_ ___   ___ | |
|  _ \ / _ \| | | | | |/ _` |  | |   | |    | || __/ _ \ / _ \| |
| |_) | (_) | | | |_| | (_| |  | |___| |___ | || || (_) | (_) | |
|____/ \___/|_|_|\__,_|\__,_|___\____|_____|___|\__\___/ \___/|_|
                           |_____|                               
\n"""

banner7 = """\033[92m
01000010 01101111 01101100 01101100 01110101 01100001 01011111 01000011
01001100 01001001 01110100 01101111 01101111 01101100                  
\n"""

banner8 = """\033[92m
░█▀▄░█▀█░█░░░█░░░█░█░█▀█░░░░░█▀▀░█░░░▀█▀░▀█▀░█▀█░█▀█░█░░
░█▀▄░█░█░█░░░█░░░█░█░█▀█░░░░░█░░░█░░░░█░░░█░░█░█░█░█░█░░
░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀
\n"""

banner9 = """\033[92m
42 6F 6C 6C 75 61 5F 43 4C 49 74 6F 6F 6C
\n"""

banner10 = """\033[92m
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||B |||o |||l |||l |||u |||a |||_ |||C |||L |||I |||t |||o |||o |||l ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
\n"""

banner11 = """\033[92m
 _              _ ___     _ ____                 _ _        ____ 
| | ___   ___ _| |_ _|   | |___ \    _ __  _   _| | | ___  ( __ |
| |/ _ \ / _ |__ || |    | |   | |  | '_ \| | | | | |/ _ \ / _  |
| | (_) | (_) _| || | ___| |___| |  | |_) | |_| | | | (_) | (_| |
|_|\___/ \___|__/|___|_____|________|_.__/|_.__/|_|_|\___/ \____|
                               |_____|                           
\n"""

banner12 = """\033[92m
乃ㄖㄥㄥㄩ卂_匚ㄥ丨ㄒㄖㄖㄥ
\n"""             

banner13 = """\033[92m
𝔹𝕠𝕝𝕝𝕦𝕒_ℂ𝕃𝕀𝕥𝕠𝕠𝕝
\n"""

banner14 = """\033[92m
『B』『o』『l』『l』『u』『a』『_』『C』『L』『I』『t』『o』『o』『l』               
\n"""  

banner15 = """\033[92m
๒๏ɭɭยค_ςɭเՇ๏๏ɭ
\n"""       

banner16 = """\033[92m
__________       .__  .__                   _________ .____    .___  __                .__   
\______   \ ____ |  | |  |  __ _______      \_   ___ \|    |   |   |/  |_  ____   ____ |  |  
 |    |  _//  _ \|  | |  | |  |  \__  \     /    \  \/|    |   |   \   __\/  _ \ /  _ \|  |  
 |    |   (  <_> )  |_|  |_|  |  // __ \_   \     \___|    |___|   ||  | (  <_> |  <_> )  |__
 |______  /\____/|____/____/____/(____  /____\______  /_______ \___||__|  \____/ \____/|____/
        \/                            \/_____/      \/        \/                             
\n"""

banner17 = """\033[92m
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄     ▄▄   ▄▄ ▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄     
█  ▄    █       █   █   █   █   █  █ █  █      █  █       █   █   █   █       █       █       █   █    
█ █▄█   █   ▄   █   █   █   █   █  █ █  █  ▄   █  █       █   █   █   █▄     ▄█   ▄   █   ▄   █   █    
█       █  █ █  █   █   █   █   █  █▄█  █ █▄█  █  █     ▄▄█   █   █   █ █   █ █  █ █  █  █ █  █   █    
█  ▄   ██  █▄█  █   █▄▄▄█   █▄▄▄█       █      █  █    █  █   █▄▄▄█   █ █   █ █  █▄█  █  █▄█  █   █▄▄▄ 
█ █▄█   █       █       █       █       █  ▄   █  █    █▄▄█       █   █ █   █ █       █       █       █
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█  █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█
\n"""

banner18 = """\033[92m
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▀▄▄▀█░██░██░██░█░▄▄▀████░▄▄▀██░████▄░▄█▄░▄█▀▄▄▀█▀▄▄▀█░█
██░▄▄▀█░██░█░██░██░██░█░▀▀░████░█████░█████░███░██░██░█░██░█░█
██░▀▀░██▄▄██▄▄█▄▄██▄▄▄█▄██▄████░▀▀▄██░▀▀░█▀░▀██▄███▄▄███▄▄██▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
\n"""

banner19 = """\033[92m
╔══╗     ╔╗ ╔╗              ╔═══╗╔╗   ╔══╗ ╔╗         ╔╗ 
║╔╗║     ║║ ║║              ║╔═╗║║║   ╚╣╠╝╔╝╚╗        ║║ 
║╚╝╚╗╔══╗║║ ║║ ╔╗╔╗╔══╗     ║║ ╚╝║║    ║║ ╚╗╔╝╔══╗╔══╗║║ 
║╔═╗║║╔╗║║║ ║║ ║║║║╚ ╗║     ║║ ╔╗║║ ╔╗ ║║  ║║ ║╔╗║║╔╗║║║ 
║╚═╝║║╚╝║║╚╗║╚╗║╚╝║║╚╝╚╗    ║╚═╝║║╚═╝║╔╣╠╗ ║╚╗║╚╝║║╚╝║║╚╗
╚═══╝╚══╝╚═╝╚═╝╚══╝╚═══╝    ╚═══╝╚═══╝╚══╝ ╚═╝╚══╝╚══╝╚═╝
\n"""

banner20 = """\033[92m
░██▄░▄▀▄░█▒░░█▒░░█▒█▒▄▀▄░░░▄▀▀░█▒░░█░▀█▀░▄▀▄░▄▀▄░█▒░
▒█▄█░▀▄▀▒█▄▄▒█▄▄░▀▄█░█▀█▒░░▀▄▄▒█▄▄░█░▒█▒░▀▄▀░▀▄▀▒█▄▄
\n"""

banner21 = """\033[92m
▄▄▄▄·       ▄▄▌  ▄▄▌  ▄• ▄▌ ▄▄▄·    ▄▄· ▄▄▌  ▪  ▄▄▄▄▄            ▄▄▌  
▐█ ▀█▪ ▄█▀▄ ██•  ██•  █▪██▌▐█ ▀█   ▐█ ▌▪██•  ██ •██   ▄█▀▄  ▄█▀▄ ██•  
▐█▀▀█▄▐█▌.▐▌██ ▪ ██ ▪ █▌▐█▌▄█▀▀█   ██ ▄▄██ ▪ ▐█· ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ 
██▄▪▐█▐█▌.▐▌▐█▌ ▄▐█▌ ▄▐█▄█▌▐█▪ ▐▌  ▐███▌▐█▌ ▄▐█▌ ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄
·▀▀▀▀  ▀█▄▀▪.▀▀▀ .▀▀▀  ▀▀▀  ▀  ▀   ·▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
\n"""

banner22 = """\033[92m
                       mm     mm                                                                                     mm  
*@@@***@@m           *@@@   *@@@                              mm@***@m@*@@@@*    *@@@@*  @@                        *@@@  
  @@    @@             @@     @@                            m@@*     *@  @@        @@    @@                          @@  
  @@    @@  m@@*@@m    @@     @@  *@@@  *@@@   m@*@@m       @@*       *  @@        @@  @@@@@@   m@@*@@m   m@@*@@m    @@  
  @@***@mm @@*   *@@   !@     !@    @@    @@  @@   @@       @@           @@        @@    @@    @@*   *@@ @@*   *@@   !@  
  @!    *@ @@     @@   !@     !@    !@    @@   m@@@!@       @!m          @!     m  @!    @@    @@     @@ @@     @@   !@  
  !!    m@ @@     !@   !@     !@    !@    @!  @!   !@       *!@m     m*  @!    :@  @!    @!    @@     !@ @@     !@   !@  
  !:    *! !@     !!   !!     !!    !@    !!   !!!!:!       !!!          !!     !  !!    !!    !@     !! !@     !!   !!  
  !:    !! !!!   !!!   :!     :!    !!    !!  !!   :!       :!!:     !*  !:    !!  :!    !!    !!!   !!! !!!   !!!   :!  
: !: : : :  : : : :  : : :  : : :   :: !: :!: :!: : !:        : : : :! : :: !: : :!: :   ::: :  : : : :   : : : :  : : : 
                                                                                                                         
\n"""

banner23 = """\033[92m
┏━━┓┃┃┃┃┓┃┓┃┃┃┃┃┃┃┃┃┃┃━━━┓┓┃┃┃━━┓┏┓┃┃┃┃┃┃┃┓┃
┃┏┓┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┏━┓┃┃┃┃┃┫┣┛┛┗┓┃┃┃┃┃┃┃┃
┃┗┛┗┓━━┓┃┃┃┃┓┏┓━━┓┃┃┃┃┃┃┗┛┃┃┃┃┃┃┃┓┏┛━━┓━━┓┃┃
┃┏━┓┃┏┓┃┃┃┃┃┃┃┃┃┓┃┃┃┃┃┃┃┏┓┃┃┏┓┃┃┃┃┃┃┏┓┃┏┓┃┃┃
┃┗━┛┃┗┛┃┗┓┗┓┗┛┃┗┛┗┓┃┃┃┗━┛┃┗━┛┃┫┣┓┃┗┓┗┛┃┗┛┃┗┓
┗━━━┛━━┛━┛━┛━━┛━━━┛┃┃┃━━━┛━━━┛━━┛┗━┛━━┛━━┛━┛
┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃
┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃
\n"""

banner24 = """\033[92m
  (°_ʖ°)                                  (●>●)              (°з°)         _                            
oo_\/_oo________ ___\\   ___\\   ▼.ᴥ.▼__ __/____    (͡°͜ʖ͡°)__//   (°з°)_(•̪●)__ _______ _______ ___\\   
|  _    |       |   |ʖ°)|   |ʖ°)|  | |  |       |  |       |   |   |   |       |       |       |   |ʖ°) 
| |_|   |  ___  |   |/  |   |/  |  | |  |   _   |  |       |   |   8   8_     _8  ___  |  ___  |   |/   
|       | |▀-▀| |   8   |   8   |  |_|  |  |_|  |  |      _|   |   |   | |   | | |▀-▀| | |▀-▀| |   8    
|  _   || |___| |   |___|   |___|       |       |  |     | |   |___|   | |   | | |___| | |___| |   |___ 
| |_|   |       |       |       |       |   _   |  |     |_|       |   | |   | |       |       |       |
|_______|_______|_______|_______|_______|__| |__|  |_______|_______|___| |___| |_______|_______|_______|
\n"""

banner25 = """\033[92m
  ( .         (    (          (  (     (( (  .   .      
 ())  ( ( (   )\ : )\        ()) )\    ))\)\   (   ( (  
(_)() )\)\)\ ((_) (_()      ((_))(_) (((_)(_)  )\  )\)\ 
| _ )((_) | |(_))((_)()    (/ __| |  |_ _| |_ ((_)((_) |
| _ \ _ \ | | || | _` |    | (__| |__ | ||  _| _ \ _ \ |
|___/___/_|_|\_._|__/_|     \___|____|___|\__|___/___/_|
\n"""

banner26 = """\033[92m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░     ░░░░░░░░░░░░░░░░   ░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░░░   ░░░░░░░░   ░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░   
▒  ▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒   ▒   ▒▒▒▒▒▒▒▒   ▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
▒  ▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒   ▒   ▒   ▒▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒    ▒  ▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒   
▓      ▓▓▓▓▓   ▓▓   ▓▓   ▓   ▓   ▓▓   ▓▓   ▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓   ▓▓   ▓▓▓   ▓▓   ▓▓   
▓  ▓▓▓▓   ▓   ▓▓▓▓   ▓   ▓   ▓   ▓▓   ▓   ▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓   ▓▓▓▓   ▓   ▓▓▓▓   ▓   
▓  ▓▓▓▓▓  ▓▓   ▓▓   ▓▓   ▓   ▓   ▓▓   ▓   ▓▓▓   ▓▓▓▓▓▓▓▓▓   ▓▓▓   ▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓ ▓▓   ▓▓   ▓▓▓   ▓▓   ▓▓   
█    █   █████   █████   █   ███      ███   █    ██████████     ███          █   ████   █████   ████████   █████   
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████

\n"""

banner27 = """\033[92m
  ▄▄▄▄    ▒█████    ██▓     ██▓    █    ██  ▄▄▄          ▄████▄  ██▓     ██▄▄▄█████▓ ▒█████   ▒█████    ██▓   
 ▓█████▄ ▒██▒  ██▒ ▓██▒    ▓██▒    ██  ▓██▒▒████▄       ▒██▀ ▀█ ▓██▒   ▒▓██▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒ ▓██▒   
 ▒██▒ ▄██▒██░  ██▒ ▒██░    ▒██░   ▓██  ▒██░▒██  ▀█▄     ▒▓█    ▄▒██░   ░▒██▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒ ▒██░   
 ▒██░█▀  ▒██   ██░ ▒██░    ▒██░   ▓▓█  ░██░░██▄▄▄▄██    ▒▓▓▄ ▄██▒██░    ░██░ ▓██▓ ░ ▒██   ██░▒██   ██░ ▒██░   
▒░▓█  ▀█▓░ ████▓▒░▒░██████▒░██████▒▒█████▓ ▒▓█   ▓██    ▒ ▓███▀ ░██████ ░██  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░▒░██████
░░▒▓███▀▒░ ▒░▒░▒░ ░░ ▒░▓  ░░ ▒░▓  ░▒▓▒ ▒ ▒ ░▒▒   ▓▒█    ░ ░▒ ▒  ░ ▒░▓   ░▓   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░░ ▒░▓  
░▒░▒   ░   ░ ▒ ▒░ ░░ ░ ▒  ░░ ░ ▒  ░░▒░ ░ ░ ░ ░   ▒▒       ░  ▒  ░ ░ ▒    ▒     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░░ ░ ▒  
  ░    ░ ░ ░ ░ ▒     ░ ░     ░ ░   ░░░ ░ ░   ░   ▒      ░         ░ ░    ▒   ░      ░ ░ ░ ▒  ░ ░ ░ ▒     ░ ░  
░ ░          ░ ░  ░    ░  ░    ░     ░           ░      ░ ░         ░    ░              ░ ░      ░ ░  ░    ░  
\n"""


banner28 = """\033[92m
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄     ▄▄   ▄▄ ▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄     
█  ▄    █       █   █   █   █   █  █ █  █      █  █       █   █   █   █       █       █       █   █    
█ █▄█   █   ▄   █   █   █   █   █  █ █  █  ▄   █  █       █   █   █   █▄     ▄█   ▄   █   ▄   █   █    
█       █  █ █  █   █   █   █   █  █▄█  █ █▄█  █  █     ▄▄█   █   █   █ █   █ █  █ █  █  █ █  █   █    
█  ▄   ██  █▄█  █   █▄▄▄█   █▄▄▄█       █      █  █    █  █   █▄▄▄█   █ █   █ █  █▄█  █  █▄█  █   █▄▄▄ 
█ █▄█   █       █       █       █       █  ▄   █  █    █▄▄█       █   █ █   █ █       █       █       █
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█  █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█
\n"""
 
banner29 = """\033[92m
________      ___________                  __________________________            ______
___  __ )________  /__  /___  _______ _    __  ____/__  /____  _/_  /_______________  /
__  __  |  __ \_  /__  /_  / / /  __ `/    _  /    __  /  __  / _  __/  __ \  __ \_  / 
_  /_/ // /_/ /  / _  / / /_/ // /_/ /     / /___  _  /____/ /  / /_ / /_/ / /_/ /  /  
/_____/ \____//_/  /_/  \__,_/ \__,_/______\____/  /_____/___/  \__/ \____/\____//_/   
                                    _/_____/                                           
\n"""
 
banners = [banner1, banner2, banner3, banner4, banner5, banner6, banner7, banner8, banner9, banner10, banner11, banner12, banner13, banner14, banner15, banner16, banner17, banner18, banner19, banner20, banner21, banner22, banner23, banner24, banner25, banner26, banner27, banner28, banner29]
def test():
    result = random.choice(banners)
    print(result)