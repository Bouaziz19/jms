import copy
import random
import time

import numpy as np
import allfunction as allf
from input_config import *
from input_data import *

global list_worker
global list_product
global list_zone
global list_workstation
global list_tache
global n_robot
list_worker=[]
list_product=[]
list_zone=[]
list_workstation=[]
list_street=[]
list_tache=[]
n_robot=0
def list2nllist(lis):
        s="["
        for i in lis:
            if type(i) == str:
                s+=' "'+i+'" '
            else :
                s+=' '+str(i)+' '
        s+="]"
        return s

def de_copy(a):
    return copy.deepcopy(a)

def set_workstations(n):
    ind=0
    for rec in data.list_ag :
        x=rec[0]
        y=rec[1]
        id_typ=rec[2]
        id=ind
        shape=data.list_shape[id_typ]
        size_shape=data.list_shape_size[id_typ]
        color=data.list_shape_color[id_typ]
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
    for rec in data.list_link:
        fr=rec[0]-1
        to=rec[1]-1
        street(n,fr,to)
    for i in range(len(list_workstation)-1):
        list_workstation[i].next_ws=list_workstation[i+1]
  
        

def set_workers(n):    
    i=0
    for rec in list_workstation:
        # wrk_experience
        shape="person_"+str(i)
        prof=data.profiles[i]
        exper = prof.exper

        w=worker(n,shape=shape,assignment=rec,profile=prof)
        i+=1
        rec.ls_worker.append(w)
        w.move_to(rec)
        w.fd(8)
    
        
        pass
def set_products(n):

    i=0
    for ws in list_workstation:
        j=0
        while j < ws.nppar and j <list_nppar_i[i]:
            p=product(n)
            p.tache_encours=i
            p.plist_tache[i].dj=0
            p.move_to(ws)
            ws.prd_encours.append(p)
            j+=1
        i+=1
    pass
# def set_taches(n):
#     for i in range(n_tache):
#         ws=list_workstation[i]
#         tach=tache(i,pt_tache[i],ws,pt_min_tache[i],pt_max_tache[i])
#         list_tache.append(tach)

#     # list_tache[0].dj=0
#     pass  
def configuration_initiale(n):
    set_workstations(n)
    set_workers(n)
    # set_taches(n)
    set_products(n)
class turtle:
    def __init__(self,n):
        self.id= id
        self.n= n
    def distanceto(self,n,fr=0,id_target=1):
        c = "distanceto "+list2nllist([fr,id_target])
        c = self.n.report(c)
        idd = int(c[:-2])
        return idd
    def face_to(self,n,fr=0,id_target=1):
        c="faceto "+list2nllist([fr,id_target])
        c=self.n.report(c)
        idd= int(c[:-2])
        return idd
    def move_to(self,id_target):
        fr=self.id
        c="moveto "+list2nllist([fr,id_target.id])
        c=self.n.report(c)

    def hideturtle(self):
        turtleid=self.id
        c="hideturtle "+list2nllist([turtleid])
        self.n.report(c)
    def set_shape(self,shape):
        turtleid=self.id
        c="set_shape "+list2nllist([turtleid,shape])
        self.n.report(c)


    def fd(self,repeat=1):
        fr=self.id
        c="fdfd "+list2nllist([fr,repeat])
        self.n.report(c)

class tache:
    def __init__(self,id=0, pt=0,ws=0,pt_min=0,pt_max=0):
        self.dj = 'False'
        self.id = id
        self.pt = pt
        self.pt_min = pt_min
        self.pt_max = pt_max
        self.cj = 0
        self.pt_pass=0
        self.fin= 'False'
        self.ws= ws
    def update(self,time_now):
        if self.dj!="False":
            self.update_pt_pass()
            if self.pt_pass >= self.pt :
                self.fin=True
                self.cj=time_now
    def tout_contrainte(self):
        a = self.contr_worker()
        b = self.contr_machine_panee()
        c = self.contr_experience()
        d = True
        e = True
        tout = a and b and c and d and e
        return tout
    def update_pt_pass(self):
        if self.tout_contrainte():
            d=self.value_add_to_pt_pass()
            self.pt_pass+=d

    def contr_worker(self):
        ln=len(self.ws.ls_worker)
        if ln >0:
            return True
        return False

    def contr_machine_panee(self):
        
        return True
    def contr_experience(self):
        
        return True
    # value_add_to_pt_pass
    def value_add_to_pt_pass(self):
        wrk=self.ws.ls_worker[0]

        # self.pt_min
        # self.pt_max
        v=wrk.profile.exper/15

        return v
        # return 1

    
class job :
    def __init__(self, id=0):
        self.id = id
        self.lst_Tache = []
class np_zone (turtle):
    def __init__(self,n,x=0,y=0,id=0,shape="car",size_shape=4,color=0,typ="zn_p",name="zn",labelcolor=0):
        super().__init__(n)
        self.id = id
        self.typ = typ
        self.ls_worker = []
        self.create_zone_xyid(n,x,y,id,shape,size_shape,color,typ,name,labelcolor)
    def create_zone_xyid(self,n,x,y,id,shape,size_shape,color,typ,name,labelcolor):
        c="create-zone-xyid "+list2nllist([x,y,id,shape,size_shape,color,typ,name,labelcolor])
        c=n.report(c)
        self.id = int(c[:-2])
        list_zone.append(self)
        return self
