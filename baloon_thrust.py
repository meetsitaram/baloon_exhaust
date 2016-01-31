# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:59:52 2016

@author: sitarama
"""
from math import pi, sqrt

import matplotlib.pyplot as plt

gma=1.4             # gamma of air - ratio of specific heats at const. press. to that a const. vol. at NTP
R=8.3145            # universal gas constant in J/mol.K
MolM=28.966/1000.   # molecular mass of air in g/mol
T_A=298.             # 25 degrees room temperature in kelvin
T_BLOWN_AIR=310.    # assuming this is same as body temperature 37c
pc=107991.          # pressure inside chamber(baloon)  (810 mmhg) - https://www.youtube.com/watch?v=fwh-i0WB_bQ
#pa=101325.          # air pressure101325 kpa
pa=103991.          # air pressure (780 hhmg) in N/m2 as in video

air_density = 1.225     #kg/m3
expanded_dia = .228     # diameter of expanded baloon (9 inch - rough measurement) in m
exit_dia = .027           # measured 27mm
throat_dia = 0.018
g = 9.81
total_exhaust_time = 1.69      # 1.69 sec approx (measured using stopwatch)
#m_b = 1.8/1000.      # mass of baloon 1.8 grams approx. pack of 100 11inch baloons weighs 6.4 ounce (180g)
   
pe=pa            # pressure at exit of nozzle same as atm. press. with optimum nozzle

IDEAL_NOZZLE = False
if IDEAL_NOZZLE:
    pe = pa

def get_exhaust_velocity(press_exit) :

    v_exhaust = sqrt( ((2.*gma/(gma-1))*R*T_BLOWN_AIR/MolM)*(1- (press_exit/pc)**((gma-1)/gma) ) )
    #print 'exhaust velocity:', v_exhaust, ' m/s' # result value : 112 m/s
    
    #print 'specific impulse:', v_exhaust/g, ' sec' 
    
    return v_exhaust
    
def get_mass_of_air_in_baloon():
    volume_c = (4./3.)*pi*(expanded_dia/2.)**3
    volume_a = pc*volume_c*T_A/(pa*T_BLOWN_AIR)     # pv/T is const at given temp.
    
    ma = air_density*volume_a    
    
    print 'mass of air in baloon:', ma*1000., ' grams'  # result 7.5 grams
    return ma
    
def get_theoritical_exit_area_to_throat_area():
    nm1= ((gma-1)/2.) * ( 2./(gma+1) )**( (gma+1.)/(gma-1.) )
    dm1=(pe/pc)**(2./gma) * ( 1. - (pe/pc)**((gma-1)/(gma)) )
    ae_by_at = sqrt(nm1/dm1)   

    actual_throat_area = pi*(throat_dia/2.)**2
    actual_exit_area = pi*(exit_dia/2.)**2
    actual_ae_by_at = actual_exit_area / actual_throat_area
    
    print 'exit_area_to_throat_area, theoritical:', ae_by_at, ', actual:', actual_ae_by_at
    
    return ae_by_at
    
def get_baloon_thrust():
    
    
    ae = pi*(exit_dia/2.)**2.
    
    exhaust_velocity = get_exhaust_velocity(pe)
    
    print 'exhaust velocity:', exhaust_velocity, ' m/s'
    
    print 'specific impulse:', exhaust_velocity/g, ' sec'     

    ma = get_mass_of_air_in_baloon()    
    mass_flow_rate = ma / total_exhaust_time    
    
    print 'air flow rate :', mass_flow_rate*1000., ' grams/msec'
    
    exhaust_thrust = mass_flow_rate * exhaust_velocity

    
    
    thrust = exhaust_thrust  + pe*ae - pa*ae  # for now assuming pe = pa
    
    print 'baloon thrust :', thrust*1000., ' mN'

    print 'lift capacity :', thrust*1000./g, ' grams'
      
    
def plot_ve_vs_press_ratio():        
    rng = range(1000)
    percent_values = [(1000 - v)/1000. for v in rng]
    pressure_values = [ pc*percent for percent in percent_values if pc*percent >= pa]
    velocity_values = [get_exhaust_velocity(p) for p in pressure_values]
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt_v_vs_p, = ax1.plot([p/pc for p in pressure_values], [v for v in velocity_values], label= str(T_BLOWN_AIR) + ' K')
    ax1.set_xlabel('Pressure Ratio p/pc')
    ax1.set_ylabel('Exhaust Velocity m/s')
    plt.legend(handles=[plt_v_vs_p], loc='upper right')
    plt.show()    
    
   
plot_ve_vs_press_ratio()

get_theoritical_exit_area_to_throat_area()

get_baloon_thrust()

