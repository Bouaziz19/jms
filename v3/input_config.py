from model import *

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
    profile_0=profile(0,mt_0,0)
    profile_1=profile(1,mt_1,0)
    profile_2=profile(2,mt_2,0)
    profile_3=profile(3,mt_3,0)
    profile_4=profile(4,mt_4,0)
    profile_5=profile(5,mt_5,0)
    profile_6=profile(6,mt_6,0)
    profile_7=profile(7,mt_7,0)
    profile_8=profile(8,mt_8,0)
    profile_9=profile(9,mt_9,0)
    profile_10=profile(10,mt_10,0)
    profile_11=profile(11,mt_11,0)
    profile_12=profile(12,mt_12,0)
    profile_13=profile(13,mt_13,0)
    prfls=[profile_0,profile_1,profile_2,profile_3,profile_4,profile_5,profile_6,profile_7,profile_8,profile_9,profile_10,profile_11,profile_12,profile_13]
    return prfls
    
data={
    "profiles":get_lis_prof()
}
