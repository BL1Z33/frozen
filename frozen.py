this = "frozen.py"
import os
if os.path.exists("frozencfg.py"):
    pass
else:
    with open("frozencfg.py", "w") as cfg:
        cfg.write("version=\"1.0.0\"\n")
        cfg.write("printmsg=\"Hello World!\"")
import frozencfg as frozen
os.system(f"title frozen v{frozen.version}")
while True:
    command = input("frozen: ")
    if command.startswith("dlfile "):
        parts = command.split(" ")
        if len(parts) != 3:
            print("Invalid command. Usage: dlfile [format] [link]")
            continue
        fileformat, filelink = parts[1], parts[2]
        os.system(f"powershell -Command iwr -Uri {filelink} -OutFile dl.{fileformat}")
        print(f"Saved file to dl.{fileformat}")
    elif command == "dlfile":
        print("Invalid command. Usage: dlfile [format] [link]")
    elif command == "print":
        print(frozen.printmsg)
    elif command == "reload":
        os.system(f"python {this}")
    elif command == "deletecfg":
        os.system("del frozencfg.py /S /Q")
        os.system(f"python {this}")
    else:
        print("Invalid command.")