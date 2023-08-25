import pandas as pd
from jugaad_data.nse import bhavcopy_save
from datetime import datetime
bhavcopy_save(datetime(2023,3,28),"")
#bc=pd.read_csv('cm23MAR2023bhav.csv')


data = pd.read_csv('cm28MAR2023bhav.csv')
data = data[data['SERIES']== 'EQ']
result = data[['SYMBOL','TIMESTAMP','OPEN','HIGH','LOW','CLOSE','TOTTRDQTY','TOTALTRADES']]
print("Inside get data")
# save the CSV file
#filenamedata = datetime.strftime("06",'%m%d%y').upper
filename = 'cm23MAR2023bhav.csv'+ '_NSE.txt'
result.to_csv('D:\\program codes\\Python\\Amibroker data script' +filename, header=False, index=False )
print("Data Successfully write for ")
print("Inside Save CSV")