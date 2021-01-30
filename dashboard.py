import streamlit as st
import pandas as pd
import numpy as np

st.title("Patient DashBoard")
st.sidebar.title("DashBoard")
st.sidebar.markdown("All the required details at one place.")

#--------------------------------------------DATA IMPORTING START------------------------------------------------------------------#
#@st.cache(persist=True)
@st.cache(allow_output_mutation=True)
def load_details():
	details=pd.read_csv("patients.csv")
	return (details)
patient_details=load_details()

@st.cache(allow_output_mutation=True)
def load_observations():
	details=pd.read_csv("observations.csv")
	return (details)
patient_observations=load_observations()

@st.cache(allow_output_mutation=True)
def load_condition():
	details=pd.read_csv("conditions.csv")
	return (details)
patient_conditions=load_condition()

@st.cache(allow_output_mutation=True)
def load_allergies():
	details=pd.read_csv("allergies.csv")
	return (details)
patient_allergies=load_allergies()

@st.cache(allow_output_mutation=True)
def load_careplans():
	details=pd.read_csv("careplans.csv")
	return (details)
patient_careplans=load_careplans()

@st.cache(allow_output_mutation=True)
def load_devices():
	details=pd.read_csv("devices.csv")
	return (details)
patient_devices=load_devices()

@st.cache(allow_output_mutation=True)
def load_suppliers():
	details=pd.read_csv("providers.csv")
	return(details)
suppliers=load_suppliers()

#-------------------------------------------------DATA IMPORTING END----------------------------------------------------------------#




#----------------------------------------------------DATA CLEARING START------------------------------------------------------------#
patient_details['PREFIX'] = patient_details['PREFIX'].str.replace('\f+',' ')
patient_details['MAIDEN'] = patient_details['MAIDEN'].str.replace('\f+','')

index=0
for i in patient_details["PREFIX"]:
    if not(isinstance(i, str)):
         patient_details["PREFIX"][index]=''
    index=index+1
    
index=0
for i in patient_details["FIRST"]:
    patient_details["FIRST"][index]=''.join([i for i in i if not i.isdigit()])
    index=index+1;
    
index=0
for i in patient_details["LAST"]:
    patient_details["LAST"][index]=''.join([i for i in i if not i.isdigit()])
    index=index+1;
    
index=0
for i in patient_details["MAIDEN"]:
    if (isinstance(i, str)):
        patient_details["MAIDEN"][index]=''.join([i for i in i if not i.isdigit()])
    else:
        patient_details["MAIDEN"][index]=''        
    index=index+1;

index=0
for i in patient_details["MARITAL"]:
    if(i=="M"):
        patient_details["MARITAL"][index]="Marrried"
    elif(i=="S"):
        patient_details["MARITAL"][index]="Single"
    elif(i==''):
        patient_details["MARITAL"][index]="N/A"
    index=index+1;

index=0
for i in patient_details["GENDER"]:
    if(i=="M"):
        patient_details["GENDER"][index]="Male"
    if(i=="F"):
        patient_details["GENDER"][index]="Female"
    index=index+1;

#----------------------------------------------------DATA CLEARING END--------------------------------------------------------------#




#------------------------------------------Display Function---------------------------------------------#
	
