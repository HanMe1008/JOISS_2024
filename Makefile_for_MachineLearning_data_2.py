# Step 1
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

df = pd.read_csv('BestTrack_since1994_WP.csv')
csv_time = pd.to_datetime(df['ISO_TIME'].values)

latitude = df['MEAN_LAT'].tolist()
longitude = df['MEAN_LON'].tolist()

temp_0m_yesterday = []
temp_10m_yesterday = []
temp_20m_yesterday = []
temp_30m_yesterday = []
temp_40m_yesterday = []
temp_50m_yesterday = []
temp_60m_yesterday = []
temp_70m_yesterday = []
temp_80m_yesterday = []
temp_90m_yesterday = []
temp_100m_yesterday = []

temp_0m_today = []
temp_10m_today = []
temp_20m_today = []
temp_30m_today = []
temp_40m_today = []
temp_50m_today = []
temp_60m_today = []
temp_70m_today = []
temp_80m_today = []
temp_90m_today = []
temp_100m_today = []

temp_0m_tomorrow = []

def append_nan():
    temp_0m_yesterday.append(np.NaN)
    temp_10m_yesterday.append(np.NaN)
    temp_20m_yesterday.append(np.NaN)
    temp_30m_yesterday.append(np.NaN)
    temp_40m_yesterday.append(np.NaN)
    temp_50m_yesterday.append(np.NaN)
    temp_60m_yesterday.append(np.NaN)
    temp_70m_yesterday.append(np.NaN)
    temp_80m_yesterday.append(np.NaN)
    temp_90m_yesterday.append(np.NaN)
    temp_100m_yesterday.append(np.NaN)

    temp_0m_today.append(np.NaN)
    temp_10m_today.append(np.NaN)
    temp_20m_today.append(np.NaN)
    temp_30m_today.append(np.NaN)
    temp_40m_today.append(np.NaN)
    temp_50m_today.append(np.NaN)
    temp_60m_today.append(np.NaN)
    temp_70m_today.append(np.NaN)
    temp_80m_today.append(np.NaN)
    temp_90m_today.append(np.NaN)
    temp_100m_today.append(np.NaN)

    temp_0m_tomorrow.append(np.NaN)

def process_nc_file(file_path, season, number, idx_start):
    dataset = xr.open_dataset(file_path)
    data = dataset['water_temp']
    nc_time = pd.to_datetime(dataset['time'].values)

    num = (df['SEASON'] == season) & (df['NUMBER'] == number)
    indices = np.where(num)[0]
    
    for i in indices:
        time_idx = np.where(nc_time == csv_time[idx_start])
        if time_idx[0].size == 0:
            append_nan()
        else:
            target_time = nc_time[time_idx]
            target_before_24h = target_time - pd.Timedelta(hours=24)
            target_after_24h = target_time + pd.Timedelta(hours=24)

            formatted_dates_before = pd.DatetimeIndex(target_before_24h.strftime('%Y-%m-%d %H:%M:%S'))
            formatted_dates_after = pd.DatetimeIndex(target_after_24h.strftime('%Y-%m-%d %H:%M:%S'))

            time_idx_before = np.where(nc_time == formatted_dates_before[0])
            time_idx_after = np.where(nc_time == formatted_dates_after[0])

            if time_idx_before[0].size == 0 or time_idx_after[0].size == 0:
                append_nan()
            else:
                temp_0m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=0).values)
                temp_10m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=5).values)
                temp_20m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=8).values)
                temp_30m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=10).values)
                temp_40m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=12).values)
                temp_50m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=14).values)
                temp_60m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=15).values)
                temp_70m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=16).values)
                temp_80m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=17).values)
                temp_90m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=18).values)
                temp_100m_yesterday.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                      .isel(time=time_idx_before[0], depth=19).values)
        
                temp_0m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=0).values)
                temp_10m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=5).values)
                temp_20m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=8).values)
                temp_30m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=10).values)
                temp_40m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=12).values)
                temp_50m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=14).values)
                temp_60m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=15).values)
                temp_70m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=16).values)
                temp_80m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=17).values)
                temp_90m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=18).values)
                temp_100m_today.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                  .isel(time=time_idx[0], depth=19).values)

                temp_0m_tomorrow.extend(data.sel(lat=latitude[idx_start], lon=longitude[idx_start], method='nearest')
                                     .isel(time=time_idx_after[0], depth=0).values)
        idx_start += 1
    
    return idx_start

