import pandas as pd
from jugaad_data.nse import bhavcopy_save, full_bhavcopy_save
from datetime import datetime
bhavcopy_save(datetime(2023,7,10),"")
#bc=pd.read_csv('cm23MAR2023bhav.csv')
#full_bhavcopy_save(datetime(2023,3,28),"")


data = pd.read_csv('cm10JUL2023bhav.csv')
data = data[data['SERIES']== 'GB']
result = data[['SYMBOL','TIMESTAMP','OPEN','HIGH','LOW','CLOSE','TOTTRDQTY','TOTALTRADES']]
#fulldata = pd.read_csv('sec_bhavdata_full_04Aug2023bhav.csv')

print("complete get data")


# save the CSV file
#filenamedata = datetime.strftime("06",'%m%d%y').upper
filename = 'Final10JUL2023bhav.csv'+ '_NSE.txt'
result.to_csv('D:\\program codes\\Python\\Amibroker data script' +filename, header=False, index=False )
print("Data Successfully write for ")
print("Inside Save CSV")