from flask import Flask, url_for, redirect,render_template,request
from qrcode_generator import make_qr
import csv
import os
app= Flask(__name__)
def change_form(time_prompt):
    while(time_prompt.find('_')!=-1):
        idx=time_prompt.find('_')
        time_prompt=list(time_prompt)
        time_prompt[idx]=":"
        time_prompt="".join(time_prompt)
    return time_prompt

@app.route('/')
def home():
    return render_template("Homepage.html")

@app.route('/hospital_page',methods=["POST","GET"])
def hospital_page():
    if request.method=="POST":
       user=request.form['hosp']
       return redirect(url_for('hospital_data',hospital_name=user))
    else:
        return render_template('hospital.html')

@app.route('/hospital_page/<hospital_name>')
#searching for csv files with the name given from the form
def hospital_data(hospital_name):
    data=[]
    with open('hospital_data.csv','r') as csv_file:
        hospitals_data=csv.reader(csv_file)
        for hospital in hospitals_data:
            if hospital[0]==hospital_name:
                file = open(hospital[0]+'_'+hospital[1]+'.csv',"r")
                temp=csv.reader(file)
                for row in temp:
                    data.append(row[0])
                file.close()
    if len(data)>0:
        return render_template('Hospital_patient_data.html',name="hospital_name",patient_data=data)
    else:
        return 'Sorry but your hospital id wasn''t found'

@app.route('/patient_login',methods=["POST","GET"])
def patient_page():
    if request.method=="POST":
        id=request.form['id']
        return redirect(url_for('patient_data',patient_id=id))
    else:
        return render_template('Patient_login.html')

@app.route('/patient_page/<patient_id>',methods=["POST","GET"])
def patient_data(patient_id):
    if request.method=="POST":
        val=request.form['but']
        if val=="Accept":
            make_qr(str(patient_id))
            return redirect(url_for('VaccinationSchedule',id=patient_id))
            
        else:
            return redirect(url_for('home'))
    else:
        with open("patient_hospital_destination.csv",'r') as csv_file:
            patients_data=csv.reader(csv_file)
            for patients in patients_data:
                if patients[0]==patient_id:
                    return render_template('Patient_data_page.html',id=patient_id,loc=patients[1],time_prompt=change_form(patients[2]))
        return "Sorry but you are not registered to receive the vaccine yet"


@app.route('/VaccinationSchedule/<id>')
def VaccinationSchedule(id):
    with open("patient_hospital_destination.csv",'r') as csv_file:
            patients_data=csv.reader(csv_file)
            for patients in patients_data:
                if patients[0]==id:
                    return render_template('MyVaccinationSchedule.html',img_file=str(id)+'.png',id=id,loc=patients[1],time_prompt=change_form(patients[2]))
    return redirect(url_for('home'))
if __name__=='__main__':
    app.run()