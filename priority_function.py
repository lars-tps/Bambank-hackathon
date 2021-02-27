#profile : ID , age , state_of_infection (1 : infected , 0 : not infected) , coordinates ( x,y) , residency_status ( 1: local, 0 : foreign))
profile=[[132435465,19,0,(1.3454,1.12345),1],[12354787622,20,0,(1.234214,1.19284072),1],[124566,80,0,(1.222,1.22233),1]]
def priority(profile):
    """ function    : to set priority level based on certain age group
        input  : id, age, infection_status (0 means not infected , 1 means infected) , coordinates, residency
        output : priority level : local_high(6), local_medium(5) , local_low (4), foreign(3), foreign(2) ,foreign(1) ,N/A(0)"""
    priority_level=1
    for i in range(len(profile)):
        if profile[i][2]==1 :
            priority_level=0
        elif profile[i][4]==0:
            if 18<=profile[i][1]<=50:
                priority_level=3
            elif profile[i][1]<18:
                priority_level=2
            elif profile[i][1]>50:
                priority_level=1
        elif profile[i][4]==1:
            if 18<=profile[i][1]<=50:
                priority_level=6
            elif profile[i][1]<18:
                priority_level=5
            elif profile[i][1]>50:
                priority_level=4
        profile[i].append(priority_level)
    return profile

def priority_sort(profile):
    """function : sort id based on age and priority_level"""
    profile=priority(profile)
    priority_sorted_profile=sorted(profile,key=lambda l:l[5], reverse=True)
    return priority_sorted_profile


print(priority_sort(profile))