def replace_nan_with_previous_depth():

    for i in range(len(temp_10m_today)):
        if np.isnan(temp_10m_today[i]):
            if not np.isnan(temp_0m_today[i]):
                temp_10m_today[i] = temp_0m_today[i]
        if np.isnan(temp_20m_today[i]):
            if not np.isnan(temp_10m_today[i]):
                temp_20m_today[i] = temp_10m_today[i]
        if np.isnan(temp_30m_today[i]):
            if not np.isnan(temp_20m_today[i]):
                temp_30m_today[i] = temp_20m_today[i]
        if np.isnan(temp_40m_today[i]):
            if not np.isnan(temp_30m_today[i]):
                temp_40m_today[i] = temp_30m_today[i]
        if np.isnan(temp_50m_today[i]):
            if not np.isnan(temp_40m_today[i]):
                temp_50m_today[i] = temp_40m_today[i]
        if np.isnan(temp_60m_today[i]):
            if not np.isnan(temp_50m_today[i]):
                temp_60m_today[i] = temp_50m_today[i]
        if np.isnan(temp_70m_today[i]):
            if not np.isnan(temp_60m_today[i]):
                temp_70m_today[i] = temp_60m_today[i]
        if np.isnan(temp_80m_today[i]):
            if not np.isnan(temp_70m_today[i]):
                temp_80m_today[i] = temp_70m_today[i]
        if np.isnan(temp_90m_today[i]):
            if not np.isnan(temp_80m_today[i]):
                temp_90m_today[i] = temp_80m_today[i]
        if np.isnan(temp_100m_today[i]):
            if not np.isnan(temp_90m_today[i]):
                temp_100m_today[i] = temp_90m_today[i]

    for i in range(len(temp_10m_yesterday)):
        if np.isnan(temp_10m_yesterday[i]):
            if not np.isnan(temp_0m_yesterday[i]):
                temp_10m_yesterday[i] = temp_0m_yesterday[i]
        if np.isnan(temp_20m_yesterday[i]):
            if not np.isnan(temp_10m_yesterday[i]):
                temp_20m_yesterday[i] = temp_10m_yesterday[i]
        if np.isnan(temp_30m_yesterday[i]):
            if not np.isnan(temp_20m_yesterday[i]):
                temp_30m_yesterday[i] = temp_20m_yesterday[i]
        if np.isnan(temp_40m_yesterday[i]):
            if not np.isnan(temp_30m_yesterday[i]):
                temp_40m_yesterday[i] = temp_30m_yesterday[i]
        if np.isnan(temp_50m_yesterday[i]):
            if not np.isnan(temp_40m_yesterday[i]):
                temp_50m_yesterday[i] = temp_40m_yesterday[i]
        if np.isnan(temp_60m_yesterday[i]):
            if not np.isnan(temp_50m_yesterday[i]):
                temp_60m_yesterday[i] = temp_50m_yesterday[i]
        if np.isnan(temp_70m_yesterday[i]):
            if not np.isnan(temp_60m_yesterday[i]):
                temp_70m_yesterday[i] = temp_60m_yesterday[i]
        if np.isnan(temp_80m_yesterday[i]):
            if not np.isnan(temp_70m_yesterday[i]):
                temp_80m_yesterday[i] = temp_70m_yesterday[i]
        if np.isnan(temp_90m_yesterday[i]):
            if not np.isnan(temp_80m_yesterday[i]):
                temp_90m_yesterday[i] = temp_80m_yesterday[i]
        if np.isnan(temp_100m_yesterday[i]):
            if not np.isnan(temp_90m_yesterday[i]):
                temp_100m_yesterday[i] = temp_90m_yesterday[i]

