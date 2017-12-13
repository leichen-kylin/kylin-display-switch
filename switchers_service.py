#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import subprocess


class SwitchersService:

    def get_capslock_status(self):
        handle = subprocess.Popen("xset q", shell=True, stdout=subprocess.PIPE)
        handle.wait()
        res = handle.communicate()[0]
        capslock = res[res.find("Caps Lock:") + 9:]
        capslock = capslock[capslock.find("o"):capslock.find("o") + 2]

        if capslock == "on":
            return True
        else:
            return False

    def get_numlock_status(self):
        handle = subprocess.Popen("xset q", shell=True, stdout=subprocess.PIPE)
        handle.wait()
        res = handle.communicate()[0]
        numlock = res[res.find("Num Lock:") + 9:]
        numlock = numlock[numlock.find("o"):numlock.find("o") + 2]

        if numlock == "on":
            return True
        else:
            return False


def main():
    w = SwitchersService()
    print w.get_numlock_status()


if __name__ == '__main__':
    main()