
global data
class profile :
    def __init__(self, id=0,mat_t=[],exper=1):
        self.id = id
        self.mat_t = mat_t
        self.exper = exper
class defDictToObject(object):

    def __init__(self, myDict):
        for key, value in myDict.items():
            if type(value) == dict:
                setattr(self, key, defDictToObject(value))
            else:
                setattr(self, key, value)
list_ag = [[20,25 ,0],[30,25 ,1],[40,25 ,2],[50,25 ,3],[60,25 ,4],[70,25 ,5],[20,50 ,6],[40,50 ,7],[60,50 ,8]]
list_shape =  ["machine" , "machine2" , "machine3" , "machine4" , "machine2", "machineinsp", "cantine", "calling", "infirmary" ]
list_shape_size =  [11,11,11,11,11,11,5,5,5]
list_shape_color =  [0,0,15,105,5,5,5,3,3]
list_link =  [[1,2],[2,3],[3,4],[4,5],[5,6]]
list_ws =  [0,1,2,3,4,5]
# number inisalle de product
np_in=1

def get_lis_prof():
    mt_0=[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
    mt_1=[[0.95,0.05,0,0],[0.95,0.05,0,0],[1,0,0,0],[1,0,0,0]]
    mt_2=[[0.95,0.05,0,0],[0.7,0.3,0,0],[1,0,0,0],[1,0,0,0]]
    mt_3=[[0.9,0.1,0,0],[0.95,0.05,0,0],[1,0,0,0],[1,0,0,0]]
    mt_4=[[0.9,0.1,0,0],[0.9,0.1,0,0],[1,0,0,0],[1,0,0,0]]
    mt_5=[[0.95,0.05,0,0],[0.7,0.3,0,0],[1,0,0,0],[1,0,0,0]]
    mt_6=[[0.7,0.3,0,0],[0.95,0.05,0,0],[1,0,0,0],[1,0,0,0]]
    mt_7=[[0.7,0.3,0,0],[0.7,0.3,0,0],[1,0,0,0],[1,0,0,0]]
    mt_8=[ [0.95,0.05,0,0],[0.95,0.03,0.01,0.01],[0,0.3,0.4,0.3],[0,0.3,0.4,0.3]]
    mt_9=[[0.95,0.05,0,0],[0.95,0.03,0.01,0.01],[0.95,0.01,0.03,0.01],[0.95,0.01,0.01,0.03]]
    mt_10=[[0.8,0.2,0,0],[0.6,0.2,0.1,0.1],[0,0.3,0.4,0.3],[0,0.3,0.3,0.4]]
    mt_11=[[0.8,0.2,0,0],[0.6,0.2,0.1,0.1],[0.6,0.1,0.2,0.1],[0.6,0.1,0.1,0.2]]
    mt_12=[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
    mt_13=[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
    profile_0=profile(0,mt_0,15)
    profile_1=profile(1,mt_1,30)
    profile_2=profile(2,mt_2,25)
    profile_3=profile(3,mt_3,1)
    profile_4=profile(4,mt_4,2)
    profile_5=profile(5,mt_5,5)
    prfls=[profile_0,profile_1,profile_2,profile_3,profile_4,profile_5]
    return prfls
    
data_d={
    "profiles":get_lis_prof(),
    "list_ag":list_ag,
    "list_shape":list_shape,
    "list_shape_size":list_shape_size,
    "list_shape_color":list_shape_color,
    "list_link":list_link,
    "list_ws":list_ws,
}
data=defDictToObject(data_d)