class workstation(turtle) :
    def __init__(self, n,x=0,y=0,id=0,shape="car",size_shape=4,color=0,typ="zn_p",name="zn",labelcolor=0,nppar=1):
        
        super().__init__(n)
        self.id = id
        self.typ = typ
        self.prd_encours = []
        self.bfr_prd_encours = []
        self.nppar=nppar
        self.next_ws=self
        self.fin="False"
        self.ls_worker = []
        self.create_workstation_xyid(n,x,y,id,shape,size_shape,color,typ,name,labelcolor,nppar)
    def update(self,n,n_tache,time_now):
        
        for rec in self.prd_encours:
            rec.update(n,n_tache,time_now)
        for rec in self.prd_encours:
            rec.update2(n,n_tache,time_now)
        for rec in self.bfr_prd_encours:
                self.prd_encours.append(rec)
                self.bfr_prd_encours.remove(rec)
        
        pass
  
        
    def create_workstation_xyid(self,n,x,y,id,shape,size_shape,color,typ,name,labelcolor,nppar):
        c="create-workstation-xyid "+list2nllist([x,y,id,shape,size_shape,color,typ,name,labelcolor])
        c=n.report(c)
        self.id= int(c[:-2])
        list_workstation.append(self)
        return self
class street :
    def __init__(self, n,fromm=0,too=1,label="street",id_s=0,labelcolor=0,color=0,shape="aa",thickness=0.5):
        self.id = id
        self.create_street_ft(n,fromm,too,label,id_s,labelcolor,color,shape,thickness)
    def create_street_ft(self,n,fromm=0,too=1,label="street",id_s=0,labelcolor=0,color=0,shape="aa",thickness=0.5):
        c="create-street-ft "+list2nllist([fromm,too,label,id_s,labelcolor,color,shape,thickness])
        c=n.report(c)
        self.id= int(c[:-2])
        list_street.append(self)
        return self

class product(turtle):
    def __init__(self, n,x=0,y=0,id=0,shape="p_robot00",size_shape=6,assignment=None,inf={}):
        super().__init__(n)
        self.id = id
        self.assignment = assignment
        self.inf=inf
        self.plist_tache=[]
        self.get_plist_tache()
        
        # self.list_tache=list_tache

        self.tache_encours=0
        self.fin= 'False'
        self.create_product_xyid(n,x,y,id,shape,size_shape)

    
    def get_plist_tache(self):
        for i in range(n_tache):
            ws=list_workstation[i]
            tach=tache(i,pt_tache[i],ws,pt_min_tache[i],pt_max_tache[i])
            tmin=tach.pt_min
            tmax=tach.pt_max
            prof=data.profiles[i]
            exper = prof.exper
            # contr_experience
            tach.pt=tmin+((exper/30)*(tmax-tmin))

            self.plist_tache.append(tach)

    # list_tache[0].dj=0
    pass  
    def create_product_xyid(self,n,x,y,id,shape,size_shape):
        c="create-product-xyid "+list2nllist([x,y,id,shape,size_shape])
        c=n.report(c)
        self.id = int(c[:-2])
        list_product.append(self)
        return self

    def update(self,n,n_tache,time_now):
        if self.fin=="False" :
            tache_encours=self.plist_tache[self.tache_encours]
            tache_encours.update(time_now)
    
    def update2(self,n,n_tache,time_now):
        if self.fin=="False" :
            #  data 
            tache_encours=self.plist_tache[self.tache_encours]
            ws=tache_encours.ws
            


            if tache_encours.fin != "False":
                self.tache_encours+=1
                # pr
                ws.prd_encours.remove(self)
                if self.tache_encours == n_tache:
                    # pr
                    self.fin= True
                    self.hideturtle()
                else:
                    #  data 
                    next_tache_encours=self.plist_tache[self.tache_encours]
                    next_ws=tache_encours.ws.next_ws
                    
                    #tache
                    # next_tache_encours.pt_pass=0
                    next_tache_encours.dj=time_now
                    # next_tache_encours.fin = "False"
                    # pr

                    next_ws.bfr_prd_encours.append(self)
                    shape="p_robot0"+str(next_ws.id)
                    self.set_shape(shape)
                    self.move_to(next_ws)
                    # ws
                    if ws.id==0:
                        ws=list_workstation[0]
                        global n_robot
                        n_robot =n_robot+1
                        p=product(n,shape="p_robot00")
                        # p.tache_encours=0
                        p.plist_tache[0].dj=time_now
                        # p.plist_tache[0].pt_pass=0
                        # p.plist_tache[0].fin = "False"
                        ws.bfr_prd_encours.append(p)
                        p.move_to(ws)
            pass

class worker (turtle):
    def __init__(self,n,x=0,y=0,id=0,shape="person",size_shape=6,assignment=None,profile={}):
        super().__init__(n)
        self.id = id
        self.assignment = assignment
        self.assignment_now = assignment
        self.profile=profile
        self.create_worker_xyid(n,x,y,id,shape,size_shape,assignment)

    def update(self,n):
        w=self.id
        r=random.randint(0,3)
        
        if r==0:
            z=self.assignment
        else:
            r=r-1

            z=list_zone[r]
        self.assignment_now.ls_worker.remove(self)
        self.assignment_now=z
        z.ls_worker.append(self)
        self.move_to(z)

        # mt_10=[[0.8,0.2,0,0],[0.6,0.2,0.1,0.1],[0,0.3,0.4,0.3],[0,0.3,0.3,0.4]]
        # nw=2
        # snow=0
        # ns=4
        # M = np.array(mt_10   )
        # print(np.random.choice(np.arange(0,ns), p=M[snow]))
    def create_worker_xyid(self,n,x,y,id,shape,size_shape,assignment):
        c="create-worker-xyid "+list2nllist([x,y,id,shape,size_shape])
        c=n.report(c)
        self.id= int(c[:-2])
        list_worker.append(self)
        return self
