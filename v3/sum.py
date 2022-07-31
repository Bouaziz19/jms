import os
os.system("cls")
import nl4py,sys,time,copy
from allfunction import *
from model import *
from allfunction import *
from input_config import *
from input_data import *
# def up_
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
    time_now=1
    in_v = ''
    tick = 1
    n=run_netlogo()
    configuration_initiale(n)

    while in_v != 'q':
        while tick<= max_t_sum:
            time.sleep(speed_sum)
            print("***********  ",time_now,"  ********")

            
            tick+=1
            time_now+=1
            for rec in list_worker:
                rec.update(n)
            for rec in list_workstation:
                rec.update(n,n_tache,time_now)
            pass

 
            
            pass
        n.close_model()
        in_v="q"
        # print("***********  ","fin","  ********")
        # in_v = input("in_v , or enter 'q': ")
# except Exception as error:
#    error_string = str(error)
#    print(error_string)
#    in_v = input("in_v , or enter 'q': ")
# def main():
#     print('Total = ', total)
#     func1()
#     print('Total = ', total)
#     func()
#     print('Total = ', total)
#     func2()
#     print('Total = ', total)
#     func3()
#     print('Total = ', total)
# if __name__ == '__main__':
#     main()