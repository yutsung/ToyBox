"""
Ptt count your login times at most once a day,
this code can work with crontab on linux-like OS to help me
when someday I can't or forget to login
"""
import sys
import telnetlib
import time

import Account


def react_login(tnobj, signal, react):
    content = tnobj.read_very_eager().decode("big5", "ignore")
    if signal in content:
        tnobj.write((react+"\r\n").encode("big5"))
        time.sleep(1)
    else:
        print("No target string in screen")
        sys.exit()
    return tnobj


def login_ptt(account):
    tnobj = telnetlib.Telnet("ptt.cc")
    time.sleep(1)
    tnobj = react_login(tnobj, "請輸入代號", account.username)
    tnobj = react_login(tnobj, "請輸入您的密碼", account.passwd)
    content = tnobj.read_very_eager().decode("big5", "ignore")
    time.sleep(1)
    assert "歡迎您再度拜訪" in content
    #print("Login successful")

    tnobj.write("\r\n".encode("big5"))
    time.sleep(1)

    return tnobj

def main():
    account = Account.load_account()
    tnobj = login_ptt(account)
    tnobj.close()
    #print("Logout")

if __name__ == "__main__":
    main()

