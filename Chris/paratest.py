import paramiko,time
from scp import SCPClient



username = 'robot'
server = '192.168.1.17'
password = 'maker'

gSSHRef = paramiko.SSHClient()
gSSHRef.set_missing_host_key_policy(paramiko.AutoAddPolicy())
result = gSSHRef.connect(server, username=username, password=password, timeout = 5)
reply = str(result)
print(reply)
gchannel = gSSHRef.invoke_shell()
chan = gSSHRef.get_transport().open_session()
# print(chan.recv_exit_status())
gchannel.settimeout(0)
scp = SCPClient(gSSHRef.get_transport())
print(reply)

def CloseSSH():
    if gchannel != None:
        gchannel.close()
    if gSSHRef != None:
        gSSHRef.close()
    if scp != None:
        scp.close()
    return('done')
def WriteSSH(string):
    reply = 'no reference'
    if gSSHRef != None:
        reply = 'no file'
        if gchannel != None:
            size = gchannel.send(string.encode())
            reply = str(size)
    return reply
def ReadSSH():
    reply = 'no reference'
    if gSSHRef != None:
        reply = 'no file'
        if gchannel != None:
            reply = ''
            if gchannel.recv_ready():
                reply = gchannel.recv(9999).decode()
    return(reply)
def WriteWaitReadSSH(string,char,timeout=10000):
     reply = ReadSSH()
     WriteSSH(string)
     n = int(timeout/10)
     for i in range(n):
         ans = ReadSSH()
         reply = reply + ans
         if ans.find(char) >= 0:
             print(ans)
             return 'test\n>> ' + str(ans.find(char)) +'\n' + ans
         time.sleep(0.01)
     return reply
def scp_get(name):
     try:
          scp.get(name)
          return 'get succeeded\n'
     except Exception as e:
          return  'scp.get('+name+')\n' +str(e)
def scp_put(source, dest):
     try:
          scp.put(source, dest)
          return 'scp.put('+source+','+dest+')\n' +'put succeeded\n'
     except Exception as e:
          return str(e)
def scp_put_all(source, dest):
     try:
          scp.put(source, recursive = True, remote_path = dest)
          return 'put succeeded\n'
     except Exception as e:
          return str(e)

reply = WriteWaitReadSSH('\r','$',15000)
print(reply)
time.sleep(1)
reply = WriteWaitReadSSH('brickrun -r --  pybricks-micropython\n','>',6000)
print(reply)
time.sleep(5)
reply = WriteWaitReadSSH('ddd\n','>',5000)
print(reply)
CloseSSH()