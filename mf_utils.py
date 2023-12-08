# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:39:19 2023

@author: solisgb
"""
import pandas as pd


def wells_to_df(well_pack, verbose=True):

    # Get the well data
    wel_data = well_pack.stress_period_data.get_data()
    print(f'The number of wells in the model is: {len(wel_data[0])}')
    
    # Print the well data for each stress period
    wdata = []
    # sp is the stree period
    for sp, data in wel_data.items():
        for wdata1 in data:
            if verbose:
                print(wdata1)
            wdata.append( (wdata1[3], wdata1[0][0], wdata1[0][1],
                           wdata1[2], wdata1[1] ) )
    print('Number of pumping rates (nwells*nstress_periods): ', len(wdata))
    col_names = ['well_id', 'layer', 'cell_id', 'stress_period',
                 'pumping_rate']
    wdata_df = pd.DataFrame(wdata, columns=col_names)    
    return wdata_df

