"""Merge monthly ERSST data files into a single data file."""

from pathlib import Path
import xarray as xr

home = str(Path.home())
datadir = home + '/data/ERSST_v5/raw/'
years = range(1880, 2017)
months = range(1, 13)
datafiles = [datadir + f'ersst.v5.{year}{month:02d}.nc' for year in years
             for month in months]
savefile = '../data/ERSST_v5_1880-2016.nc'

for i, datafile in enumerate(datafiles):
    print('Loading ' + datafile)
    with xr.open_dataset(datafile) as ds:
        ds.load()
        if i == 0:
            data = ds
        else:
            data = xr.concat([data, ds], dim='time')

print('Saving merged data to ' + savefile)
data.to_netcdf(savefile)