idx = 0
file_list = [
    ## Total 108 Typhoons, 6296 Data터

    ## 1994 (37 typhoons, 2392 data)
    ('data_1994_25.nc4', 1994, 25),
    ('data_1994_30.nc4', 1994, 30),
    ('data_1994_32.nc4', 1994, 32),
    ('data_1994_34.nc4', 1994, 34),
    ('data_1994_40.nc4', 1994, 40),
    ('data_1994_41.nc4', 1994, 41),
    ('data_1994_43.nc4', 1994, 43),
    ('data_1994_44.nc4', 1994, 44),
    ('data_1994_46.nc4', 1994, 46),
    ('data_1994_52.nc4', 1994, 52),
    ('data_1994_53.nc4', 1994, 53),
    ('data_1994_54.nc4', 1994, 54),
    ('data_1994_55.nc4', 1994, 55),
    ('data_1994_56.nc4', 1994, 56),
    ('data_1994_57.nc4', 1994, 57),
    ('data_1994_60.nc4', 1994, 60),
    ('data_1994_63.nc4', 1994, 63),
    ('data_1994_66.nc4', 1994, 66),
    ('data_1994_67.nc4', 1994, 67),
    ('data_1994_68.nc4', 1994, 68),
    ('data_1994_70.nc4', 1994, 70),
    ('data_1994_72.nc4', 1994, 72),
    ('data_1994_77.nc4', 1994, 77),
    ('data_1994_78.nc4', 1994, 78),
    ('data_1994_80.nc4', 1994, 80),
    ('data_1994_81.nc4', 1994, 81),
    ('data_1994_84.nc4', 1994, 84),
    ('data_1994_87.nc4', 1994, 87),
    ('data_1994_93.nc4', 1994, 93),
    ('data_1994_94.nc4', 1994, 94),
    ('data_1994_97.nc4', 1994, 97),
    ('data_1994_98.nc4', 1994, 98),
    ('data_1994_99.nc4', 1994, 99),
    ('data_1994_101.nc4', 1994, 101),
    ('data_1994_102.nc4', 1994, 102),
    ('data_1994_110.nc4', 1994, 110),
    ('data_1994_112.nc4', 1994, 112),

    ## 1995 (25 typhoons, 1226 data)
    ('data_1995_18.nc4', 1995, 18),
    ('data_1995_23.nc4', 1995, 23),
    ('data_1995_24.nc4', 1995, 24),
    ('data_1995_29.nc4', 1995, 29),
    ('data_1995_33.nc4', 1995, 33),
    ('data_1995_38.nc4', 1995, 38),
    ('data_1995_43.nc4', 1995, 43),
    ('data_1995_44.nc4', 1995, 44),
    ('data_1995_46.nc4', 1995, 46),
    ('data_1995_51.nc4', 1995, 51),
    ('data_1995_53.nc4', 1995, 53),
    ('data_1995_55.nc4', 1995, 55),
    ('data_1995_58.nc4', 1995, 58),
    ('data_1995_59.nc4', 1995, 59),
    ('data_1995_64.nc4', 1995, 64),
    ('data_1995_67.nc4', 1995, 67),
    ('data_1995_73.nc4', 1995, 73),
    ('data_1995_75.nc4', 1995, 75),
    ('data_1995_78.nc4', 1995, 78),
    ('data_1995_79.nc4', 1995, 79),
    ('data_1995_80.nc4', 1995, 80),
    ('data_1995_81.nc4', 1995, 81), 
    ('data_1995_84.nc4', 1995, 84), 
    ('data_1995_86.nc4', 1995, 86),
    ('data_1995_94.nc4', 1995, 94),

    # 1996 (32 typhoons, 1827 data)
    ('data_1996_25.nc4', 1996, 25), 
    ('data_1996_33.nc4', 1996, 33), 
    ('data_1996_35.nc4', 1996, 35), 
    ('data_1996_44.nc4', 1996, 44), 
    ('data_1996_48.nc4', 1996, 48), 
    ('data_1996_49.nc4', 1996, 49), 
    ('data_1996_50.nc4', 1996, 50), 
    ('data_1996_51.nc4', 1996, 51), 
    ('data_1996_53.nc4', 1996, 53), 
    ('data_1996_55.nc4', 1996, 55), 
    ('data_1996_56.nc4', 1996, 56), 
    ('data_1996_58.nc4', 1996, 58), 
    ('data_1996_60.nc4', 1996, 60), 
    ('data_1996_61.nc4', 1996, 61),
    ('data_1996_62.nc4', 1996, 62),
    ('data_1996_66.nc4', 1996, 66),
    ('data_1996_71.nc4', 1996, 71),
    ('data_1996_73.nc4', 1996, 73),
    ('data_1996_77.nc4', 1996, 77),
    ('data_1996_78.nc4', 1996, 78),
    ('data_1996_81.nc4', 1996, 81),
    ('data_1996_82.nc4', 1996, 82),
    ('data_1996_84.nc4', 1996, 84),
    ('data_1996_90.nc4', 1996, 90),
    ('data_1996_91.nc4', 1996, 91),
    ('data_1996_97.nc4', 1996, 97),
    ('data_1996_101.nc4', 1996, 101),
    ('data_1996_104.nc4', 1996, 104),
    ('data_1996_107.nc4', 1996, 107),
    ('data_1996_108.nc4', 1996, 108),
    ('data_1996_118.nc4', 1996, 118),
    ('data_1996_120.nc4', 1996, 120),

    # 1997 (14 typhoons, 851 data)
    ('data_1997_4.nc4', 1997, 4),
    ('data_1997_21.nc4', 1997, 21),
    ('data_1997_23.nc4', 1997, 23),
    ('data_1997_25.nc4', 1997, 25),
    ('data_1997_28.nc4', 1997, 28), 
    ('data_1997_29.nc4', 1997, 29),
    ('data_1997_31.nc4', 1997, 31),
    ('data_1997_36.nc4', 1997, 36),
    ('data_1997_37.nc4', 1997, 37),
    ('data_1997_47.nc4', 1997, 47), 
    ('data_1997_52.nc4', 1997, 52),
    ('data_1997_53.nc4', 1997, 53), 
    ('data_1997_55.nc4', 1997, 55),

]

