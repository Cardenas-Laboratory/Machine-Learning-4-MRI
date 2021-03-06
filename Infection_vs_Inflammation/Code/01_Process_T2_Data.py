import numpy as np
import pandas as pd
from pylab import *
import os

main_dir= "../Study_03_CBA/"

# Create List of T2 MSME data
file_names=list()
for file in os.listdir(main_dir):
    if file.endswith("T2.txt"):
        file_names.append(file)

Txt2DataFrame(main_dir,file_names[0],12)

# Function to convert txt to data frame
def Txt2DataFrame(main_dir,file_name,num_rows):
    f1 = open(main_dir + file_name,'r')
    # Read all lines
    all_lines = f1.readlines()
    f1.close()
    # Select from Fourht line to the end
    first_row_with_data = 3
    all_lines=all_lines[first_row_with_data:]
    # Calculate number of rows
    #num_rows=len(all_lines)
    f1.close()
    num_cols = len( all_lines[0].split()[1::3] )
    np_array=np.zeros( (num_rows,num_cols) )
    for i in range(num_rows):
        l=all_lines[i].split()[1::3]
        np_array[i,:]=array(l)
    # Define Column Names
    column_names=list()
    for i in range(num_cols):
        column_names.append( "ROI_"+str(i+1))
    df=pd.DataFrame(np_array,columns=column_names)
    #df.plot()
    return df

if __name__ == '__main__':
    main()
