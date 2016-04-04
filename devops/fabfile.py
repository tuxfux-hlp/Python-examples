from fabric.api import run,settings,hide,task,env,roles,hosts
from fabric.colors import red,green
import re
import sys

env.user=['root']
env.password=['password']

# few more options to think about.

#env.hosts=['localhost','192.168.1.8']
#env.users=['root','key2gyaan']
#env.passwords=['linuxrocks','redhat']

def trim(var):
  reg = re.compile('\n',re.M)
  reg.sub('',var)

@task
def host_type():
  with settings(
    hide('warnings','running','stderr'),
    warn_only=True
    ):
        output=run('uname -s')
        return trim(output)

@task
@hosts('root@192.168.1.8')
def upme():
  run('uptime')

def exec_remote_cmd(cmd):
  with settings(
    #hide('warnings','running','stderr','output'),
    hide('everything'),
    warn_only=True
    ):
      return run(cmd)

@task
@hosts('root@192.168.1.8')
def e_uptime():
  cmdlist={'uptime':'uptime','kernel':'uname -a','cpus':'cat /proc/cpuinfo|grep -i processor|wc -l'}
  print " ******** OS command ************** "
  for key,cmd in cmdlist.items(): 
    results = exec_remote_cmd(cmd)
    if results.succeeded:
      sys.stdout.write(green('\n* Command succeeded: ' +key+'\n'))
      sys.stdout.write(results+"\n")
    else:
      sys.stdout.write('\n* Command failed: '+cmd+'\n')
      sys.stdout.write(results+"\n")


