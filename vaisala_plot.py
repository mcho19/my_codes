import pandas as pd
import matplotlib.pyplot as plt
import os
from calibration_modules.data_preprocessing import reformat_raw_data_download_files as reformat
import pandas as pd
import zipfile
import datetime as dt
import shutil

def parse_vaisala_putty():

    vaisala_putty_file = '/Users/matthewchow/Documents/Projects/calibration_folder/raw_data/170519_RH_T_comparisions/vaisala_log_20170518152718.txt'
    # vaisala_file = '/Users/matthewchow/Documents/Projects/calibration_folder/raw_data/170519_RH_T_comparisons/vaisala_log_20170518152718.csv'
    vaisala_file = vaisala_putty_file + '.txtprocessed_UTC.csv'
    starttime_gmt = '2017-05-18T22:27:00'
    endtime_gmt = '2017-05-19T16:57:00'


    try:
        vaisala_df = pd.read_csv(vaisala_file, parse_dates = True,
                                       index_col=0,header=0)
    except:
        vaisala_file = reformat.process_vaisala_from_putty(vaisala_putty_file)

        vaisala_df = pd.read_csv(vaisala_file, parse_dates = True,
                                       index_col=0,header=0)
    vaisala_df.index = pd.to_datetime(vaisala_df.index,format='%Y-%m-%d %H:%M:%S')
    # now drop the fractional!
    vaisala_df.index = vaisala_df.index.map(lambda t: t.replace(microsecond=0))
    grouped = vaisala_df.groupby(level=0)
    vaisala_df = grouped.last()
    names = vaisala_df.columns.tolist()

    # goal is to make a column format flat file, consistent with all of the other modalities.

def vaisla_plot():
    path = '/Users/matthewchow/Documents/Projects/calibration_folder/raw_data/170519_RH_T_comparisions/'
    file_name = 'vaisala_log_20170518152718.txtprocessed_UTC.csv'
    csv_path = path + file_name
    plot_path = '/Users/matthewchow/Documents/Projects/calibration_folder/raw_data/170519_RH_T_comparisions/'

    if not os.path.exists(plot_path):
        os.makedirs(plot_path)

    df = pd.read_csv(csv_path, sep=',', usecols=['Time_UTC','Temperature','Humidity'], na_filter=True)

    df.plot(x='Time_UTC', y='Temperature', rot=(45), figsize=(12,12))
    plt.savefig(plot_path + 'T_ref.png')

    df.plot(x='Time_UTC', y='Humidity', rot=(45), figsize=(12,12))
    plt.savefig(plot_path + 'RH_ref.png')


parse_vaisala_putty()
vaisla_plot()

