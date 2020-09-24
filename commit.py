import subprocess as cmd
import time
from datetime import datetime


def updateGithub():
    while True:
        cmd.run("git add .", check=True, shell=True)
        cmd.run(f"git commit -m 'NED_BYTES'", check=True, shell=True)
        cmd.run("git push origin master", check=True, shell=True)
        now = datetime.now()
        print('completed commit: ', now)
        cmd.run("git reset --hard", check=True, shell=True)
        now = datetime.now()
        print('completed reset: ', now)
        time.sleep(600)


updateGithub()
