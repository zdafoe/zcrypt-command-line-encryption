""" 
This is the third version of zcrypt an encryption program made with python and C++ by me: Zech Dafoe
when using the program the syntax is: filename, password, and an optional third argument for keylength that defaults to 30 and must be an even number
an example of its usage:
                   filename    password   keylength(optional)
python zcrypt3.py   me.png     iforgot    30
"""



import base64, random, sys, time,os
from multiprocessing import Process,Queue,Value,freeze_support


def encryption(string,key,queue,direction,progressval,keylength,processnum,C_executablename):
    '''this function calls the C++ executable to do the acutal encrypting'''
    #make file to transfer data to C++ executable
    writefile=open('spliced.tmp'+str(processnum),'w')
    writefile.write(string)
    writefile.close()
    #call executable
    x=0
    for y in key:
        key[x]=str(y)
        x+=1
    key='`'.join(key)
    var=os.system(f'{C_executablename} 2 {key} {direction} {keylength} {processnum}')
    #get processed string from transfer file
    string=open('spliced.tmp'+str(processnum)).read()
    os.remove('spliced.tmp'+str(processnum))

    queue.put(string)
#function called for encryping a file args are the base64 encoded file and the password
def encrypt(file,pas,keylength,C_executablename,buffer):
    '''function creates key from password and starts processes for encrypting a base 64 string'''
    if buffer:
        file=file+'Z'*200
    direction=0
    print('_'*60)
    #creates the key for encryption using the password to seed the random number generator
    random.seed(pas)
    key=[]
    while keylength%2!=0:
        keylength=int(input('please enter valid keylength'))
    for num in range(keylength):
        key.append(random.randint(2,int(len(file)*.12)))
        key.append(random.randint(0,1))
        key.append(random.randint(2,20))
        key.append(random.randint(0,1))

    writefile=open('spliced.tmp','w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 1')
    files=open('spliced.tmp').read().split('*/|/*')
    os.remove('spliced.tmp')
    file1=files[0]
    file2=files[1]
    file3=files[2]
    file4=files[3]
    key1=key[0:int(len(key)/4)]
    key2=key[int(len(key)/4):int(len(key)/2)]
    key3=key[int(len(key)/2):int(3*(len(key)/4))]
    key4=key[int(3*(len(key)/4)):len(key)]

    progressval=Value('i')
    queue1=Queue()
    queue2=Queue()
    queue3=Queue()
    queue4=Queue()
    p1=Process(target=encryption,args=(file1,key1,queue1,direction,progressval,keylength,1,C_executablename))
    p2=Process(target=encryption,args=(file2,key2,queue2,direction,progressval,keylength,2,C_executablename))
    p3=Process(target=encryption,args=(file3,key3,queue3,direction,progressval,keylength,3,C_executablename))
    p4=Process(target=encryption,args=(file4,key4,queue4,direction,progressval,keylength,4,C_executablename))
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    mixed1=queue1.get()
    mixed2=queue2.get()
    mixed3=queue3.get()
    mixed4=queue4.get()
    file=mixed1+'`'+mixed2+'`'+mixed3+'`'+mixed4
    writefile=open('spliced.tmp','w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 0')
    final=open('spliced.tmp').read()
    os.remove('spliced.tmp')

    return final
#same as above function but for decrypting
def decrypt(file,pas,keylength,C_executablename):
    '''function creates key from password and starts processes for decrypting a base 64 string'''
    direction=1
    print('_'*60)
    #creates the key for encryption using the password to seed the random number generator
    random.seed(pas)
    key=[]
    while keylength%2!=0:
        keylength=int(input('please enter valid keylength'))
    for num in range(keylength):
        key.append(random.randint(2,int(len(file)*.12)))
        key.append(random.randint(0,1))
        key.append(random.randint(2,20))
        key.append(random.randint(0,1))

    writefile=open('spliced.tmp','w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 1')
    files=open('spliced.tmp').read().split('*/|/*')
    os.remove('spliced.tmp')
    file1=files[0]
    file2=files[1]
    file3=files[2]
    file4=files[3]
    key1=key[0:int(len(key)/4)]
    key2=key[int(len(key)/4):int(len(key)/2)]
    key3=key[int(len(key)/2):int(3*(len(key)/4))]
    key4=key[int(3*(len(key)/4)):len(key)]
    key1.reverse()
    key2.reverse()
    key3.reverse()
    key4.reverse()

    progressval=Value('i')
    queue1=Queue()
    queue2=Queue()
    queue3=Queue()
    queue4=Queue()
    p1=Process(target=encryption,args=(file1,key1,queue1,direction,progressval,keylength,1,C_executablename))
    p2=Process(target=encryption,args=(file2,key2,queue2,direction,progressval,keylength,2,C_executablename))
    p3=Process(target=encryption,args=(file3,key3,queue3,direction,progressval,keylength,3,C_executablename))
    p4=Process(target=encryption,args=(file4,key4,queue4,direction,progressval,keylength,4,C_executablename))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    mixed1=queue1.get()
    mixed2=queue2.get()
    mixed3=queue3.get()
    mixed4=queue4.get()
    file=mixed1+'`'+mixed2+'`'+mixed3+'`'+mixed4
    writefile=open('spliced.tmp','w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 0')
    final=open('spliced.tmp').read()
    os.remove('spliced.tmp')
    return final
# is the user interface portion of the code which takes the arguments,
# reads and writes the files, and encodes/decodes the files to/from 
# base64 strings before and after encryption

if __name__ == "__main__":
        freeze_support()
        if len(sys.argv)<3:
            print('Please specify file name, password and keylength(optional, default=30) respectively')
        else:



                #name of the executable for the C++ part of the program:

                C_Executable_Name='zcryptsplicer.exe'





                if len(sys.argv)>3:
                    keylength=int(sys.argv[3])
                else:
                    keylength=30
                path=sys.argv[1]
                password=sys.argv[2]
                if 'zrip' in path:
                        print('Decrypting: ',path)
                        with open(path,'rb') as file:
                            encoded=base64.b64encode(file.read())
                        string=str(encoded).replace("b'",'').replace("'",'').replace('=','')
                        string=decrypt(string,password,keylength,C_Executable_Name)
                        string+='==='
                        string=string.encode()
                        wpath=path.replace('.zrip','')
                        splitvar="\nBUFFER\nBUFFER\nBUFFER\nBUFFER".encode()
                        with open(wpath,'wb') as out:
                            final=base64.b64decode(string)
                            if splitvar in final:
                                final=final.split(splitvar)[0]
                            out.write(final)
                else:
                        print('Encrypting: ',path)
                        buffer=False
                        with open(path,'rb') as file:
                            filetext=file.read()
                            encoded=base64.b64encode(filetext)
                            if len(encoded)<400:
                                buffer=True
                                encoded=base64.b64encode(filetext+"\nBUFFER\nBUFFER\nBUFFER\nBUFFER".encode())
                        string=str(encoded).replace("b'",'').replace("'",'').replace('=','')
                        string=encrypt(string,password,keylength,C_Executable_Name,buffer)
                        string+='==='
                        string=string.encode()
                        with open(path+'.zrip','wb') as out:
                            out.write(base64.b64decode(string))
        print('Done')
