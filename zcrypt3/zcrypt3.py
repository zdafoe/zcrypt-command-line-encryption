""" 
This is the third version of zcrypt an encryption program made with python and C++ by me: Zech Dafoe
when using the program the syntax is: filename, password, and an optional third argument for keylength that defaults to 30 and must be an even number
an example of its usage and add an "s" as the last argument to only use 4 processes on a large file:
                   filename    password   keylength(optional)  (use this last argumetn to only use 4 processes)(optional and always the last argument)
python zcrypt3.py   me.png     iforgot    30                     s
"""



import base64, random, sys, time,os
from multiprocessing import Process,Queue,Value,freeze_support,cpu_count


def encryption(string,key,queue,direction,progressval,keylength,processnum,C_executablename,setnum):
    '''this function calls the C++ executable to do the acutal encrypting'''
    #make file to transfer data to C++ executable
    writefile=open('spliced.tmp'+str(processnum)+str(setnum),'w')
    writefile.write(string)
    writefile.close()
    #call executable
    x=0
    for y in key:
        key[x]=str(y)
        x+=1
    key='`'.join(key)
    var=os.system(f'{C_executablename} 2 {key} {direction} {keylength} {processnum} {setnum}')
    #get processed string from transfer file
    string=open('spliced.tmp'+str(processnum)+str(setnum)).read()
    os.remove('spliced.tmp'+str(processnum)+str(setnum))

    queue.put(string)
#function called for encryping a file args are the base64 encoded file and the password
def encrypt(file,pas,keylength,C_executablename,buffer,setnum,loadbar):
    '''function creates key from password and starts processes for encrypting a base 64 string'''
    if buffer:
        file=file+'Z'*200
    direction=0
    if setnum==1:
        print('_'*60*loadbar)
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

    writefile=open('spliced.tmp'+str(setnum),'w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 1 {setnum}')
    files=open('spliced.tmp'+str(setnum)).read().split('*/|/*')
    os.remove('spliced.tmp'+str(setnum))
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
    p1=Process(target=encryption,args=(file1,key1,queue1,direction,progressval,keylength,1,C_executablename,setnum))
    p2=Process(target=encryption,args=(file2,key2,queue2,direction,progressval,keylength,2,C_executablename,setnum))
    p3=Process(target=encryption,args=(file3,key3,queue3,direction,progressval,keylength,3,C_executablename,setnum))
    p4=Process(target=encryption,args=(file4,key4,queue4,direction,progressval,keylength,4,C_executablename,setnum))
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    mixed1=queue1.get()
    mixed2=queue2.get()
    mixed3=queue3.get()
    mixed4=queue4.get()
    file=mixed1+'`'+mixed2+'`'+mixed3+'`'+mixed4
    writefile=open('spliced.tmp'+str(setnum),'w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 0 {setnum}')
    final=open('spliced.tmp'+str(setnum)).read()
    os.remove('spliced.tmp'+str(setnum))

    return final
#same as above function but for decrypting
def decrypt(file,pas,keylength,C_executablename,setnum,loadbar):
    '''function creates key from password and starts processes for decrypting a base 64 string'''
    direction=1
    if setnum==1:
        print('_'*60*loadbar)
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

    writefile=open('spliced.tmp'+str(setnum),'w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 1 {setnum}')
    files=open('spliced.tmp'+str(setnum)).read().split('*/|/*')
    os.remove('spliced.tmp'+str(setnum))
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
    p1=Process(target=encryption,args=(file1,key1,queue1,direction,progressval,keylength,1,C_executablename,setnum))
    p2=Process(target=encryption,args=(file2,key2,queue2,direction,progressval,keylength,2,C_executablename,setnum))
    p3=Process(target=encryption,args=(file3,key3,queue3,direction,progressval,keylength,3,C_executablename,setnum))
    p4=Process(target=encryption,args=(file4,key4,queue4,direction,progressval,keylength,4,C_executablename,setnum))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    mixed1=queue1.get()
    mixed2=queue2.get()
    mixed3=queue3.get()
    mixed4=queue4.get()
    file=mixed1+'`'+mixed2+'`'+mixed3+'`'+mixed4
    writefile=open('spliced.tmp'+str(setnum),'w')
    writefile.write(file)
    writefile.close()
    splicevar=os.system(f'{C_executablename} 0 {setnum}')
    final=open('spliced.tmp'+str(setnum)).read()
    os.remove('spliced.tmp'+str(setnum))
    return final
