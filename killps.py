#!/usr/bin/env python3

import psutil
import sys
import re


def psListFunc(psName):
    pslist = psutil.pids()
    psListMach = []
    for psid in pslist:
        p = psutil.Process(psid)
        if psName in p.name().lower():
            psListMach.append({p.name(): psid})
    return psListMach


def psTerminate(psList):
    if len(psList) == 1:
        for id in psList[0].values():
            psid = id
        p = psutil.Process(psid)
        p.terminate()
        p.wait()
    elif len(psList) > 1:
        print("Process list match:")
        psnum = 0
        for data in psList:
            for name in data.keys():
                print(f"{psnum}. {name}")
                psnum += 1

        try:
            psnum = int(input("Choice what process terminate (number): "))
        except KeyboardInterrupt:
            print("\nKeyboard Interruption")
            return None

        for id in psList[psnum].values():
            psid = id

        p = psutil.Process(psid)
        p.terminate()
        p.wait()
    else:
        print("the process not exist.")


def help():
    print("SCRIPT by chronologie")
    print("TERMINATE PROCESS SCRIPT HELP\n")
    print("use mode")
    print("example:\n")
    print("> terminate_process.py <process name>\n")
    print("The named process passed by argument that will be the name of this or\nthat it contains in its name will be stopped\n")
    print("The script only accepts one argument, two or more arguments will send\nyou to the help guide.\n")
    print("If two or more processes match the name passed as an argument, a list\nwill be displayed for you to choose the process you want to terminate.")


def run():
    psName = sys.argv[1].lower()
    psList = psListFunc(psName)
    psTerminate(psList)


def nameCheck():
    result = re.search(r"^[\w\.-]+$", sys.argv[1])
    if result == None:
        return False
    else:
        return True


sys.argv

if len(sys.argv) == 1 or len(sys.argv) > 2 or "?" in sys.argv[1]:
    help()
elif len(sys.argv) == 2:
    if nameCheck():
        run()
    else:
        print("process name format incorrect")
