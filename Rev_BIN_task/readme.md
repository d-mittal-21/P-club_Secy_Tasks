# REV-BIN!
Hi I am Divyansh Mittal, and this the Task-2 provided by p-club

**Problem Statemen**
>A password is hidden in some form in the binary file \<rev>\. Your task is to reverse engineer the binary to get the password.
---
So, I started with the command strings over file rev, to see if the password is hidden as plain text, but as expected it was not there.

![image_1](/ss/image_1.png)

got these strings

Then the only option left was to disassemble the binary file to get the assembly code.
For this I used an online disassembler, **disassembler.io** (I didn't have IDA)

Seeing the assembly code I understood that first the file is taking a input from us, storing it in Var_33 which is of size 31 bits, then it is passing it to a function **checkPassword()** and comparing the return value with 1.

![image_2](/ss/image_2.png)

Upon seeing checkPassword function I realised that there is much more manuplation done on input than expected, many left-shift and right-shifts in while loops. 

I tried applying break-points on ro-data, but there were too many functions. all in vain.

![image_3](/ss/image_3.png)

Now only one tool was left **ANGR**
I found base_address, target_address, and a avoid_address. Using these, I made a python program with angr library, defined a list of certain flag characters, brute force it and run on a venv.

**The Source Code is available in file win.py.**

I possibly did a mistake in installing angr, the code was not recognising claripy lib :(   
