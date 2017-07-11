#install script to esnure all necessary modules are present for viewer.py
#is designed to work for both python 2 and 3 

#Author: Constantinos Kavadias
#Email: ckavadias@student.unimelb.edu.au or kavacon@icloud.com
#July 2017
import subprocess
import site
import platform
try:
    from importlib import reload as reload
except ImportError:
    pass

#check python version being used and assign correct interpreter and pip
if int(platform.python_version()[0]) < 3:
    print("Using python 2")
    python_v = "python"
    pip_v = "pip"
else:
    python_v = "python3"
    pip_v = "pip3"


#check if pip is installed and act accordingly
try:
    import pip
except ImportError:
    print("pip does not appear to be installed, installing pip")
    print("you may be requested to enter your password to complete installation")
    if platform.system() == 'Windows':
        subprocess.call(["curl","-O","https://bootstrap.pypa.io/get-pip.py"])
        cmd = [python_v, "get-pip.py"]
    elif platform.system() == 'Darwin':
        subprocess.call(["curl","-O","https://bootstrap.pypa.io/get-pip.py"])
        cmd = ["sudo", python_v, "get-pip.py"]
    elif platform.system() == 'Linux':
        subprocess.call(["sudo","wget","https://bootstrap.pypa.io/get-pip.py"])
        cmd = ["sudo", python_v, "get-pip.py"]
    else:
        print("Your platform is not supported, our apologies")
        quit()
    subprocess.call(cmd)
    reload(site)

#check if requests is installed and act accordingly
try:
    import requests
except ImportError:
    print("requests does not appear to be installed, installing requests")
    print("you may be requested to enter your password to complete installation")
    import pip
    if platform.system() == "Windows":
        cmd = [pip_v, "install", "requests"]
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        cmd = ["sudo", pip_v, "install", "requests"]
    else:
        print("Your platform is not supported, our apologies")
        quit()
    subprocess.call(cmd)
    reload(site)

#confirm that the future module is installed for backwards compatibility
try:
    import six
except ImportError:
    print("six does not appear to be installed, installing six")
    print("you may be requested to enter your password to complete installation")
    if platform.system() == "Windows":
        cmd = [pip_v, "install", "six"]
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        cmd = ["sudo", pip_v, "install", "six"]
    else:
        print("Your platform is not supported, our apologies")
        quit()
    subprocess.call(cmd)
    reload(site)
