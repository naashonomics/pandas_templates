from datetime import datetime
import os,glob,subprocess,pexpect


try:
    var_command = "scp <file1> user@host:<file2>"
    var_child = pexpect.spawn(var_command)
    i = var_child.expect(["password:", pexpect.EOF])
    if i==0: # send password            
        print('Sending: <file1> to <file2>' )    
        var_child.sendline("<password>")
        var_child.expect(pexpect.EOF)
    elif i==1:
        print("Got the key or connection timeout")
        pass
except Exception as e:
    print("Oops Something went wrong buddy")
    print(e)
