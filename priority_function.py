#profile : ID , age , state_of_infection (1 : infected , 0 : not infected) , coordinates ( x,y) , residency_status ( 1: local, 0 : foreign))
#profile=[[132435465,19,0,(1.3454,1.12345),1],[12354787622,20,0,(1.234214,1.19284072),1],[124566,80,0,(1.222,1.22233),1],[2134324,60,0,(1.212,1.313),1]]
class Patient:
    def __init__(self,id,age,infection_status,cordsx,cordsy,residency_status):
        self.id=id
        self.age=int(age)
        self.infection_status=infection_status
        self.cordsx=cordsx
        self.cordsy=cordsy
        self.residency_status=0 if residency_status=='Infected' else 1
    def set_priority(self,priority_level):
        self.priority_level=priority_level
def priority(patients):
    """ function    : to set priority level based on certain age group
        input  : id, age, infection_status (0 means not infected , 1 means infected) , coordinates, residency
        output : priority level : local_high(6), local_medium(5) , local_low (4), foreign(3), foreign(2) ,foreign(1) ,N/A(0)"""
    priority_level=1
    for profile in patients:
        if profile.infection_status==1 :
            priority_level=0
        elif profile.residency_status==0:
            if 18<=profile.age<=50:
                priority_level=3
            elif profile.age<18:
                priority_level=2
            elif profile.age>50:
                priority_level=1
        elif profile.residency_status==1:
            if 18<=profile.age<=50:
                priority_level=6
            elif profile.age<18:
                priority_level=5
            elif profile.age>50:
                priority_level=4
        profile.set_priority(priority_level)
    return patients

def priority_sort(patients):
    """function : sort id based on age and priority_level
        for group 3 and 6 : younger age gets higher priority
        for group 2 and 5 : older age gets higher priority
        for group 1 and 4 : younger age gets higher priority
        for group 0 : no need sorting"""
    patients=priority(patients)
    profile6=[]
    profile5=[]
    profile4=[]
    profile3=[]
    profile2=[]
    profile1=[]
    profile0=[]
    priority_sorted_profile=sorted(patients,key=lambda l:l.priority_level, reverse=True)
    for i in priority_sorted_profile:
        if i.priority_level==6:
            profile6.append(i)
        elif i.priority_level==5:
            profile5.append(i)
        elif i.priority_level==4:
            profile4.append(i)
        elif i.priority_level==3:
            profile3.append(i)
        elif i.priority_level==2:
            profile2.append(i)
        elif i.priority_level==1:
            profile1.append(i)
        elif i.priority_level==0:
            profile0.append(i)
    profile6=sorted(profile6,key=lambda l:l.age, reverse = False)
    profile3 = sorted(profile3, key=lambda l: l.age, reverse=False)
    profile5 = sorted(profile5, key=lambda l: l.age, reverse=True)
    profile2 = sorted(profile2, key=lambda l: l.age, reverse=True)
    profile4 = sorted(profile4, key=lambda l: l.age, reverse=False)
    profile1 = sorted(profile1, key=lambda l: l.age, reverse=False)
    priority_sorted_profile=[]+profile6+profile5+profile4+profile3+profile2+profile1+profile0
    return priority_sorted_profile


#print(priority_sort(profile))





