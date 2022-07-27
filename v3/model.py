import copy
import allfunction as allf
# import sum as sum
global list_worker
global list_product
global list_zone
global list_workstation
global list_tache
list_worker=[]
list_product=[]
list_zone=[]
list_workstation=[]
list_street=[]
list_tache=[]
def list2nllist(lis):
        s="["
        for i in lis:
            if type(i) == str:
                s+=' "'+i+'" '
            else :
                s+=' '+str(i)+' '
        s+="]"
        return s
class turtle:
    def __init__(self,n):
        self.id= id
        self.n= n
    def distanceto(self,n,fr=0,id_target=1):
        c = "distanceto "+list2nllist([fr,id_target])
        
        c = n.report(c)
        idd = int(c[:-2])
        return idd
    def face_to(self,n,fr=0,id_target=1):
        c="faceto "+list2nllist([fr,id_target])

        c=n.report(c)
        idd= int(c[:-2])
        return idd
    def move_to(self,id_target=1):
        print("*************")
        print(self.id)
        fr=self.id
        c="moveto "+list2nllist([fr,id_target])
        c=self.n.report(c)
        # self.id= int(c[:-2])
        # return self
    def hideturtle(self):
        turtleid=self.id
        c="hideturtle "+list2nllist([turtleid])

    def fd(self,repeat=1):
        fr=self.id
        c="fdfd "+list2nllist([fr,repeat])
class tache:
    def __init__(self,id=0, pt=0,ws=0):
        self.dj = 'False'
        self.id = id
        self.pt = pt
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
        c = True
        d = True
        e = True
        tout = a and b and c and d and e
        return tout
    def update_pt_pass(self):
        if self.tout_contrainte():
            self.pt_pass+=1

    def contr_worker(self):
        
        return True

    def contr_machine_panee(self):
        
        return True
class job :
    def __init__(self, id=0):
        self.id = id
        self.lst_Tache = []
class np_zone (turtle):
    def __init__(self,n,x=0,y=0,id=0,shape="car",size_shape=4,color=0,typ="zn_p",name="zn",labelcolor=0):
        super().__init__(n)
        self.id = id
        self.typ = typ
        self.create_zone_xyid(n,x,y,id,shape,size_shape,color,typ,name,labelcolor)
    def create_zone_xyid(self,n,x,y,id,shape,size_shape,color,typ,name,labelcolor):
        c="create-zone-xyid "+list2nllist([x,y,id,shape,size_shape,color,typ,name,labelcolor])
        c=n.report(c)
        print(c[:-2])
        self.id = int(c[:-2])
        list_zone.append(self)
        return self
class workstation(turtle) :
    def __init__(self, n,x=0,y=0,id=0,shape="car",size_shape=4,color=0,typ="zn_p",name="zn",labelcolor=0,nppar=1):
        
        super().__init__(n)
        self.id = id
        self.typ = typ
        self.prd_encours = []
        self.nppar=nppar
        self.next_ws=self
        self.fin="False"
        self.create_workstation_xyid(n,x,y,id,shape,size_shape,color,typ,name,labelcolor,nppar)
    def update(self,n,n_tache,time_now):
        print(self.prd_encours)

        for rec in self.prd_encours:
            rec.update(n,n_tache,time_now)
    def create_workstation_xyid(self,n,x,y,id,shape,size_shape,color,typ,name,labelcolor,nppar):
        c="create-workstation-xyid "+list2nllist([x,y,id,shape,size_shape,color,typ,name,labelcolor])
        c=n.report(c)
        self.id= int(c[:-2])
        list_workstation.append(self)
        return self
    def update2(self,n,n_tache,time_now):
        for rec in self.prd_encours:
            if rec.fin =='False':
                tache_encours=rec.list_tache[rec.tache_encours]
                if tache_encours.fin != "False":
                    self.prd_encours.remove(rec)
                    self.next_ws.prd_encours.append(rec)
                    rec.fin="False"
                    rec.dj="False"
                    self.fin="False"
                    rec.update2(n,n_tache,time_now)
            if rec.fin !='False':
                self.prd_encours.remove(rec)          
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
class profile :
    def __init__(self, id=0,mat_t=[],expr=0):
        self.id = id
        self.mat_t = mat_t
        self.mat_t = expr
class product(turtle):
    def __init__(self, n,x=0,y=0,id=0,shape="p_robot00",size_shape=6,assignment=None,inf={}):
        super().__init__(n)
        self.id = id
        self.assignment = assignment
        self.inf=inf
        # self.list_tache=copy.deepcopy(list_tache)
        self.list_tache=list_tache

        self.tache_encours=0
        self.fin= 'False'
        self.create_product_xyid(n,x,y,id,shape,size_shape)
    def create_product_xyid(self,n,x,y,id,shape,size_shape):
        c="create-product-xyid "+list2nllist([x,y,id,shape,size_shape])
        c=n.report(c)
        self.id = int(c[:-2])
        list_product.append(self)
        return self

    def update(self,n,n_tache,time_now):
        if self.fin=="False" :
            tache_encours=self.list_tache[self.tache_encours]
            tache_encours.update(time_now)
            # if tache_encours.fin != "False":
            #     self.tache_encours += 1

    def update2(self,n,n_tache,time_now):
        if self.fin=="False" :
            tache_encours=self.list_tache[self.tache_encours]
            if tache_encours.fin != "False":
                self.tache_encours+=1
                if self.tache_encours == n_tache:
                    self.fin= True
                    self.hideturtle()
                    print(time_now)
                else:
                    tache_encours=self.list_tache[self.tache_encours]
                    tache_encours.dj=time_now
                    p=self.id
                    z=tache_encours.ws
                    self.move_to(z)
class worker (turtle):
    def __init__(self,n,x=0,y=0,id=0,shape="person",size_shape=6,assignment=None):
        super().__init__(n)
        self.id = id
        self.assignment = assignment
        self.assignment_now = assignment
        self.create_worker_xyid(n,x,y,id,shape,size_shape,assignment)

    def update(self,n):
        w=self.id
        z=self.assignment_now.id
        allf.move_to(n,w,z)
    def create_worker_xyid(self,n,x,y,id,shape,size_shape,assignment):
        c="create-worker-xyid "+list2nllist([x,y,id,shape,size_shape])
        c=n.report(c)
        self.id= int(c[:-2])
        list_worker.append(self)
        return self