def main_display():
	st.sidebar.subheader("Patient Details to Display:")
	choice = st.sidebar.radio('', ('Personal Details', 'Patient Obsevations', 'Patient Allergies' , 'Patient Conditions' , 'Monitoring Devices'))
	if(choice=='Personal Details'):
		st.write("\n")
		st.subheader("Personal Details of the Patient-")
		index=-1
		for i in patient_details["Id"]:
			index=index+1
			if patient_id==i:
				st.write("Address of the patient: "+patient_details["ADDRESS"][index]+", "+patient_details["CITY"][index]+", "+patient_details["STATE"][index]+", "+patient_details["COUNTY"][index])
				st.write("Zip Code-"+str(patient_details["ZIP"][index]))
				st.write("Gender of the patient: "+patient_details["GENDER"][index])
				st.write("Race of the patient: "+patient_details["RACE"][index])
				st.write("Ethnicity of the patient: "+patient_details["ETHNICITY"][index])
		#st.write("Marital Status of patient: "+patient_details["MARITAL"][index])

	if(choice=='Patient Obsevations'):
		st.write("\n")
		st.subheader("Medical Details of the Patient-")
		index=0
		reading=0
		st.markdown("#### Observation:"+str(reading+1))
		reading=reading+1
		for i in patient_observations["PATIENT"]:
			if patient_id==i:
				if(patient_observations["DESCRIPTION"][index]!='QOLS')and(patient_observations["DESCRIPTION"][index]!='DALY')and(patient_observations["DESCRIPTION"][index]!="QALY"):
					if("/uL" in str(patient_observations["UNITS"][index])):
						st.write(patient_observations["DESCRIPTION"][index]+": "+str(patient_observations["VALUE"][index])+" x "+str(patient_observations["UNITS"][index]))
					else:
						st.write(patient_observations["DESCRIPTION"][index]+": "+str(patient_observations["VALUE"][index])+""+str(patient_observations["UNITS"][index]))	

					if(patient_observations["DESCRIPTION"][index]=="Tobacco smoking status NHIS"):
						st.markdown("#### Observation:"+str(reading+1))
						reading+=1
					index=index+1

	if(choice=='Patient Allergies'):
		st.write("\n")
		st.subheader("Allergies suffered by the Patient-")
		index=0
		found=0
		for i in patient_allergies["PATIENT"]:
			if patient_id==i:
				st.write(str(patient_allergies["DESCRIPTION"][index]))
				found=1
			index=index+1

		if found==0:
			st.write("No Allergies to Report.")
		else:
			st.markdown("### Take care of these while interacting with Patient")

	if(choice=='Patient Conditions'):
		st.write("\n")
		st.subheader("Patient is suffering from:")
		index=0
		for i in patient_conditions['PATIENT']:
			if patient_id==i:
				st.write(patient_conditions['DESCRIPTION'][index])
				index=index+1

		index=0
		st.subheader("Patient's careplan to Keep in Mind-:")
		for i in patient_careplans['PATIENT']:
			if i==patient_id:
				st.write(patient_careplans['DESCRIPTION'][index])
			index=index+1


	if(choice=='Monitoring Devices'):
		st.write("\n")
		st.subheader("Monitoring devices/Implants for the Patient")
		index=0
		found=0
		for i in patient_devices['PATIENT']:
			if i==patient_id:
				st.write("Device: "+patient_devices['DESCRIPTION'][index])
				st.write("Device id:"+patient_devices['UDI'][index])
				found=1
			index=index+1
		if found==0:
			st.write("No Implants/Devices for the Patient.")

#------------------------------------------------------------------------------------------------------------#






#---------------------------------------------------Final working-------------------------------------------------------------------#
patient_id = st.text_input("ENTER THE PATIENT ID:")

if(patient_id!=""):
	st.markdown("#### Patient ID: "+ patient_id)
	index=-1;
	for i in patient_details["Id"]:
		index=index+1
		if patient_id==i:
			 st.markdown("#### Patient Name: "+patient_details["PREFIX"][index]+" "+patient_details["FIRST"][index]+" "+patient_details["LAST"][index]+" "+patient_details["MAIDEN"][index])       
	main_display()
else:
	st.markdown("#### Patient ID: ")
	st.markdown("#### Patient Name: ")
	choice = st.sidebar.radio('', ('Personal Details', 'Patient Obsevations', 'Patient Allergies' , 'Patient Conditions' , 'Monitoring Devices'))
	if(choice=='Personal Details'):
		st.write("\n")
		st.subheader("Personal Details of the Patient-")
	
	if(choice=='Patient Obsevations'):
		st.write("\n")
		st.subheader("Medical Details of the Patient-")
	
	if(choice=='Patient Allergies'):
		st.write("\n")
		st.subheader("Allergies suffered by the Patient-")
	
	if(choice=='Patient Conditions'):
		st.write("\n")
		st.subheader("Patient is suffering from-")
	
	if(choice=='Monitoring Devices'):
		st.write("\n")
		st.subheader("Monitoring devices/Implants for the Patient-")
	
st.sidebar.subheader("Medical Suppliers Loacations")
if st.sidebar.checkbox("Show", True, key='0'):
	st.subheader("Locations of Medical Suppliers in Massachusetts")
	st.map(suppliers)
