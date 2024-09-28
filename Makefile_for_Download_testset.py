import pandas as pd

df = pd.read_csv('ibtracs.since1980.list.v04r01.csv')

columns_to_include = ['SID', 'SEASON', 'NUMBER', 'BASIN', 'SUBBASIN', 'NAME',
                      'ISO_TIME', 'NATURE', 'DIST2LAND', 'LANDFALL', 'STORM_SPEED',
                      'USA_LAT', 'USA_LON', 'USA_WIND', 'USA_PRES',
                      'TOKYO_LAT', 'TOKYO_LON', 'TOKYO_WIND', 'TOKYO_PRES',
                      'CMA_LAT', 'CMA_LON', 'CMA_WIND', 'CMA_PRES',
                      'HKO_LAT', 'HKO_LON', 'HKO_WIND', 'HKO_PRES',
                      'KMA_LAT', 'KMA_LON', 'KMA_WIND', 'KMA_PRES']
                      
df = df[columns_to_include]


df = df[df['BASIN'] == 'WP']
df = df[df['NAME'] != 'UNNAMED']
df = df[df['DIST2LAND'] != 0]
df['ISO_TIME'] = pd.to_datetime(df['ISO_TIME'])
df = df[df['ISO_TIME'] >= '1998-01-01 00:00:00']
df = df[df['ISO_TIME'] <  '2016-01-01 00:00:00']

df[['USA_LAT', 'USA_LON', 'USA_WIND', 'USA_PRES',
    'TOKYO_LAT', 'TOKYO_LON', 'TOKYO_WIND', 'TOKYO_PRES',
    'CMA_LAT', 'CMA_LON', 'CMA_WIND', 'CMA_PRES',
    'HKO_LAT', 'HKO_LON', 'HKO_WIND', 'HKO_PRES',
    'KMA_LAT', 'KMA_LON', 'KMA_WIND', 'KMA_PRES']] = df[['USA_LAT', 'USA_LON', 'USA_WIND', 'USA_PRES',
                                                        'TOKYO_LAT', 'TOKYO_LON', 'TOKYO_WIND', 'TOKYO_PRES',
                                                        'CMA_LAT', 'CMA_LON', 'CMA_WIND', 'CMA_PRES',
                                                        'HKO_LAT', 'HKO_LON', 'HKO_WIND', 'HKO_PRES',
                                                        'KMA_LAT', 'KMA_LON', 'KMA_WIND', 'KMA_PRES']].apply(pd.to_numeric, errors='coerce')

df['MEAN_LAT'] = df[['USA_LAT', 'TOKYO_LAT', 'CMA_LAT', 'HKO_LAT', 'KMA_LAT']].mean(axis=1)
df['MEAN_LON'] = df[['USA_LON', 'TOKYO_LON', 'CMA_LON', 'HKO_LON', 'KMA_LON']].mean(axis=1)
df['MEAN_WIND'] = df[['USA_WIND', 'TOKYO_WIND', 'CMA_WIND', 'HKO_WIND', 'KMA_WIND']].mean(axis=1)
df['MEAN_PRES'] = df[['USA_PRES', 'TOKYO_PRES', 'CMA_PRES', 'HKO_PRES', 'KMA_PRES']].mean(axis=1)

df = df.dropna(subset=['MEAN_LAT', 'MEAN_LON', 'MEAN_WIND', 'MEAN_PRES'])

new_column_order = ['SID', 'SEASON', 'NUMBER', 'NAME', 'ISO_TIME',
                    'MEAN_LAT', 'MEAN_LON', 'MEAN_WIND', 'MEAN_PRES',
                    'NATURE', 'DIST2LAND', 'LANDFALL', 'STORM_SPEED']
                    
df = df[new_column_order]

condition_1 =(df['MEAN_LON'] >= 119.1) & (df['MEAN_LON'] <= 126.5) & (df['MEAN_LAT'] >= 31.4) & (df['MEAN_LAT'] <= 39.5)

filtered_df = df[condition_1]

# 결과 출력
print(filtered_df)

filtered_df.to_csv('for_testset_Download.csv', index=False)

print("complete to save csv file")
