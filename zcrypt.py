import base64
import sys
def rev2(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
        y=y+1
        if y%2==0:
            num=0
            l1.append(x)
            l1.append(sl)
        else:
            num=1
            sl=x
    if num==1:
           l1.append(sl)
    s=''.join(l1)
    return s
def rev3(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%3==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s2)
           l1.append(s1)
       else:
           if y%2==0:
               num=1
               s2=x
           else:
               num=2
               s1=x
    if num==1:
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev4(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%4==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else:
           if y%3==0:
               num=1
               s3=x
           else:
               if y%2==0:
                   num=2
                   s2=x
               else:
                   num=3
                   s1=x
    if num==1:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s2)
           l1.append(s1)
    elif num==3:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev5(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%5==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else:
           if y%4==0:
               num=1
               s4=x
           else:
               if y%3==0:
                   num=2
                   s3=x
               else:
                   if y%2==0:
                       num=3
                       s2=x
                   else:
                       num=4
                       s1=x
    if num==1:
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==3:
           l1.append(s2)
           l1.append(s1)
    elif num==4:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev6(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%6==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else: 
           if y%5==0:
               num=1
               s5=x
           else:
               if y%4==0:
                   num=2
                   s4=x
               else:
                   if y%3==0:
                       num=3
                       s3=x
                   else:
                       if y%2==0:
                           num=4
                           s2=x
                       else:
                           num=5
                           s1=x
    if num==1:
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==3:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==4:
           l1.append(s2)
           l1.append(s1)
    elif num==5:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev7(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%7==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else: 
           if y%6==0:
               num=1
               s6=x
           else: 
               if y%5==0:
                   num=2
                   s5=x
               else:
                   if y%4==0:
                       num=3
                       s4=x
                   else:
                       if y%3==0:
                           num=4
                           s3=x
                       else:
                           if y%2==0:
                               num=5
                               s2=x
                           else:
                               num=6
                               s1=x
    if num==1:
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==3:
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==4:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==5:
           l1.append(s2)
           l1.append(s1)
    elif num==6:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev8(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%8==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else: 
           if y%7==0:
               num=1
               s7=x
           else: 
               if y%6==0:
                   num=2
                   s6=x
               else: 
                   if y%5==0:
                       num=3
                       s5=x
                   else:
                       if y%4==0:
                           num=4
                           s4=x
                       else:
                           if y%3==0:
                               num=5
                               s3=x
                           else:
                               if y%2==0:
                                   num=6
                                   s2=x
                               else:
                                   num=7
                                   s1=x
    if num==1:
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==3:
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==4:
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==5:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==6:
           l1.append(s2)
           l1.append(s1)
    elif num==7:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev9(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%9==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else: 
           if y%8==0:
               num=1
               s8=x
           else: 
               if y%7==0:
                   num=2
                   s7=x
               else: 
                   if y%6==0:
                       num=3
                       s6=x
                   else: 
                       if y%5==0:
                           num=4
                           s5=x
                       else:
                           if y%4==0:
                               num=5
                               s4=x
                           else:
                               if y%3==0:
                                   num=6
                                   s3=x
                               else:
                                   if y%2==0:
                                       num=7
                                       s2=x
                                   else:
                                       num=8
                                       s1=x
    if num==1:
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==3:
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==4:
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==5:
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==6:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==7:
           l1.append(s2)
           l1.append(s1)
    elif num==8:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev10(s):
    y=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%10==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s9)
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else: 
           if y%9==0:
               num=1
               s9=x
           else: 
               if y%8==0:
                   num=2
                   s8=x
               else: 
                   if y%7==0:
                       num=3
                       s7=x
                   else: 
                       if y%6==0:
                           num=4
                           s6=x
                       else: 
                           if y%5==0:
                               num=5
                               s5=x
                           else:
                               if y%4==0:
                                   num=6
                                   s4=x
                               else:
                                   if y%3==0:
                                       num=7
                                       s3=x
                                   else:
                                       if y%2==0:
                                           num=8
                                           s2=x
                                       else:
                                           num=9
                                           s1=x
    if num==1:
           l1.append(s9)
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==2:
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==3:
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==4:
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==5:
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==6:
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==7:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
    elif num==8:
           l1.append(s2)
           l1.append(s1)
    elif num==9:
           l1.append(s1)
    s=''.join(l1)
    return s
def rev11(s):
    global y
    y=0
    y1=0
    l=list(s)
    l1=[]
    for x in l:
       y=y+1
       if y%11==0:
           y=0
           num=0
           l1.append(x)
           l1.append(s10)
           l1.append(s9)
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
       else:
           if y%10==0:
               num=1
               s10=x
           else: 
               if y%9==0:
                   num=2
                   s9=x
               else: 
                   if y%8==0:
                       num=3
                       s8=x
                   else: 
                       if y%7==0:
                           num=4
                           s7=x
                       else: 
                           if y%6==0:
                               num=5
                               s6=x
                           else: 
                               if y%5==0:
                                   num=6
                                   s5=x
                               else:
                                   if y%4==0:
                                       num=7
                                       s4=x
                                   else:
                                       if y%3==0:
                                           num=8
                                           s3=x
                                       else:
                                           if y%2==0:
                                               num=9
                                               s2=x
                                           else:
                                               num=10
                                               s1=x
    else:
        if num==1:
            l1.append(s10)
            l1.append(s9)
            l1.append(s8)
            l1.append(s7)
            l1.append(s6)
            l1.append(s5)
            l1.append(s4)
            l1.append(s3)
            l1.append(s2)
            l1.append(s1)
        elif num==2:
           l1.append(s9)
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
        elif num==3:
           l1.append(s8)
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
        elif num==4:
           l1.append(s7)
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
        elif num==5:
           l1.append(s6)
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
        elif num==6:
           l1.append(s5)
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
        elif num==7:
           l1.append(s4)
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
        elif num==8:
           l1.append(s3)
           l1.append(s2)
           l1.append(s1)
        elif num==9:
           l1.append(s2)
           l1.append(s1)
        elif num==10:
           l1.append(s1)
    s=''.join(l1)
    return s
def mov(s,n,m):
    l=list(s)
    l1=[]
    if n>int(.5*len(l)):
        n=int(.5*len(l))
    rem=len(l)%n
    if len(l)%n==0:
        for y in range(n):
            l11=[]
            for x in range(int(y*(len(l)/n)),int((y*(len(l)/n))+(len(l)/n))):
                l11.append(l[x])
            l1.append(l11)
        y=0
        b1=[]
        if m==2:
            for x in l1:
                y=y+1
                if y%2==0:
                    num=0
                    b1.append(x)
                    b1.append(sl)
                else:
                    num=1
                    sl=x
            if num==1:
                   b1.append(sl)
        elif m==5:
            for x in l1:
               y=y+1
               if y%5==0:
                   y=0
                   num=0
                   b1.append(x)
                   b1.append(s4)
                   b1.append(s3)
                   b1.append(s2)
                   b1.append(s1)
               else:
                   if y%4==0:
                       num=1
                       s4=x
                   else:
                       if y%3==0:
                           num=2
                           s3=x
                       else:
                           if y%2==0:
                               num=3
                               s2=x
                           else:
                               num=4
                               s1=x
            if num==1:
                   b1.append(s4)
                   b1.append(s3)
                   b1.append(s2)
                   b1.append(s1)
            elif num==2:
                   b1.append(s3)
                   b1.append(s2)
                   b1.append(s1)
            elif num==3:
                   b1.append(s2)
                   b1.append(s1)
            elif num==4:
                   b1.append(s1)
        for x in range(n):
            b1[x]=''.join(b1[x])
        b1=''.join(b1)
    else:
        for y in range(n):
            l11=[]
            for x in range(int(y*((len(l)-rem)/n)),int((y*((len(l)-rem)/n))+((len(l)-rem)/n))):
                l11.append(l[x])
            l1.append(l11)
        rems=[]
        for x in range(len(l)-rem,len(l)):
            rems.append(l[x])
        y=0
        b1=[]
        if m==2:
            for x in l1:
                y=y+1
                if y%2==0:
                    num=0
                    b1.append(x)
                    b1.append(sl)
                else:
                    num=1
                    sl=x
            if num==1:
                   b1.append(sl)
        elif m==5:
            for x in l1:
               y=y+1
               if y%5==0:
                   y=0
                   num=0
                   b1.append(x)
                   b1.append(s4)
                   b1.append(s3)
                   b1.append(s2)
                   b1.append(s1)
               else:
                   if y%4==0:
                       num=1
                       s4=x
                   else:
                       if y%3==0:
                           num=2
                           s3=x
                       else:
                           if y%2==0:
                               num=3
                               s2=x
                           else:
                               num=4
                               s1=x
            if num==1:
                   b1.append(s4)
                   b1.append(s3)
                   b1.append(s2)
                   b1.append(s1)
            elif num==2:
                   b1.append(s3)
                   b1.append(s2)
                   b1.append(s1)
            elif num==3:
                   b1.append(s2)
                   b1.append(s1)
            elif num==4:
                   b1.append(s1)
        for x in range(n):
            b1[x]=''.join(b1[x])
        b1=''.join(b1)+''.join(rems)
    return b1
def encrypt(file,pas):
    l=[]
    x =str(pas).replace(' ','_')
    xp=x
    s=file
##    s=list(s)
##    shift=len(list(xp))
##    for x1 in range(len(s)):
##        s[x1]=chr(ord(s[x1])+shift)
##    s=''.join(s)
    for n in x:
        l.append(str(ord(n)))
    l=''.join(l)
    l=list(l)
    print('Loading:|',end='',flush=True)
    for x in l:
        x=int(x)
        s=mov(s,len(l),2)
        s=mov(s,len(list(xp)),2)
        print('|',end='',flush=True)
        if x==0:
            s=rev2(s)
        if x==1:
            s=rev3(s)
        if x==2:
            s=rev4(s)
        if x==3:
            s=rev5(s)
        if x==4:
            s=rev6(s)
        if x==5:
            s=rev7(s)
        if x==6:
            s=rev8(s)
        if x==7:
            s=rev9(s)
        if x==8:
            s=rev10(s)
        if x==9:
            s=rev11(s)
        s=mov(s,len(l),5)
        print('|',end='',flush=True)
    return s
def decrypt(file,pas):
    l=[]
    x =str(pas).replace(' ','_')
    xp=x
    s=file
    for n in x:
        l.append(str(ord(n)))
    l=''.join(l)
    l=list(l)
    l.reverse()
    print('Loading:|',end='',flush=True)
    for x in l:
        x=int(x)
        s=mov(s,len(l),5)
        if x==0:
            s=rev2(s)
        if x==1:
            s=rev3(s)
        if x==2:
            s=rev4(s)
        if x==3:
            s=rev5(s)
        if x==4:
            s=rev6(s)
        if x==5:
            s=rev7(s)
        if x==6:
            s=rev8(s)
        if x==7:
            s=rev9(s)
        if x==8:
            s=rev10(s)
        if x==9:
            s=rev11(s)
        print('|',end='',flush=True)
        s=mov(s,len(list(xp)),2)
        s=mov(s,len(l),2)
        print('|',end='',flush=True)
##    shift=len(list(xp))
##    s=list(s)
##    for x1 in range(len(s)):
##        s[x1]=chr(ord(s[x1])-shift)
##    s=''.join(s)
    return s
if len(sys.argv)<3:
    print('Please specify file name and password respectively')
else:
    path=sys.argv[1]
    password=sys.argv[2]
    if 'zrip' in path:
        question=input('Would you like to decrypt '+path+"? yes or no 'y' / 'n': ")
        if question=='y':
            with open(path,'rb') as file:
                encoded=base64.b64encode(file.read())
            string=str(encoded).replace("b'",'').replace("'",'').replace('=','')
            string=decrypt(string,password)
            string+='==='
            string=string.encode()
            wpath=path.replace('.zrip','')
            with open(wpath,'wb') as out:
                out.write(base64.b64decode(string))
    else:
        question=input('Would you like to encrypt '+path+"? yes or no 'y' / 'n': ")
        if question=='y':
            with open(path,'rb') as file:
                encoded=base64.b64encode(file.read())
            string=str(encoded).replace("b'",'').replace("'",'').replace('=','')
            string=encrypt(string,password)
            string+='==='
            string=string.encode()
            with open(path+'.zrip','wb') as out:
                out.write(base64.b64decode(string))
print('Done')