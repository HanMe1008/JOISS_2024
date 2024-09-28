# Step 1
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

df = pd.read_csv('for_testset_Download.csv')
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
    ## Testset
    ## Total 42 Typhoons, 267 Data

    ('data_1999_47.nc4', 1999, 47),
    ('data_1999_50.nc4', 1999, 50),
    ('data_1999_53.nc4', 1999, 53),
    ('data_1999_56.nc4', 1999, 56),
    ('data_1999_62.nc4', 1999, 62),
    ('data_1999_71.nc4', 1999, 71),
    ('data_1999_78.nc4', 1999, 78),
    ('data_1999_83.nc4', 1999, 83),

    ('data_2000_40.nc4', 2000, 40),
    ('data_2000_63.nc4', 2000, 63),
    ('data_2000_69.nc4', 2000, 69),

    ('data_2001_27.nc4', 2001, 27),
    ('data_2001_40.nc4', 2001, 40),

    ('data_2002_32.nc4', 2002, 32),
    ('data_2002_37.nc4', 2002, 37),

    ('data_2004_32.nc4', 2004, 32),

    ('data_2005_49.nc4', 2005, 49),
    ('data_2005_67.nc4', 2005, 67),

    ('data_2006_24.nc4', 2006, 24),
    ('data_2006_29.nc4', 2006, 29),

    ('data_2007_53.nc4', 2007, 53),
    ('data_2007_56.nc4', 2007, 56),

    ('data_2008_37.nc4', 2008, 37),

    ('data_2009_45.nc4', 2009, 45),

    ('data_2010_41.nc4', 2010, 41),
    ('data_2010_49.nc4', 2010, 49),
    ('data_2010_52.nc4', 2010, 52),
    ('data_2010_56.nc4', 2010, 56),

    ('data_2011_32.nc4', 2011, 32),
    ('data_2011_42.nc4', 2011, 42),

    ('data_2012_37.nc4', 2012, 37),
    ('data_2012_40.nc4', 2012, 40),
    ('data_2012_50.nc4', 2012, 50),
    ('data_2012_51.nc4', 2012, 51),

    ('data_2013_52.nc4', 2013, 52),

    ('data_2014_42.nc4', 2014, 42),
    ('data_2014_48.nc4', 2014, 48),
    ('data_2014_67.nc4', 2014, 67),

    ('data_2015_37.nc4', 2015, 37),
    ('data_2015_54.nc4', 2015, 54),

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

with open('TestsetData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(all_input)

print("complete to save csv file")