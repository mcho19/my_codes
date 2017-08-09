import pandas as pd
import matplotlib.pyplot as plt

csv_name = '170525_golden_co.csv'
csv_path = '/Users/matthewchow/Downloads/'
path = csv_path + csv_name

df = pd.read_csv(path, sep=',', names=['timestamp','sensor_1','sensor_2','sensor_3','sensor_4','sensor_5','sensor_6'], header=0)

df['sensor_average'] = df.mean(axis=1)

df_avg = df[['timestamp','sensor_average']].copy()

# print(df_avg)

df_avg.plot(x='timestamp', y='sensor_average', rot=(45), figsize=(12,12) )
plt.savefig(csv_path + 'co_sensor_average.png')