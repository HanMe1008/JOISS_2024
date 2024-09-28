### merge NetCDF file 

import xarray as xr

file1 = 'data_2015_37 (1).nc4'
file2 = 'data_2015_37 (2).nc4'

ds1 = xr.open_dataset(file1)
ds2 = xr.open_dataset(file2)

combined_ds = xr.concat([ds1, ds2], dim='time') 

combined_ds.to_netcdf('data_2015_37.nc4')

print("complete to merge nc file")