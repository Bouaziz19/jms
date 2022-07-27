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

print("\n1) Starting the NetLogoControllerServer with: nl4py.startServer()\n")

nl4py.initialize(netlogo_home)

nl4py.startServer(netlogo_home)
model = "./test.nlogo"
n=nl4py.NetLogoApp()
n.openModel(model)
print("")
