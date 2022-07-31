########Demonstration of NL4Py#################

netlogo_home="C:/Program Files/NetLogo 6.1.1"

import nl4py
import sys
import time
from input_data import *
# all function


def list2nllist(lis):
    s="["
    for i in lis:
        if type(i) == str:
            s+=' "'+i+'" '
        else :
            s+=' '+str(i)+' '
    s+="]"
    return s

 




