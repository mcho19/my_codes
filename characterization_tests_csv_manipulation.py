import pandas as pd
import numpy as np
import os
import errno

# file path of query builder file

date_of_test = "190606"
default_file = '~/Downloads/gas_cal_data/'
file_name = date_of_test + '-gascal-test.csv'
file_path = default_file + file_name

# file path of edited csv
# edited_file_name = '190523-gascal-test_edited.csv'
# edited_file_path = default_file + edited_file_name

# importing csv, setting timestamp as index
df = pd.read_csv(file_path, index_col="Datetime_UTC")

# changing column name
df.columns = ['o3']

# creating two dataframes
df_1 = df[(df['o3']>113)&(df['o3']<120)]
df_1_std = df_1.std()
df_1 = df_1.mean().astype(float)

df_2 = df[(df['o3']>120)]
df_2_std = df_2.std()
df_2 = df_2.mean().astype(float)

# percent difference calculation (gas calibrator subtract ozone concentration
# percent_difference_1 = abs((df_1 - 120) / 120)*100
# percent_difference_2 = abs((df_2 - 120) / 120)*100

# percent difference calculation (gas calibrator 1 - 2)
percent_difference_3 = abs((df_1 - df_2) / df_1)*100

# save data to text file

text_file = "/Users/matthew.chow/Downloads/gas_cal_data/" + date_of_test + "_gascal_percent_diff.txt"

if not os.path.exists(os.path.dirname(text_file)):
    try:
        os.makedirs(os.path.dirname(text_file))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# writing percent difference of gas cal 1 / gas cal 2 vs what concentration is reported
# with open(text_file, "w") as file:
#     file.write(date_of_test + "\n\n" + "gas calibrator 1 percent difference: " + str(float(percent_difference_1)) + "%" + "\n\n" +
#            "gas calibrator 2 percent difference: " + str(float(percent_difference_2)) + "%")
#     file.close()

# writing percent difference between gas cal 1 and gas cal 2
with open(text_file, "w") as file:
    file.write(date_of_test + "\n\n" + "percent difference: " + str(float(percent_difference_3)) + "%" + "\n\n"
               + "std gas cal 1 " + str(float(df_1_std)) + "\n\n"
               + "std gas cal 2 " + str(float(df_2_std)))
    file.close()


