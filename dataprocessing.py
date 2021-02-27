from qrcode_generator import make_qr
from ClosestHospital import calculate,calcDistance
import csv
from priority_function import priority_sort
class Hospital:
    def __init__(self,name,time_slots,max_number_of_patients,cordsx,cordsy):
        self.name=name
        self.time_slots=time_slots
        self.max_number_of_patients=int(max_number_of_patients)
        self.cordsx=cordsx
        self.cordsy=cordsy
 
  
class Patient:
    def __init__(self,id,age,infection_status,cordsx,cordsy,residency_status):
        self.id=id
        self.age=int(age)
        self.infection_status=1 if infection_status=="Infected" else 0
        self.cordsx=cordsx
        self.cordsy=cordsy
        self.residency_status=1 if residency_status=='Singaporean Citizen' else 0
    def set_priority(self,priority_level):
        self.priority_level=priority_level


def insert_profiles():
    #getting the patient profiles and sorting them based on their priority level
    profiles=[]
    with open('data.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        start=False
        for line in csv_reader:
            
            if start:
                residency_status=0 if line[5]=='Foreigner' else 1
                patient=Patient(line[0],line[1],line[2],line[3],line[4],line[5])
                profiles.append(patient)
            start=True
    profiles=priority_sort(profiles)
    return profiles

def insert_to_hospital(profiles):
    with open('hospital_data.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        hospitals=[]
        for hospital in csv_reader:
            file = open(hospital[0]+'_'+hospital[1]+'.csv',"w")
            file.write("")
            file.close()
            hospitals.append(Hospital(hospital[0],hospital[1],hospital[2],hospital[3],hospital[4]))
        start=False
        for profile in profiles:
            mn=-1
            save=-1
            for (idx,hospital) in enumerate(hospitals):
                dist=calcDistance(int(profile.cordsx),int(profile.cordsy),int(hospital.cordsx),int(hospital.cordsy))
                if mn==-1 and hospital.max_number_of_patients>0:
                    save=idx
                    mn=dist
                    chosen_hospital=hospital
                    hospital.max_number_of_patients-=1
                elif mn>dist and hospital.max_number_of_patients>0:
                    hospitals[save].max_number_of_patients+=1
                    hospital.max_number_of_patients-=1
                    mn=dist
                    save=idx
                    chosen_hospital=hospital
            
            with open(chosen_hospital.name+'_'+chosen_hospital.time_slots+'.csv','a') as hospital_listed_patient:
                hospital_listed_patient.writelines(str(profile.id)+','+str(profile.age)+','+str(profile.infection_status)+','+profile.cordsx+','+profile.cordsy+','+str(profile.residency_status)+'\n')  
            start=True
        
if __name__=='__main__':
    profiles=insert_profiles()
    insert_to_hospital(profiles)



    
    