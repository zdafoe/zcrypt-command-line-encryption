#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <iterator>
#include <algorithm>
#include <stdio.h>
template<typename Out>
void split(const std::string &s, char delim, Out result) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        *(result++) = item;
    }
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, std::back_inserter(elems));
    return elems;
}
using namespace std;
string splicer(string text);
string joiner(string text);
string mov(string text, int key, int movvar);
string crypto(string text1, vector<int> key, int direction, int keylength,string processnum);

int main(int argc,char *argv[]){
        string text;
        string mode;
        string txt;
        mode=argv[1];
        
        if (mode=="1"){
            ifstream readfile;
            readfile.open("spliced.tmp",ios::in);
            while (readfile.good())
                {
                getline(readfile, txt);
                text.append(txt);
                }
            readfile.close();
            remove("spliced.tmp");
            string x =splicer(text);
            ofstream file;
            file.open("spliced.tmp",ios::out);
            if (file.is_open()){
                file <<x;
            }
        }else if (mode=="0"){
            ifstream readfile;
            readfile.open("spliced.tmp",ios::in);
            while (readfile.good())
                {
                getline(readfile, txt);
                text.append(txt);
                }
            readfile.close();
            remove("spliced.tmp");
            string x =joiner(text);
            ofstream file;
            file.open("spliced.tmp",ios::out);
            if (file.is_open()){
                file <<x;
            }
            file.close();
        }else if (mode=="2"){
            //make key vector<int> from vector of strings: then convert the first vector if strings into ints in the second vector
            vector<string> stringkey=split(argv[2],'`');
            vector<string>::iterator iter;
            vector<int> key;
            stringstream stream;
            int keypiece;
            for(iter=stringkey.begin(); iter!=stringkey.end(); iter++){
                stream.clear();
                stream<<*iter;
                stream>>keypiece;
                key.push_back(keypiece);
            }
            stringstream stream1(argv[3]);
            int direction;
            stream1>>direction;

            stringstream stream2(argv[4]);
            int keylength;
            stream2>>keylength;
            string processnum=argv[5];
            ifstream readfile;
            readfile.open("spliced.tmp"+processnum,ios::in);
            while (readfile.good()){
                getline(readfile, txt);
                text.append(txt);
                }
            readfile.close();
            string fn="spliced.tmp"+processnum;
            remove(fn.c_str());
            //string crypto(string text, vector<int> key, int direction, int keylength);
            string Final;
            Final=crypto(text,key,direction,keylength,processnum);
            ofstream file;
            file.open("spliced.tmp"+processnum,ios::out);
            if (file.is_open()){
                file <<Final;
            }
            
        }
        return 0;
    
    }
