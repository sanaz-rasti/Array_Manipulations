# load dependencies
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
pd.set_option("display.precision", 2)


# Read the data in .csv
df = pd.read_csv("synthetic_ehr.csv")
print(f' df_shape: {df.shape}')
print(f'df_columns: {df.columns}')
df.head()

# we assume the clinics are spread over 5 counties: 
lst_clinic_names = list(df['clinic_name'].drop_duplicates())
county_dic = {'county1':lst_clinic_names[:20], 'county2':lst_clinic_names[20:40], 
              'county3':lst_clinic_names[40:60], 'county4':lst_clinic_names[60:80], 'county5':lst_clinic_names[80:] }
county = ['county1','county2','county3','county4','county5']


## Find min max consultation_date
# to find date information from counties
# County1
datel = list(df[df['clinic_name'].isin(county_dic['county1'])].consultation_date.drop_duplicates())
datelp = []
for i in datel:
    s = str(i)
    year = s[:4]
    month = s[4:6]
    day = s[6:]
    date = year+'-'+month+'-'+day
    datelp.append(date)
print(f'Data range for county1 spans from: {min(datelp)} to {max(datelp)}')


# calculate the population for the last five years, for each county: 
year = [2019, 2020,2021, 2022, 2023,2024]
dataa = []
pop_dic = {'county1':[],'county2':[],'county3':[],'county4':[],'county5':[]}
for c in county:
    dataa = []
    #for yr < 1800:
    datel = df[df['clinic_name'].isin(county_dic[c])][['consultation_date','patient_id']]
    dataa.append(len(datel[datel['consultation_date']<20190000].patient_id))         

    #for yr < 1910:
    datel = df[df['clinic_name'].isin(county_dic[c])][['consultation_date','patient_id']]
    dataa.append(len(datel[datel['consultation_date']<20200000].patient_id))        

    #for yr < 1940: 
    datel = df[df['clinic_name'].isin(county_dic[c])][['consultation_date','patient_id']]
    dataa.append(len(datel[datel['consultation_date']<20210000].patient_id))         
        

    # for yr < 1970:
    datel = df[df['clinic_name'].isin(county_dic[c])][['consultation_date','patient_id']]
    dataa.append(len(datel[datel['consultation_date']<20220000].patient_id)) 

    # for yr < 2000:
    datel = df[df['clinic_name'].isin(county_dic[c])][['consultation_date','patient_id']]
    dataa.append(len(datel[datel['consultation_date']<20230000].patient_id))  

    #for yr < 2014:
    datel = df[df['clinic_name'].isin(county_dic[c])][['consultation_date','patient_id']]
    dataa.append(len(datel[datel['consultation_date']<20240000].patient_id)) 

    pop_dic[c]=dataa
    del dataa
    
    
# Plot the results:
year = [2019, 2020,2021, 2022, 2023,2024]
# plot line
for c in county: 
    plt.plot(year, pop_dic[c],'o-', label='county1')
plt.ylabel("Number of Patients")
plt.xlabel("YEAR")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
