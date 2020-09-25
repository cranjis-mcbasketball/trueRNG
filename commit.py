import subprocess as cmd
import time
from datetime import datetime

n = 1


def updateGithub():
    while True:
        cmd.run("git add .", check=True, shell=True)
        global n
        global_n = n + 1
        print(n, global_n)
        commit_cmd = "git commit -m 'NED_BYTES'" + str(n)
        print(commit_cmd)
        cmd.run(f"" + commit_cmd, check=True, shell=True)
        cmd.run("git push origin master", check=True, shell=True)
        now = datetime.now()
        print('completed commit: ', now)
        cmd.run("git reset --hard", check=True, shell=True)
        now = datetime.now()
        print('completed reset: ', now)
        n = n + 1
        time.sleep(10)
        print("%d squared is %d" % (10, 10*10))


updateGithub()
