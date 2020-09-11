
import subprocess as cmd
import time
from datetime import datetime



def updateGithub():
    while True:
        
        cmd.run("git add NED_BYTES", check=True, shell=True)
        cmd.run(f"git commit -m 'NED_BYTES'", check=True, shell=True)
        cmd.run("git push origin master", check=True, shell=True)
        now = datetime.now()
        print('completed commit: ', now)
        time.sleep(20)


updateGithub()