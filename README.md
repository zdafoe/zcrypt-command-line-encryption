# zcrypt-command-line-encryption
If you're worried about downloading a virus just download the c++ source code and compile it yourself, otherwise i included a windows executable version.

This is a project i have been working on for command line encryption.

Zcrypt versions 1 and 2 are completely portable python scripts. Version 1 the least secure and very slow. 

Version 2 is much more secure and much faster than version 1 but still very slow.

Version 3 uses the exact same algorithm for encryption as version 2 but uses C++ for all of the time consuming parts which makes it much faster.

So far i've only gotten version 3 to work on windows when i tried compiling the C++ code for linux on my virtual machine it didn't work and i haven't had time to make it work yet.

But all of the c++ and python should be compatible with any system as i did not use any system specific code.

Also for version 2 there is a minimum file size of about 200 bytes

  Version 3 can encrypt/decrypt any file size