for file_path, season, number in file_list:
    idx = process_nc_file(file_path, season, number, idx)

replace_nan_with_previous_depth()

# Step 2
pressure = df['MEAN_PRES'].tolist()
wind = df['MEAN_WIND'].tolist()
storm_speed = df['STORM_SPEED'].tolist()

today_0m_arr = np.array(temp_0m_today)

def get_non_nan_idx(arr):
    return np.where(~np.isnan(arr))[0]

non_nan_idx = get_non_nan_idx(today_0m_arr)

def filter_data(data_list, non_nan_idx):
    return [np.array(data)[list(non_nan_idx)] for data in data_list]

temp_yesterday = [temp_0m_yesterday, temp_10m_yesterday, temp_20m_yesterday, temp_30m_yesterday,
                  temp_40m_yesterday, temp_50m_yesterday, temp_60m_yesterday, temp_70m_yesterday,
                  temp_80m_yesterday, temp_90m_yesterday, temp_100m_yesterday]

temp_today = [temp_0m_today, temp_10m_today, temp_20m_today, temp_30m_today, temp_40m_today,
              temp_50m_today, temp_60m_today, temp_70m_today, temp_80m_today, temp_90m_today,
              temp_100m_today]

latitude_arr, longitude_arr, pressure_arr, wind_arr, storm_speed_arr = filter_data(
    [latitude, longitude, pressure, wind, storm_speed], non_nan_idx)

temp_yesterday_filtered = filter_data(temp_yesterday, non_nan_idx)
temp_today_filtered = filter_data(temp_today, non_nan_idx)

temp_0m_tomorrow_filtered = np.array(temp_0m_tomorrow)[list(non_nan_idx)]

all_input = [
    [lat, lon, pres, wind, spd, *yes, *tod]
    for lat, lon, pres, wind, spd, yes, tod
    in zip(latitude_arr, longitude_arr, pressure_arr, wind_arr, storm_speed_arr,
           zip(*temp_yesterday_filtered), zip(*temp_today_filtered))
]

all_target = temp_0m_tomorrow_filtered

# Step 3
import csv

header = ['latitude', 'longitude', 'pressure', 'wind_speed', 'strom_speed',
          'temp_0m_yes', 'temp_10m_yes', 'temp_20m_yes', 'temp_30m_yes', 'temp_40m_yes', 'temp_50m_yes',
          'temp_60m_yes', 'temp_70m_yes', 'temp_80m_yes', 'temp_90m_yes', 'temp_100m_yes',
          'temp_0m_tod', 'temp_10m_tod', 'temp_20m_tod', 'temp_30m_tod', 'temp_40m_tod', 'temp_50m_tod',
          'temp_60m_tod', 'temp_70m_tod', 'temp_80m_tod', 'temp_90m_tod', 'temp_100m_tod',
          'temp_0m_tom'
           ]

for i in range(len(all_input)):
    all_input[i].append(all_target[i])  

with open('MachineLearningData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(all_input)

print("complete to save csv file")