string splicer(string text){
    string str = text;
    string str1,str2,str3,str4;
    string add;
    int c1=0;
    int c2=3;
    int c3=2;
    int c4=1;
    for(std::string::size_type i = 0; i < str.size(); ++i) {
        add.clear();
        add=str[i];
        if (c1%4==0){
            str1.append(add);
        }else if (c2%4==0){
            str2.append(add);
        }else if (c3%4==0){
            str3.append(add);
        }else if (c4%4==0){
            str4.append(add);
        }
        c1=c1+1;
        c2=c2+1;
        c3=c3+1;
        c4=c4+1;
    }
    text.clear();
    text=str1+"*/|/*"+str2+"*/|/*"+str3+"*/|/*"+str4;
    return text;
}
string joiner(string text){
    string str1;
    string add;
    std::vector<std::string> str = split(text,'`');
    string mixed1=str[0];
    string mixed2=str[1];
    string mixed3=str[2];
    string mixed4=str[3];
    string total=mixed1+mixed2+mixed3+mixed4;
    int c1=0;
    int c2=3;
    int c3=2;
    int c4=1;
    vector<int> fnumlist={0,0,0,0};
    for(std::string::size_type i = 0; i < total.size(); ++i) {
        add.clear();
        if (c1%4==0){
            add=mixed1[fnumlist[0]];
            fnumlist[0]=fnumlist[0]+1;
        }else if (c2%4==0){
            add=mixed2[fnumlist[1]];
            fnumlist[1]=fnumlist[1]+1;
        }else if (c3%4==0){
            add=mixed3[fnumlist[2]];
            fnumlist[2]=fnumlist[2]+1;
        }else if (c4%4==0){
            add=mixed4[fnumlist[3]];
            fnumlist[3]=fnumlist[3]+1;
        }
        str1.append(add);
        c1=c1+1;
        c2=c2+1;
        c3=c3+1;
        c4=c4+1;
    }
    return str1;
}
string mov(string text, int key, int movvar){
    int textlength=text.size();
    int rem=textlength%key;
    string remaining;
    list<string> mainlist;
    list<string> mainlist2;
    string Final;
    list<string>::iterator iter;
    string substring;
    string add;
    Final=text;
    if (rem==0){
       //if there is no remaining text do this
       //create list of strings and reverse those strings
        for(int y=0; y<key; y=y+1){
            substring.clear();
            for(int x=y*(textlength/key); x<(y*(textlength/key))+textlength/key;x=x+1){
                add.clear();
                add=text[x];
                substring.append(add);
            }
            //reverse(substring.begin(),substring.end());
            mainlist.push_back(substring);
        }
        //shuffle the list of strings
        int counter =0;
        int leftovers;
        string substring1;
        if (movvar==2){ 
            for(iter = mainlist.begin(); iter != mainlist.end(); iter++){
                counter=counter+1;
                if (counter%2==0){
                    leftovers=0;
                    mainlist2.push_back(*iter);
                    mainlist2.push_back(substring1);
                }else{
                    leftovers=1;
                    substring1.clear();
                    substring1=*iter;
                }
            }
            if(leftovers==1){
                mainlist2.push_back(substring1);
            }
        }
        if (movvar==5){
            string substring2;
            string substring3;
            string substring4;
            //reverse groups of five throughout the list of strings
            for(iter = mainlist.begin(); iter != mainlist.end(); iter++){
                counter=counter+1;
                if (counter%5==0){
                    counter=0;
                    leftovers=0;
                    mainlist2.push_back(*iter);
                    mainlist2.push_back(substring4);
                    mainlist2.push_back(substring3);
                    mainlist2.push_back(substring2);
                    mainlist2.push_back(substring1);
                }else if(counter%4==0){
                    substring4.clear();
                    substring4=*iter;
                    leftovers=4;
                }else if(counter%3==0){
                    substring3.clear();
                    substring3=*iter;
                    leftovers=3;
                }else if(counter%2==0){
                    substring2.clear();
                    substring2=*iter;
                    leftovers=2;
                }else{
                    substring1.clear();
                    substring1=*iter;
                    leftovers=1;
                }
            }
            if (leftovers>0){
                mainlist2.push_back(substring1);
                if(leftovers>1){
                    mainlist2.push_back(substring2);
                    if(leftovers>2){
                        mainlist2.push_back(substring3);
                        if(leftovers>3){
                            mainlist2.push_back(substring4);
                        }
                    }
                }
            }
        }
        //put the final list of strings into the final string variable to return
        Final.clear();
        for(iter = mainlist2.begin(); iter != mainlist2.end(); iter++){
            Final.append(*iter);
        }
    }else{
        //this is the mov function code for if the number of charecters in the base64 string
        //doesn't fit perfectly into the number of groups

       //create list of strings and reverse those strings
        for(int y=0; y<key; y=y+1){
            substring.clear();
            for(int x=y*((textlength-rem)/key); x<(y*((textlength-rem)/key))+(textlength-rem)/key;x=x+1){
                add.clear();
                add=text[x];
                substring.append(add);
            }
            //reverse(substring.begin(),substring.end());
            mainlist.push_back(substring);
        }
        //shuffle the list of strings
        int counter =0;
        int leftovers;
        string substring1;
        if (movvar==2){ 
            for(iter = mainlist.begin(); iter != mainlist.end(); iter++){
                counter=counter+1;
                if (counter%2==0){
                    leftovers=0;
                    mainlist2.push_back(*iter);
                    mainlist2.push_back(substring1);
                }else{
                    leftovers=1;
                    substring1.clear();
                    substring1=*iter;
                }
            }
            if(leftovers==1){
                mainlist2.push_back(substring1);
            }
        }
        if (movvar==5){
            string substring2;
            string substring3;
            string substring4;
            //reverse groups of five throughout the list of strings
            for(iter = mainlist.begin(); iter != mainlist.end(); iter++){
                counter=counter+1;
                if (counter%5==0){
                    counter=0;
                    leftovers=0;
                    mainlist2.push_back(*iter);
                    mainlist2.push_back(substring4);
                    mainlist2.push_back(substring3);
                    mainlist2.push_back(substring2);
                    mainlist2.push_back(substring1);
                }else if(counter%4==0){
                    substring4.clear();
                    substring4=*iter;
                    leftovers=4;
                }else if(counter%3==0){
                    substring3.clear();
                    substring3=*iter;
                    leftovers=3;
                }else if(counter%2==0){
                    substring2.clear();
                    substring2=*iter;
                    leftovers=2;
                }else{
                    substring1.clear();
                    substring1=*iter;
                    leftovers=1;
                }
            }
            if (leftovers>0){
                mainlist2.push_back(substring1);
                if(leftovers>1){
                    mainlist2.push_back(substring2);
                    if(leftovers>2){
                        mainlist2.push_back(substring3);
                        if(leftovers>3){
                            mainlist2.push_back(substring4);
                        }
                    }
                }
            }
        }
        
        for(int x=textlength-rem;x<textlength;x=x+1){
            add.clear();
            add=text[x];
            remaining.append(add);
        }
        //put the final list of strings into the final string variable to return
        Final.clear();
        for(iter = mainlist2.begin(); iter != mainlist2.end(); iter++){
            Final.append(*iter);            
        }
        Final.append(remaining);
    }
    return Final;
}



string crypto(string text1,vector<int> key, int direction, int keylength,string processnum){
    string Final;
    int y;
    float ratio;
    string loadsymbol="|";
    int movvar;
    float addvar=key.size()/15;
    float loadnum=0;
    if(direction==1){
        
        for(int x=0; x<key.size();x=x+2){
            y=x+1;
            if (key[x]==0){
                movvar=2;
            }else{
                movvar=5;
            }
            text1=mov(text1,key[y],movvar);
            if(x>=loadnum){
                cout<<loadsymbol;
                loadnum=loadnum+addvar;
            }
            
        }
    }else{
        for(int x=0; x<key.size();x=x+2){
            y=x+1;
            if (key[y]==0){
                movvar=2;
            }else{
                movvar=5;
            }

            text1=mov(text1,key[x],movvar);


            if(x>=loadnum){
                cout<<loadsymbol;
                loadnum=loadnum+addvar;
            }
        }
    }
    
    return text1;
}