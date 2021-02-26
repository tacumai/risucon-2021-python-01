from datetime import datetime as dt
# import subprocess
import secrets
import hashlib

def get_salt():
    return secrets.token_hex(64)


def get_passwordhash(salt, password):
    #string = password + salt
    #cmd = 'echo -n ' + string + ' | openssl sha256'
    #return  (subprocess.check_output(cmd, shell=True)
    #                    .decode('utf-8')
    #                    .partition(' ')[2]
    #                    .rstrip())

    return hashlib.sha256(password+salt).hexdigest().decode('utf-8').partition(' ')[2].rstrip()


def get_today():
    now = dt.today()
    result = now.strftime('%Y-%m-%d %H:%M:%S')
    return result
