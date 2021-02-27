#profile : ID , age , state_of_infection (1 : infected , 0 : not infected) , coordinates ( x,y) , residency_status ( 1: local, 0 : foreign))
profile=[[132435465,19,0,(1.3454,1.12345),1],[12354787622,20,0,(1.234214,1.19284072),1],[124566,80,0,(1.222,1.22233),1],[2134324,60,0,(1.212,1.313),1]]

def priority(profile):
    """ function    : to set priority level based on certain age group
        input  : id, age, infection_status (0 means not infected , 1 means infected) , coordinates, residency
        output : priority level : local_high(6), local_medium(5) , local_low (4), foreign(3), foreign(2) ,foreign(1) ,N/A(0)"""
    priority_level=1
    for i in range(len(profile)):
        if profile[i][2]==1 :
            priority_level=0
        elif profile[i][5]== 0:
            if 18<=profile[i][1]<=50:
                priority_level=3
            elif profile[i][1]<18:
                priority_level=2
            elif profile[i][1]>50:
                priority_level=1
        elif profile[i][5] == 1:
            if 18<=profile[i][1]<=50:
                priority_level=6
            elif profile[i][1]<18:
                priority_level=5
            elif profile[i][1]>50:
                priority_level=4
        profile[i].append(priority_level)
    return profile

def priority_sort(profile):
    """function : sort id based on age and priority_level
        for group 3 and 6 : younger age gets higher priority
        for group 2 and 5 : older age gets higher priority
        for group 1 and 4 : younger age gets higher priority
        for group 0 : no need sorting"""
    profile=priority(profile)
    profile6=[]
    profile5=[]
    profile4=[]
    profile3=[]
    profile2=[]
    profile1=[]
    profile0=[]
    priority_sorted_profile=sorted(profile,key=lambda l:l[5], reverse=True)
    for i in priority_sorted_profile:
        if i[6]==6:
            profile6.append(i)
        elif i[6]==5:
            profile5.append(i)
        elif i[6]==4:
            profile4.append(i)
        elif i[6]==3:
            profile3.append(i)
        elif i[6]==2:
            profile2.append(i)
        elif i[6]==1:
            profile1.append(i)
        elif i[6]==0:
            profile0.append(i)
    profile6=sorted(profile6,key=lambda l:l[1], reverse = False)
    profile3 = sorted(profile3, key=lambda l: l[1], reverse=False)
    profile5 = sorted(profile5, key=lambda l: l[1], reverse=True)
    profile2 = sorted(profile2, key=lambda l: l[1], reverse=True)
    profile4 = sorted(profile4, key=lambda l: l[1], reverse=False)
    profile1 = sorted(profile1, key=lambda l: l[1], reverse=False)
    priority_sorted_profile=[]+profile6+profile5+profile4+profile3+profile2+profile1+profile0
    return priority_sorted_profile



