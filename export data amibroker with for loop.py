import pandas as pd
from jugaad_data.nse import bhavcopy_save
from datetime import datetime

dt = pd.date_range(start="27/03/2023", end="27/03/2023",freq='B')
for tday in dt:
    try:
        dMMyFomatUpperCase = datetime.strftime(tday,'%Y,%b,%d')
        Fomatfilename = datetime.strftime(tday,'%d%b%Y').upper
        #Formatfile_int = int (Fomatfilename)
        
        bhavcopy_save(datetime(dMMyFomatUpperCase),"")
        #bc=pd.read_csv('cm23MAR2023bhav.csv')

        
        data = pd.read_csv('cm27MAR2023bhav.csv')
        data = data[data['SERIES']== 'EQ']
        result = data[['SYMBOL','TIMESTAMP','OPEN','HIGH','LOW','CLOSE','TOTTRDQTY','TOTALTRADES']]
        print("Inside get data")
        # save the CSV file
        #filenamedata = datetime.strftime("06",'%m%d%y').upper
        filename = 'cm23MAR2023bhav.csv'+ '_NSE.txt'
        result.to_csv('D:\\program codes\\Python\\Amibroker data script' +filename, header=False, index=False )
        print("Data Successfully write for ")
        print("Inside Save CSV")
    except Exception as e:
        print("Oops! Error in", datetime.strftime(tday,'%m%d%Y'),e)
        print("Inside exception")
