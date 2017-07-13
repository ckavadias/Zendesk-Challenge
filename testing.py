#Testing script for viewer.py

import subprocess as sub
import platform
from six import print_

#constant definitions
VERSION = platform.python_version()[0]
PATH1 = ["options","tickets", "next", "previous", "previous", "select", "42",
         "options", "leave"]
ADD = ('', "'")
PYTHON = ["python3", "python"]
PATH2 = ["options", "select", "205", "leave"]
PATH3 = ["leave"]
PATH4 = ["options", "tickets", "leave"]
TESTS = [PATH1, PATH2, PATH3, PATH4]
OUT = open("test_out.txt", "w")

#determine which python version we are using for input syntax and calling
#interpreter
if VERSION == '2':
    index = 1
else:
    index = 0

i = 0
for test in TESTS:
    i+=1
    print_("TESTING PATH"+str(i))
    OUT.write("--"*25)
    OUT.write("PATH"+str(i))
    OUT.write("--"*25 + '\n')
    print_("PATH: ", test)

    path = ''
    for option in test:
        path+= (ADD[index]+option+ADD[index]+'\n')
    try:
        viewer = sub.Popen([PYTHON[index], "viewer.py"], stdout = sub.PIPE,
                        stdin = sub.PIPE, stderr = sub.STDOUT)
        out, err = viewer.communicate(input=path.encode())
    except Exception as ex:
           print_("ERROR occurred, there're problems with the testing")
           raise ex
    if err != None:
           print_("ERRORS returned by test:")
           OUT.write("This test failed: \n")
           OUT.write(err.decode())
           print_(err.decode())
    else:
           print_("HAPPY PATH :D, NO ERRORS\n")
           OUT.write(out.decode())
    OUT.write(" "*15 + "--"*25 + '\n')
OUT.close()
print_("Output from the test will be available in the file test_out.txt")
    


