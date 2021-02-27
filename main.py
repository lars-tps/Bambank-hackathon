from qrcode_generator import make_qr
import csv
from priority_function import priority_sort
if __name__=='__main__':
    profiles=[]
    with open('data.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        start=False
        for line in csv_reader:
            if start:
                residency_status=0 if line[5]=='Foreigner' else 1
                profiles.append([line[0],int(line[1]),line[2],(line[3],line[4]),residency_status])
            start=True
    temp=priority_sort(profiles)
    
    