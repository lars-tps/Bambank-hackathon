from qrcode_generator import make_qr
from ClosestHospital import calculate,calcDistance
import csv
from priority_function import priority_sort
def insert_profiles():
    #getting the patient profiles and sorting them based on their priority level
    profiles=[]
    with open('data.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        start=False
        for line in csv_reader:
            if start:
                residency_status=0 if line[5]=='Foreigner' else 1
                profiles.append([line[0],int(line[1]),line[2],(line[3],line[4]),residency_status])
            start=True
    profiles=priority_sort(profiles)
    return profiles

def insert_to_hospital(profiles):
    with open('hospital_data.csv','r') as csv_file:
        hospital=csv.reader(csv_file)
        start=False
        for line in hospital:
            temp=profiles
            save=[]
            if start:
                for i in temp:
                    save.append(i[0]+','+str(i[1])+','+i[2]+','+str(calcDistance(int(i[3][0]),int(i[3][1]),int(line[3]),int(line[4])))+'\n')
                with open(line[0]+'_'+line[1]+'.csv','w+') as hospital_data:
                    for i in save:
                        hospital_data.writelines(i)  
            start=True
        
if __name__=='__main__':
    profiles=insert_profiles()
    insert_to_hospital(profiles)



    
    