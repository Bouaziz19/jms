########Demonstration of NL4Py#################

netlogo_home="C:/Program Files/NetLogo 6.1.1"

import nl4py
import sys
import time
from model import *
from input_config import *
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


def design_data(n):
    ind=0
    for rec in list_ag :
        x=rec[0]
        y=rec[1]
        id_typ=rec[2]
        id=ind
        shape=list_shape[id_typ]
        size_shape=list_shape_size[id_typ]
        color=list_shape_color[id_typ]
        if id_typ in list_ws:
            typ="zn_p"
            name=typ+str(ind)
            nppar=list_nppar[ind]
            workstation(n,x,y,id,shape,size_shape,color,typ,name,0,nppar)
        else:
            typ="zn_np"
            name=typ+str(ind)
            np_zone(n,x,y,id,shape,size_shape,color,typ,name)
            
        ind+=1
    for rec in list_link:
        fr=rec[0]-1
        to=rec[1]-1
        street(n,fr,to)
    for i in range(len(list_workstation)-1):
        list_workstation[i].next_ws=list_workstation[i+1]
  
        
    for rec in list_workstation:
        w=worker(n,assignment=rec)
        z=rec.id
        w.move_to(z)
        # fd(n,w,4)
    
        
        pass
def set_product(n):
    i=0
    for ws in list_workstation:
        j=0
        z=ws.id
        while j < ws.nppar and j <list_nppar_i[i]:

            p=product(n)
            p_id=p.id
            p.move_to(z)
            
            ws.prd_encours.append(p)
            j+=1
        i+=1
    pass
def set_list_tache(n):
    for i in range(n_tache):
        ws=list_workstation[i]
        tach=tache(i,pt_tache[i],ws)
        list_tache.append(tach)
    list_tache[0].dj=0
    pass  
def configuration_initiale(n):
    design_data(n)
    set_list_tache(n)
    set_product(n)
    return n
 




