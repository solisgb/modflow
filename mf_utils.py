# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:39:19 2023

@author: solisgb
"""
import pandas as pd


def wells_to_df(well_pack, verbose=True) -> pd.DataFrame:
    """
    Returns wells data as a dataframe

    Parameters
    ----------
    well_pack : mf6 well package class
    verbose : if True display extra information.

    Returns
    -------
    wdata_df : well data as a pandas dataframe
    """

    # Get the well data
    wdata = wells_to_tuple(well_pack, verbose)
    col_names = ['layer', 'cell_id', 'pumping_rate', 'stress_period', 
                 'well_id']
    wdata_df = pd.DataFrame(wdata, columns=col_names)    
    return wdata_df


def wells_to_tuple(well_pack, verbose=True) -> [()]:
    """
    Returns wells data as a list of tuples
    Parameters
    ----------
    well_pack : mf6 well package class
    verbose : if True display extra information.

    Returns
    -------
    wdata : well data as a list of tuples

    """

    # Get the well data
    well_sp_data = well_pack.stress_period_data.get_data()
    print(f'The number of wells in the model is: {len(well_sp_data[0])}')
    
    # Print the well data for each stress period
    wdata = []
    # sp is the stree period
    for sp, data in well_sp_data.items():
        for wdata1 in data:
            if verbose:
                print(wdata1)
            wdata.append( (wdata1[0][0], wdata1[0][1],
                           wdata1[1], wdata1[2], wdata1[3] ) )
    print('Number of pumping rates (nwells*nstress_periods): ', len(wdata))
    
    return wdata


def wells_update_pumping_rates(well_pck, new_pumping_rates: dict) -> None:
    """
    Update wells pumping rates stored in new_pumping_rates

    Parameters
    ----------
    well_pack : well package
    well_data : dict
        key: (well identifier, stress period, layer, cell identifier)
        value: new pumping rate

    Returns
    -------
    None.

    """
    # Get the well data
    well_sp_data = well_pck.stress_period_data.get_data()
    
    # Change the pumping rates
    for sp, data in well_sp_data.items():
        data_updated = False
        for i, well in enumerate(data):
            if (well[3], well[2], well[0][0], well[0][1]) in new_pumping_rates:
                data[i] = (well[0], new_pumping_rates[(well[3], well[2], well[0][0], well[0][1])], well[2], well[3])
                data_updated = True
                print(f'{well[3]}has been updated')
        if data_updated:
            well_sp_data[sp] = data
    
    # Update the well data
    well_pck.stress_period_data.set_data(well_sp_data)
    return None
