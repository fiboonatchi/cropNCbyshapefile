# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:35:27 2023

@author: USER
"""

import geopandas
import xarray
import rioxarray
from shapely.geometry import mapping
import netCDF4
#import PyNIO
import scipy
import pydap
import h5netcdf
import os

for filename in os.listdir('C:/Users/USER/Desktop/Mahya/evaporation_volgabasin/GLEAM/'):

    if filename.split('.')[1] == 'nc':
            print(filename)
            MSWEP_monthly2 = xarray.open_dataset('C:/Users/USER/Desktop/Mahya/evaporation_volgabasin/GLEAM/'+filename)
            
            #MSWEP_monthly2 = xarray.open_dataset('C:/Users/USER/Desktop/Mahya/volga/file/precip_volga.nc')
            print(MSWEP_monthly2)
            
            
            
            
           # variable_name = 'e'
            variable_name = 'E'
            #variable_name = 'e'
            print(filename)
            variable = MSWEP_monthly2[variable_name]
            variable.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
            variable.rio.write_crs("epsg:4326", inplace=True)
            Africa_Shape = geopandas.read_file('C:/Users/USER/Desktop/Mahya/volga/volga.shp', crs="epsg:4326")

            clipped = variable.rio.clip(Africa_Shape.geometry.apply(mapping), Africa_Shape.crs, drop=False)
            fname=filename.split('.')[0]
            name=fname+'.nc'
            clipped.to_netcdf('C:/Users/USER/Desktop/Mahya/volga/crop/'+name)