def starter(string,password,keylength,C_Executable_Name,buffer,crypt,qx,setnum,loadbar):
    if crypt:
        string=encrypt(string,password,keylength,C_Executable_Name,buffer,setnum,loadbar)
    else:
        string=decrypt(string,password,keylength,C_Executable_Name,setnum,loadbar)
    qx.put(string)
# is the user interface portion of the code which takes the arguments,
# reads and writes the files, and encodes/decodes the files to/from 
# base64 strings before and after encryption

if __name__ == "__main__":
        freeze_support()
        if len(sys.argv)<3:
            print('Please specify file name, password, keylength(optional, default=30) and "s"(only use 4 processes on a large file)(optional) respectively')
        else:



                #name of the executable for the C++ part of the program:

                C_Executable_Name='zcryptsplicer.exe'



                #check if user specified a key length
                if len(sys.argv)>3:
                    try:
                        keylength=int(sys.argv[3])
                    except:
                        keylength=30
                else:
                    keylength=30

                path=sys.argv[1]
                password=sys.argv[2]
                if os.path.isfile(path):
                    #            the division converts bytes to megabytes
                    if os.path.getsize(path)/1048576<125:
                        # make it split file up and use open(path,'a+b') to append the file back together
                        setnum=1
                        if 'zrip' in path:
                                print('Decrypting: ',path)
                                with open(path,'rb') as file:
                                    encoded=base64.b64encode(file.read())
                                string=str(encoded).replace("b'",'').replace("'",'').replace('=','')
                                string=decrypt(string,password,keylength,C_Executable_Name,setnum,1)
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
                                string=encrypt(string,password,keylength,C_Executable_Name,buffer,setnum,1)
                                string+='==='
                                string=string.encode()
                                with open(path+'.zrip','wb') as out:
                                    out.write(base64.b64decode(string))
                    else:
                        filesize=os.path.getsize(path)
                        splitnum=2

                        while filesize/splitnum>131072000:
                            splitnum+=1
                        sectionsize=filesize/splitnum
                        sectionsize=int(str(sectionsize).split('.')[0])


                        if 'zrip'in path:
                            writepath=path.replace('.zrip','')
                            print('Decrypting: ',path)
                            crypt=False
                        else:
                            crypt=True
                            print('Encrypting: ',path)
                            writepath=path+'.zrip'
                        oneset=False
                        if cpu_count()<8:
                            oneset=True
                        else:
                            if len(sys.argv)>3:
                                if len(sys.argv)>4:
                                    if sys.argv[4]=='s':
                                        oneset=True
                                if sys.argv[3]=='s':
                                    oneset=True
                        if oneset:
                            loadbar=1
                        else:
                            loadbar=2
                        first1,first2=True,True
                        buffer=False
                        w=open(writepath,'wb')
                        w.write(b'')
                        w.close()
                        writefile=open(writepath,'a+b')
                        readfile=open(path,'rb')
                        q1=Queue()
                        q2=Queue()
                        for num in range(splitnum):
                            byteindex=(num*sectionsize)
                            if num==splitnum-1:
                                sectionsize+=1000
                            readfile.seek(byteindex)
                            string=readfile.read(sectionsize)
                            encoded=base64.b64encode(string)
                            string=str(encoded).replace("b'",'').replace("'",'').replace('=','')
                            if num%2==0 or oneset:
                                if not first1:
                                    ElFin=q1.get()
                                    ElFin+='==='
                                    ElFin=ElFin.encode()
                                    writefile.write(base64.b64decode(ElFin))
                                    print(f'({num+1}/{splitnum})')
                                P1=Process(target=starter,args=(string,password,keylength,C_Executable_Name,buffer,crypt,q1,1,loadbar))
                                P1.start()
                                first1=False
                            else:
                                if not first2:
                                    ElFin=q2.get()
                                    ElFin+='==='
                                    ElFin=ElFin.encode()
                                    writefile.write(base64.b64decode(ElFin))
                                    print(f'({num+1}/{splitnum})')
                                P2=Process(target=starter,args=(string,password,keylength,C_Executable_Name,buffer,crypt,q2,2,loadbar))
                                P2.start()
                                first2=False
                        string=q1.get()
                        string+='===='
                        string=string.encode()
                        writefile.write(base64.b64decode(string))
                        print(f'({num+1}/{splitnum})')
                        if splitnum%2==0 and not oneset:
                            string=q2.get()
                            string+='===='
                            string=string.encode()
                            writefile.write(base64.b64decode(string))
                        #print("The file: ",path, " is too big: ",round((filesize/1024)/1024,3)," MB")
                else:
                    if os.path.exists(path):
                        print(path," is a folder. Please enter a valid file name.")
                    else:
                        print("Cannot find: ",path," Please provide a valid file name.")
        print('Done')
