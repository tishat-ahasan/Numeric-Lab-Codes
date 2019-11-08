 1. Read Problem Description carefully to understand the problem.

 & Read Second Part of Design Document to understand the solution properly.

2. Unzip asst1.zip and go to directory $ asst1/src/kern/asst1 here you will see the following files: 

    1.invest_assignment.c  

    2.invest_assignment.h

    3.investor_producer.c

    4.investor_producer.h

you have to complete the function in **investor_producer.c** according to the demand of **invest_assignment.c.**


3. Solution is on the Solution Folder.Just replace the **"investor_producer.c"** and **"investor_producer.h"** files in **asst1/src/kern/asst1** with the files situated in Solution Folder (With same name). 

4. To compile you need to run the Compile.sh file.to do so run the following 2 commands in terminal

    $ chmod -R 777 Compile.sh  //to change the permission.Need to run only once. 

    $ ./Compile

5. Then Run the os-161 by: 

    $ chmod -R 777 Run.sh   //to change the permission.Need to run only once.

    $ ./Run 

you should see the following:

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

sys161: System/161 release 2.0.8, compiled Jul 18 2019 20:15:45


OS/161 base system version 2.0.3

Copyright (c) 2000, 2001-2005, 2008-2011, 2013, 2014

   President and Fellows of Harvard College.  All rights reserved.


Put-your-group-name-here's system version 0 (ASST1 #125)


1888k physical memory available

Device probe...

lamebus0 (system main bus)

emu0 at lamebus0

ltrace0 at lamebus0

ltimer0 at lamebus0

beep0 at ltimer0

rtclock0 at ltimer0

lrandom0 at lamebus0

random0 at lrandom0

lhd0 at lamebus0

lhd1 at lamebus0

lser0 at lamebus0

con0 at lser0



cpu0: MIPS/161 (System/161 2.x) features 0x0

OS/161 kernel [? for menu]:

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


Now put '1b' to run the Investor Producer Problem.you should see a window like this:

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Producer 0 going home after serving 130 orders
Producer 4 going home after serving 78 orders
Producer 2 going home after serving 77 orders
Producer 3 going home after serving 84 orders
Producer 1 going home after serving 81 orders
=====================================================================================
Bank Income ... 
[0]: 137885 [1]: 143240 [2]: 131340 
Producer Income ... 
[0]: 238500 [1]: 148310 [2]: 142360 [3]: 154220 [4]: 141540 
Customer Spending ... 
[0]: 956110 [1]: 954040 [2]: 952660 [3]: 944035 [4]: 936445 [5]: 935755 [6]: 960020 [7]: 931730 [8]: 964160 [9]: 951740 
=====================================================================================
Verification ....
The InvestorProducer is closed, bye!!!
Operation took 1.881944000 seconds
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Teacher's Feedback: 
#################################################
Teacher said everthing is ok except 2 thinks. 

1.There was a condition that a producer can take at most 1/3 of a order.to do so
we split every order in equal 3 size in order_item() funtion.He said not to split it.Instead
take 1/3 orders of the of total currently placed order,if you understand the solution properly 
hopefully you can implement it. 
2.He asked to use semaphore for every bank explicitely.