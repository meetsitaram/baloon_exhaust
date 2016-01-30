# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:59:52 2016

@author: sitarama
"""
from math import pi, sqrt

def get_exhaust_velocity() :
    gma=1.3             # gamma of air - ratio of specific heats at const. press. to that a const. vol. at NTP
    R=8.3145            # universal gas constant in J/mol.K
    MolM=28.966/1000.   # molecular mass of air in g/mol
    TK=298.             # 25 degrees room temperature in kelvin
    pc=111990.          # pressure inside chamber(baloon)  (840 mmhg) - https://www.youtube.com/watch?v=fwh-i0WB_bQ
    pe=101325.          # pressure at exit of nozzle (760 hhmg) in N/m2 or 101325 kpa
    
    
    v_exhaust = sqrt( ((2.*gma/(gma-1))*R*TK/MolM)*(1- (pe/pc)**((gma-1)/gma) ) )
    print 'exhaust velocity:', v_exhaust, ' m/s' # result value : 112 m/s
    
    g = 9.81
    print 'specific impulse:', v_exhaust/g, ' sec' 
    
    return v_exhaust
    
def get_mass_of_air_in_baloon():

    p_a=101325.          # air pressure 101kpa
    p_c=111990.          # pressure inside chamber(baloon)  (840 mmhg) - https://www.youtube.com/watch?v=fwh-i0WB_bQ
    
    dia = .2794     # diameter of expanded baloon (11inch) in m
    volume_c = (4./3.)*pi*(dia/2.)**3
    volume_a = p_c*volume_c/p_a     # pv is const at given temp.
    
    density = 1.225     #kg/m3
    
    ma = density*volume_a    
    
    print 'mass of air :', ma*1000., ' grams'  # result 15 grams
    return ma
    
    
def get_baloon_thrust():
#    m_b = 1.8/1000.      # mass of baloon 1.8 grams approx. pack of 100 11inch baloons weighs 6.4 ounce (180g)
    
    ma = get_mass_of_air_in_baloon()
    
    total_exhaust_time = 3.      # 3 sec approx (only by visual observation)
    
    mass_flow_rate = ma / total_exhaust_time
    
    exhaust_velocity = get_exhaust_velocity()
    
    print 'air flow rate :', mass_flow_rate*1000., ' grams/msec'
    
    thrust = mass_flow_rate * exhaust_velocity
    
    print 'baloon thrust :', thrust*1000., ' mN'
    
    g = 9.81
    print 'lift capacity :', thrust*1000./g, ' grams'
      
    

get_baloon_thrust()