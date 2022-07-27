########Demonstration of NL4Py#################
#This example takes two commandline arguments n and model
#n : number of concurrent model runs required.
#model: path to model file
#example usage: python NRunsOfAModel.py 100 netlogo_home
###############################################
netlogo_home="C:/Program Files/NetLogo 6.2.2"
print("\n\n------------ This is a Demonstration of NL4PY --------------------\n")

import nl4py
import sys
import time

print("\n1) Starting the NetLogoControllerServer with: nl4py.startServer()\n")

nl4py.initialize(netlogo_home)

nl4py.startServer(netlogo_home)
model = "./test.nlogo"
n=nl4py.NetLogoApp()
n.openModel(model)
ames = []

in_v = ''
while in_v != 'q':
    n.command("setup")
    for i in range(10):
        print("**")
        n.command("go")
        print(n.get_param_names())
        print(n.getParamSpace())
        print(n.get_param_space())
        time.sleep(1)
    in_v = input("in_v , or enter 'q': ")
    if in_v == "n":
        n.command("go")
        
        # print(n.get)
        # print(n.get_param_names())
        # n.close_model()
        # n.get_param_names()
        # print("Before the sleep statement")
        # time.sleep(5)
        # print("After the sleep statement")
        # n.openModel(model)
n.close_model()

