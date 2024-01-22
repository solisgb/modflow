# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:39:19 2023

@author: solisgb
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_h_obs_sim_sta\
    (out_file: str, 
    obs: np.ndarray, 
    sim: np.ndarray, 
    rmse: float, 
    length_unit = 'm', 
    title = 'H medida vs. calculada en los puntos de observación',
    xlabel = 'h medida', ylabel = 'h calculada',
    zero_origin: bool=False):

    fig, ax = plt.subplots()

    # Scatter plot
    ax.scatter(obs, sim, label=f'RMSE {rmse}')

    if zero_origin:
        origin = 0.
    else:
        origin = np.floor(obs.min())


    # Diagonal line
    obs_max = obs.max()
    ax.plot([origin, obs_max], [origin, obs_max], color='red',
            linestyle='--')

    ax.set_title(title)
    ax.set_xlabel(f'{xlabel} ({length_unit})')
    ax.set_ylabel(f'{ylabel} ({length_unit})')
    
    ax.legend()
    ax.grid()
    
    fig.savefig(out_file)
    
    plt.show()