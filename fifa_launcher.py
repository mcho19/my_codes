# objective of this script is to append the wording to bypass Fifa 17's autolauncher

from __future__ import print_function

with open("config.ini", "w") as config:  # need full path to the config.ini
    # pos1 = config.tell()
    # print(pos1)
    # config.seek(1,0)
    print("LAUNCH_EXE = fifa17.exe\nSETTING_FOLDER = 'FIFA 17'\nAUTO_LAUNCH = 1", file=config)

