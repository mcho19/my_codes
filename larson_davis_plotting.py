'''

Author: Matthew Chow
Created date: 5/05/17
Updated: 5/11/17

This script will process sound files from the Larson Davis 831 reference file, specifically the raw data from the 
instrument; the data used is 'LAeq'



'''

import pandas as pd
import matplotlib.pyplot as plt
import datetime, pytz
from pytz import timezone
utc = pytz.utc

starttime_gmt = '2017-05-05 21:30:00'
endtime_gmt = '2017-05-08 16:35:00'

# Will take the last tab of the sound meter CSV file, process it and produce a temporal plot of LAeq.

path = '/Users/matthewchow/Documents/Projects/calibration_folder/raw_data/170508_cbre_sound/'
file_name = '170508_sound_file_CBRE.csv'
csv_path = path + file_name
plot_save_name = '150524_sound_plots'

df = pd.read_csv(csv_path, sep=',', skip_blank_lines=True, na_filter=True, usecols=['Date', 'Time','LAeq'])
df['timestamp'] = df['Date'] + ' ' + df['Time']
df.drop(['Time','Date'], axis=1, inplace=True)
df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_localize('US/Pacific').dt.tz_convert('UTC')\
    .apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
df1 = df[['timestamp','LAeq']]
df1.index = df1['timestamp']
del df1['timestamp']
df1 = df1[starttime_gmt:endtime_gmt]
df1 = df1.reset_index()

# df1_plot_LAeq = df1.plot(x='timestamp', y='LAeq', rot=(45), figsize=(12,12))
# plt.savefig(path + plot_save_name + '_LAeq.png')

# ==================================================================================================================== #

# Will take flatfiles and produce a temporal plot of sound (Db).

path2 = '/Users/matthewchow/Documents/Projects/calibration_folder/raw_data/170508_cbre_sound/processed/' \
        'sound_flatfile_single_week_1sec.csv'
path3 = '/Users/matthewchow/Documents/Projects/calibration_folder/raw_data/170508_cbre_sound/processed/'

df2 = pd.read_csv(path2, sep=',', skip_blank_lines=True, na_filter=True, parse_dates=True)
df2.index = df2['timestamp']
del df2['timestamp']
df2 = df2.reset_index()

# df2.plot(x='timestamp', rot=45, figsize= (12,12), legend=False)
# plt.savefig(path3 + 'sound_plot_cbre_170524.png')


# ==================================================================================================================== #

# combine sound meter csv files with sound flatfiles to produce temporal comparision plots.



