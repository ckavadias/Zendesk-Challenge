{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf810
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\csgray\c0;\csgray\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Notes:\
The author highly recommends the use of python 3 when using viewer.py for a more natural user experience but has included failsafes and workarounds to ensure a successful experience in python 2.\
\
Throughout the below python 2 will be referencing python 2.7 or higher and python 3 will be referencing python 3.4 or higher.\
\
Installation:\
Welcome to viewer, this program is designed to retrieve and display tickets stored in the Zendesk API and is written with the intention to be run on python 3. However due to how common python 2 is and the issues presented with running multiple versions of python on the same device, precautions and steps have been taken to ensure a high level of compatibility with both version 2 and 3 with minimal change to the user interface. This program is also designed to be used on both Windows and Unix environments.\
\
There is one small caveat that needs to be addressed in the interface depending on the python version you are running, this will be addressed in the usage section below.\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\li530\fi22\pardirnatural\partightenfactor0
\cf0 The tricky part:\
Ensuring your system is properly setup to run the viewer is simple and requires only that you have either python 2 or 3 already installed. For users running Linux or darwin your system likely comes with python 2.7 as standard as well as many libraries. For other users please visit {\field{\*\fldinst{HYPERLINK "https://www.python.org/downloads/"}}{\fldrslt https://www.python.org/downloads/}} and download the appropriate python package for your system. It is recommended if you are installing python for the first time that you install 3.4 or higher as this will ensure the most seamless user experience with the viewer program. However python 2.7 or higher is also compatible and can be chosen if desired.\
If you\'92re unsure if you have python simply open a terminal or command prompt window and type python (to check for python 2) or python3 (to check for python 3) then enter. If installed the python interpreter will start and the version number will be printed. Otherwise an error will present saying this command is not found, please refer above to install.\
\
The easy part:\
There are three modules that are key to successfully running viewer.py pip, six and requests. To avoid a lengthy explanation of checking for and installing these modules yourself I have included with viewer.py the file install.py which will check for and install all necessary packages. This module may require administrator password while running.\
Before starting viewer simply navigate to the folder containing viewer.py and install.py in your terminal/command prompt window and execute python install.py or python3 install.py (depending on the version of python you\'92re running). It will take care of the messy stuff. (Note install.py has been designed and tested to function with both the python 2 interpreter (python) and python 3 interpreter (python3).)\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
Now you\'92re ready to go, you can now execute python/python3 viewer.py and start using the program, enjoy!\
\
\pard\tx557\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 Usage:\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 The viewer will work in one of two interfaces, direct invocation from the terminal/command prompt in the manner python viewer.py or python3 viewer.py or in the python standalone interpreter IDLE, both will be discussed below.\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\li515\fi29\pardirnatural\partightenfactor0
\cf0 IDLE:\
To use the viewer in IDLE, open the program if installed which will present you with a custom active python shell and it should be showing >>> on the left hand side. This is an interactive shell and command style language will not work here. Navigate to the file menu in IDLE and select open, navigate to viewer.py and open, this will open the source code for viewer in a module window. Click into the module window, make sure not to edit the code and select run, then run module. This should activate the module on the shell and you may begin using the interface as per the below instructions\
\
Terminal/Command prompt:\
Once installation has occurred successfully from your terminal window stay in the folder containing viewer.py. In order to activate the interface simply type python viewer.py or python3 viewer.py followed by enter (depending on the version of python you are running) The interface will now activate, you can begin using it as per the below instructions.\
\
Basic Usage:\
The interface operates using one word commands for the assistant \'91Alfred\'92 and is designed to be as simplistic and intuitive as possible. Upon start up you will be presented with the following message\
\

\f1\fs22 \cf2 \cb3 \CocoaLigature0 	Welcome, my name's Alfred\
	I will be assisting with your tickets\
\
  	  To view command options type 'options' then press enter\
   	  Alternatively to quit type \'91leave\'92 then press enter.\
\
\
	I pick:\
\

\f0\fs24 \cf0 \cb1 \CocoaLigature1 To select an option simply type it in and hit enter as instructed. Selecting quit will exit the interface with the message 
\f1\fs22 \cf2 \cb3 \CocoaLigature0 It appears my services are no longer required, good bye. 
\f0\fs24 \cf0 \cb1 \CocoaLigature1 Selecting options will present the main options menu as below:\
\

\f1\fs22 \cf2 \cb3 \CocoaLigature0 	Type one of the following then press enter:\
		\'91tickets\'92 | View all available tickets.\
		'select'  | View a specific ticket (have the ticket number ready).\
		\'91leave\'92   | Quit the viewer.\
		'options' | Make me repeat myself.\
\
	I pick:\
\

\f0\fs24 \cf0 \cb1 \CocoaLigature1 Select the options in the same manner as before and you will be presented with another series of options specific to your request, always with the option to quit or return to this menu available.\
Selecting tickets will present the first 25 available tickets with the option to page through any other available tickets and select any specific ticket. Selecting select will prompt for a ticket number and allow a more detailed display of the selected ticket\'92s details\
\
Python 2 interface notes:\
The interface when used in python 2 is practically identical in presentation to when it is used in python 3 with only one small change to how the user inputs their chosen options. Due to changes implemented in python 3 the use of he function input() in python 2 does not behave as it does in python 3. When presented with the 
\f1\fs22 \cf2 \cb3 \CocoaLigature0 I pick:
\f0\fs24 \cf0 \cb1 \CocoaLigature1  interface in a python 2 instance of viewer.py the user must type their option as a string literal for the input to be recognised. When selecting an option in python 2 please ensure it is enclosed in \'93 \'93 or \'91 \'91 . A warning will present whenever the interface is started in python 2 reiterating this.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0
\cf0 \
You now have all the tools you need to start using the viewer interface, enjoy!\
}