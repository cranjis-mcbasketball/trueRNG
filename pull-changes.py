import subprocess as cmd
import time
from datetime import datetime


def pullGithubChanges():
    while True:

        cmd.run("git pull origin master", check=True, shell=True)
        now = datetime.now()
        print('completed pull ', now)
        time.sleep(600)


pullGithubChanges()
