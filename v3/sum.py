import os
os.system("cls")
import nl4py,sys,time,copy
from allfunction import *
from model import *
from allfunction import *
from input_config import *
from input_data import *
import sum as sum

def run_netlogo():
    netlogo_home="C:/Program Files/NetLogo 6.1.1"
    nl4py.initialize(netlogo_home)
    nl4py.startServer(netlogo_home)
    model = "./v3/test.nlogo"
    n=nl4py.NetLogoApp()
    n.openModel(model)
    n.command("setup")
    n.command("setup")
    n.command("setup")
    return n
# try :
if 1:
    time_now=0
    in_v = ''
    tick = 0
    n=run_netlogo()
    configuration_initiale(n)

    while in_v != 'q':
        while tick<= max_t_sum:
            time.sleep(speed_sum)
            tick+=1
            time_now+=1
            # for rec in list_product:
            #     rec.update(n,n_tache,time_now)
            for rec in list_workstation:
                rec.update(n,n_tache,time_now)
            for rec in list_workstation:
                rec.update2(n,n_tache,time_now)
            
            # pass
            # list_workstation[1].update(n,n_tache,time_now)
            # for rec in list_worker:
            #     rec.update(n)
            
            print("***********  ",time_now,"  ********")
            pass
        n.close_model()
        in_v="q"
        # print("***********  ","fin","  ********")
        # in_v = input("in_v , or enter 'q': ")
# except Exception as error:
#    error_string = str(error)
#    print(error_string)
#    in_v = input("in_v , or enter 'q': ")