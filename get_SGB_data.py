import pandas as pd
from jugaad_data.nse import bhavcopy_save, full_bhavcopy_save
import datetime as dt
import sys
import os

def get_date_from_input():
  """Gets the date from the command line input.

  Returns:
    A datetime object representing the input date.
  """
  if len(sys.argv) > 1:
    date_str = sys.argv[1]
    try:
      return dt.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
      print("Invalid date format.")
      return None
  else:
    return dt.datetime.now()

def get_output_directory_from_input():
  """Gets the output directory from the command line input.

  Returns:
    A string representing the output directory.
  """
  if len(sys.argv) > 2:
    output_dir = sys.argv[2]
  else:
    output_dir = os.getcwd()
  return output_dir


input_date = get_date_from_input()
input_outdir = get_output_directory_from_input()

#down_date = datetime(2023,8,25)
down_date = dt.datetime.combine(input_date, dt.time.min)
print(f"Downloading data for : {down_date}")

bhavcopy_save(down_date, input_outdir)

down_date_str = down_date.strftime("%d%b%Y")
print(f"down_date_str={down_date_str}")

input_csv_file = os.path.join(input_outdir, f"cm{down_date_str}bhav.csv")
print(f"input_csv_file={input_csv_file}")

data = pd.read_csv(f'{input_csv_file}')
data = data[data['SERIES']== 'GB']
result = data[['SYMBOL','TIMESTAMP','OPEN','HIGH','LOW','CLOSE','TOTTRDQTY','TOTALTRADES']]

print("complete get data")

# save the CSV file
filename = os.path.join(input_outdir, f'{down_date_str}_NSE.txt')
result.to_csv(filename, header=False, index=False)
print(f"Successfully wrote : {filename}")
