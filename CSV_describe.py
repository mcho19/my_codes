import pandas as pd
import numpy as nm

''' 
    Author: Matthew Chow
    Created: 04/26/2017
    Updated: 6/28/17
   
    This script will take a csv from Querybuilder, strip the timestamp and show statistical information such as mean, standard deviation, min & max 
    for the resulting data.
    
    This does not provide units.
    
'''

def qb_csv_parser(path):

    ''' This function will parse a QB csv file and spit out the statistical data for all columns. '''

    df = pd.read_csv(path, sep=',', skip_blank_lines=True, na_filter=True)
    df.columns = df.columns.str.split('__').str[2] # index at [2] for reference instruments, [3] for sensors

    print(df.describe())


if __name__ == '__main__':
    qb_csv_parser('co2_406.csv')